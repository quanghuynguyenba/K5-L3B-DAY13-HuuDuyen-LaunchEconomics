# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: HuuDuyen
- Lớp: L3B
- Thành viên: xem `TEAM.md` (4 thành viên: Mai Danh Hiếu, Lê Tuấn Đạt, Vũ Huy Hiệu, Nguyễn Bá Quang Huy)

## 2. Mục tiêu và cách tiếp cận

Đánh giá hiệu quả kinh tế thực tế và mức độ sẵn sàng vận hành của trợ lý hoàn phí LogiX-VN trên dữ liệu chạy thử giả lập (1.200 yêu cầu, 1.624 lần chạy), từ đó lập bộ hồ sơ launch v0 trình Hội đồng Gate 2a xin phê duyệt kế hoạch chạy **pilot** (chưa phải mở rộng toàn bộ). Nhóm chia 4 vai trò rõ ràng: phân tích chi phí và độ nhạy bằng Python, gắn nhãn lỗi độc lập theo chuẩn Google PAIR, thiết kế pilot đủ năng lực thống kê và tổng hợp hồ sơ một trang.

## 3. Giải pháp

- **Nhiệm vụ A & B (CP1–CP2):** Code mô hình chi phí từ trace trong `src/lab13.py` (tính mọi lần chạy kể cả lỗi + giờ xem lại/làm lại chia cho số việc thành công), tách 4 loại yêu cầu, cộng chi phí cố định 40 triệu đ/tháng và chạy 9 kịch bản độ nhạy trong [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (CP3):** Hai thành viên gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, đối chiếu đạt đồng thuận 95% (19/20 ca), thống nhất quy tắc phân biệt ca bất đồng số 9 và lập bảng khắc phục 5 ca đại diện trong [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (CP4):** Tính cỡ mẫu cụm (ICC = 0,02) trong `src/lab13.py` và hoàn thiện kế hoạch thử nghiệm ngẫu nhiên phân tầng theo nhân viên (20 + 20) kèm 3 luật dừng 4 vế trong [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (CP5):** Đặc tả chỉ số, 10 event có `trace_id` và rủi ro kinh tế trong [chi_so.md](chi_so.md); tổng hợp thành hồ sơ 1 trang [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

- **Chi phí thật:** 4.472 đ/việc thành công [simulated], gấp 16,3× hoá đơn token + tool chia đều (274,7 đ/yc); giờ nhân viên chiếm 92,5% tổng chi phí.
- **Phạm vi pilot & độ nhạy:** Chỉ giữ `noi_dia` (2.696 đ, 0,22×) và `hang_nang` (8.221 đ, 0,69×); loại `quoc_te` (22.515 đ, 1,88×) và `doi_tac`. Giới hạn 2 lần chạy rẻ nhất cả hệ thống (6.901.220 đ [simulated]). Yếu tố nhạy nhất là số ca làm lại (+51,8% khi gấp đôi); xem lại 100% có thể nâng chi phí lên 11.743–12.415 đ/việc [simulated].
- **Đề xuất Gate 2a:** **Go có điều kiện** cho pilot phạm vi `noi_dia` + `hang_nang` (triển khai idempotency key và đối soát sổ cái, ký chấp nhận MDE 6 điểm, bật đủ 10 event và lộ trình giảm xem lại theo bậc).
- **Kết quả duyệt chéo từ hội đồng:** *(Điền sau phiên duyệt chéo tại lớp trong `report/team/phieu_cham.md`).*

## 5. Khó khăn và cách xử lý

- Với 40 nhân viên hiện tại, cỡ mẫu hiệu dụng tối đa không đủ phát hiện mức chênh +5 điểm (1.000 < 1.251); nhóm xử lý bằng cách chọn MDE +6 điểm (n = 859/nhóm, m ≥ 299 yêu cầu/nhân viên) và ghi rõ đánh đổi power 0,64 ở mức +5 điểm.
- Ở CP3, hai người gắn nhãn ban đầu lệch nhau ở ca 9 (`Hệ thống` vs `Do người dùng`); nhóm đối chiếu lại nguyên tắc "gắn theo nguyên nhân gốc, không theo chỗ cần sửa" để thống nhất nhãn `Do người dùng`.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`:

- **Mai Danh Hiếu (`2A202603948`) — Người viết code (CP1–CP2):** hoàn thiện `src/lab13.py` cho A1–B4, chạy kiểm tra A1 **ĐẠT**, tính mô hình chi phí và các kịch bản độ nhạy; điền [bang_chi_phi.md](bang_chi_phi.md). Chi tiết trong `report/team/2A202603948_MaiDanhHieu.md`.
- **Lê Tuấn Đạt (`2A202603949`) — Người gắn nhãn 2 kiêm giữ hồ sơ:** gắn nhãn độc lập 20 ca lỗi CP3, đối chiếu thống nhất ca 9 và hoàn thiện bảng khắc phục 5 ca trong [bang_loi.md](bang_loi.md); giữ và tổng hợp [ho_so_launch_v0.md](ho_so_launch_v0.md), hoàn thiện CP4–CP5. Chi tiết trong `report/team/2A202603949_LeTuanDat.md`.
- **Vũ Huy Hiệu (`2A202603979`) — Người gắn nhãn 1 (CP3):** gắn nhãn độc lập 20 ca lỗi CP3 đạt đồng thuận 95% với Lê Tuấn Đạt, tham gia tranh luận ca 9 và hoàn thiện bảng khắc phục 5 ca lỗi. Chi tiết trong `report/team/2A202603979_VuHuyHieu.md`.
- **Nguyễn Bá Quang Huy (`2A202603926`) — Người kiểm số & Nhóm trưởng:** đối chiếu số liệu tính tay, rà soát và duyệt merge các nhánh trên GitHub nhóm, điều phối chốt hồ sơ Gate 2a.

## 7. Hạn chế và hướng cải thiện

- Thời gian xem lại và làm lại hiện dựa trên hai cột `_simulated`; cần đo thời gian thực từ event `staff_review_decision` và `staff_rework_completed` ngay sau tuần 1 của pilot.
- Cần bổ sung kiểm tra mẫu ngẫu nhiên 100 đơn/tuần để phát hiện sớm các lỗi ngầm về chi phí và bảng giá đệm.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`stats.power`)
