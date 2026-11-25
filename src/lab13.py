"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


def xem_lai_tat_ca(runs, reqs, phut_lam_lai=9):
    """B4: xem lại mỗi yêu cầu có ít nhất một lượt chạy ok, 5 phút/yêu cầu."""
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    so_xem_lai = runs.loc[runs['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = (reqs['ket_qua'] == 'lam_lai').sum()
    hoa_don = (runs['tokens_in'].sum() * GIA_VAO / 1000
               + runs['tokens_out'].sum() * GIA_RA / 1000
               + runs['tool_calls'].sum() * GIA_TOOL)
    tong = hoa_don + so_xem_lai * 5 * LUONG_PHUT + so_lam_lai * phut_lam_lai * LUONG_PHUT
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(so_xem_lai=so_xem_lai, so_lam_lai=so_lam_lai,
                hoa_don=hoa_don, tong=tong, thanh_cong=thanh_cong,
                cps=tong / thanh_cong)


if __name__ == '__main__':
    if sys.stdout.encoding.lower() != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    print('\nA3 · Theo loại yêu cầu')
    for loai, nhom in reqs.groupby('loai', sort=False):
        kq = mo_hinh(runs, nhom)
        so_lan = len(runs[runs['request_id'].isin(nhom['request_id'])]) / len(nhom)
        print(f'{loai:12s} {len(nhom):4d} yêu cầu  '
              f'{kq["thanh_cong"] / len(nhom):6.1%} thành công  '
              f'{so_lan:.2f} lần/yêu cầu  {kq["cps"]:,.0f} đ/việc  '
              f'{kq["cps"] / BASELINE:.2f}× baseline [simulated]')

    print('\nA4 · Phạm vi noi_dia + hang_nang')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pham_vi = mo_hinh(runs, pham_vi)
    for so_yeu_cau in (45_000, 22_500):
        viec_thanh_cong = so_yeu_cau * kq_pham_vi['thanh_cong'] / len(reqs)
        co_dinh = 40_000_000 / viec_thanh_cong
        print(f'{so_yeu_cau:,} yêu cầu/tháng: {viec_thanh_cong:,.0f} việc thành công, '
              f'cố định {co_dinh:,.0f} đ/việc, '
              f'tổng {kq_pham_vi["cps"] + co_dinh:,.0f} đ/việc [simulated]')
    print('\nB1 · Độ nhạy từng yếu tố [simulated]')
    kich_ban = {
        'Token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Token giảm nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ 1 lần': dict(max_lan_chay=1),
    }
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        print(f'{ten:20s} {cps:>9,.0f} đ/việc  {(cps / ket_qua["cps"] - 1):+7.1%}')

    print('\nB2 · Token và xem lại cùng gấp đôi [simulated]')
    kep = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    print(f'{kep["cps"]:,.0f} đ/việc  {(kep["cps"] / ket_qua["cps"] - 1):+.1%}')

    print('\nB3 · Giới hạn số lần chạy [simulated]')
    for gioi_han in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        that_bai = len(reqs) - kq['thanh_cong']
        ca_he_thong = kq['tong'] + BASELINE * that_bai
        print(f'{gioi_han} lần: trợ lý {kq["tong"]:,.0f} đ; không thành công {that_bai}; '
              f'cả hệ thống {ca_he_thong:,.0f} đ; {kq["cps"]:,.0f} đ/việc')

    print('\nB4 · Xem lại 100% noi_dia + hang_nang [simulated]')
    phut_thuc_te_gia_lap = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    phut_trung_binh = phut_thuc_te_gia_lap.mean()
    for phut in (9, round(phut_trung_binh, 1)):
        kq = xem_lai_tat_ca(runs, pham_vi, phut_lam_lai=phut)
        hoa_von = (BASELINE * kq['thanh_cong'] - kq['hoa_don']
                   - kq['so_lam_lai'] * phut * LUONG_PHUT) / (kq['so_xem_lai'] * LUONG_PHUT)
        print(f'{phut:.1f} phút làm lại/ca: {kq["so_xem_lai"]} xem lại, '
              f'{kq["so_lam_lai"]} làm lại; tổng {kq["tong"]:,.0f} đ; '
              f'{kq["cps"]:,.0f} đ/việc ({kq["cps"] / BASELINE:.2f}×); '
              f'xem lại hòa vốn ≤ {hoa_von:.1f} phút')
    # Nhiệm vụ D · cỡ mẫu & chỉ số thử nghiệm (CP4, E1)
    def co_mau(p1, p2, alpha=0.05, power=0.80):
        za = NormalDist().inv_cdf(1 - alpha / 2)
        zb = NormalDist().inv_cdf(power)
        pb = (p1 + p2) / 2
        return math.ceil(
            (za * math.sqrt(2 * pb * (1 - pb))
             + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2
        )

    icc = 0.02
    n_5diem = co_mau(0.70, 0.75)
    de_75 = 1 + (75 - 1) * icc
    n_theo_nv_75 = math.ceil(n_5diem * de_75)
    n_6diem = co_mau(0.70, 0.76)
    m_6diem = math.ceil(n_6diem * (1 - icc) / (20 - n_6diem * icc))
    de_6diem = 1 + (m_6diem - 1) * icc
    print('\nD1 · Cỡ mẫu pilot (baseline=0.70, alpha=0.05, power=0.80, ICC=0.02)')
    print(f'a) Theo yêu cầu (+5 điểm): {n_5diem:,} yêu cầu/nhóm')
    print(f'b) Theo nhân viên m=75: DE={de_75:.2f}, {n_theo_nv_75:,}/nhóm '
          f'({math.ceil(n_theo_nv_75 / 75)} nhân viên/nhóm > 40 tổng)')
    print(f'c) 20 nhân viên/nhóm: tối đa {20 / icc:,.0f} < {n_5diem:,} (không đạt +5 điểm)')
    print(f'd) 6 depot/nhóm: tối đa {6 / icc:,.0f} (không đạt)')
    print(f'e) Mức chênh 6 điểm ({n_6diem:,}/nhóm), 20 nhân viên/nhóm: '
          f'm >= {m_6diem} yêu cầu/người (DE={de_6diem:.2f})')

    try:
        from statsmodels.stats.proportion import proportion_effectsize
        from statsmodels.stats.power import NormalIndPower
        power_5 = NormalIndPower().power(
            effect_size=proportion_effectsize(0.75, 0.70), nobs1=n_6diem, alpha=0.05, ratio=1.0
        )
        print(f'   Power ở mức chênh 5 điểm với n={n_6diem}: {power_5:.2f}')
    except ImportError:
        pass

    mo_lai_all = reqs['mo_lai_trong_7_ngay'].mean()
    mo_lai_pv = pham_vi['mo_lai_trong_7_ngay'].mean()
    print(f'D3 · Mở lại 7 ngày hiện tại: toàn bộ {mo_lai_all:.2%} '
          f'({reqs["mo_lai_trong_7_ngay"].sum()}/{len(reqs)}), '
          f'noi_dia+hang_nang {mo_lai_pv:.2%} '
          f'({pham_vi["mo_lai_trong_7_ngay"].sum()}/{len(pham_vi)})')

    chinh = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).mean()
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).mean()
    print(f'\nE1 · Chỉ số thử trên 1.200 yêu cầu: chính={chinh:.2%}, '
          f'bỏ qua gợi ý={bo_qua:.2%}, mở lại 7 ngày={mo_lai_all:.2%}')
