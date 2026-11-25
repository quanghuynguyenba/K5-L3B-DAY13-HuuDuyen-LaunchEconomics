# Báo cáo cá nhân — MaiDanhHieu-2A202603948


## 1. Thông tin thành viên

- Họ tên: Mai Danh Hiếu
- MSSV: 2A202603948
- Email: 
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code (CP1–CP2) kiêm Người gắn nhãn 1 (CP3)

## 2. Phần việc phụ trách

Phụ trách viết và chạy code CP1 (A1–A4) và CP2 (B1–B4) trong `src/lab13.py` để cung cấp kết quả cho bảng chi phí; đồng thời đảm nhiệm vai trò Người gắn nhãn 1 trong CP3 (gắn nhãn độc lập 20 ca lỗi theo Google PAIR).

## 3. Đóng góp cụ thể

- Viết ba hàm A1: số lần chạy kỳ vọng, tỉ lệ thành công và hệ số chi phí mỗi việc thành công.
- Hoàn thiện `mo_hinh()` để tính chi phí token, tool, xem lại, làm lại từ hai file CSV; tính số việc thành công và chi phí mỗi việc thành công.
- Tính kết quả theo bốn loại yêu cầu (A3) và phân bổ chi phí cố định 40 triệu đồng/tháng cho phạm vi `noi_dia` + `hang_nang` ở hai mức khối lượng (A4).
- Điền kết quả A1–A4 vào `report/team/bang_chi_phi.md`; đánh dấu `simulated` cho số sử dụng thời gian giả lập.
- Tính chín kịch bản độ nhạy B1, kịch bản kết hợp và xếp hạng B2; so sánh giới hạn 1–3 lần chạy theo chi phí cả hệ thống B3.
- Tính B4 cho trường hợp xem lại 100% trong phạm vi pilot, với hai giả định thời gian làm lại và mức hòa vốn; điền B1–B4 vào bảng chi phí.
- Gắn nhãn độc lập 20 ca lỗi (CP3) trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` theo 5 loại của Google PAIR với vai trò Người gắn nhãn 1 (không trao đổi trước khi so nhãn).
- Đối chiếu bộ nhãn với Lê Tuấn Đạt (Người gắn nhãn 2), đạt tỉ lệ đồng thuận 19/20 = 95% (đạt chuẩn >= 80%).
- Tranh luận và thống nhất quy tắc phân loại cho ca bất đồng số 9 (chuyển từ `Hệ thống` sang `Do người dùng` theo nguyên nhân gốc) và hoàn thiện bảng khắc phục 5 ca đại diện (Ca 9, 7, 18, 4, 17).

## 4. Bằng chứng

- `src/lab13.py`: chạy `python lab13.py` từ thư mục `src/`, ba phép thử A1 in **ĐẠT**.
- `report/team/bang_chi_phi.md`: bảng A1–A4 và câu trả lời CP1.
- Kết quả A2: tổng chi phí 4.373.585 đ, 978 việc thành công, 4.472 đ/việc thành công [simulated]; đối chiếu với số trong hướng dẫn chi tiết của repo.
- Kết quả A4: 4.599 đ/việc ở 45.000 yêu cầu/tháng và 5.784 đ/việc ở một nửa khối lượng [simulated].
- Kết quả B2: số ca làm lại là yếu tố ảnh hưởng mạnh nhất (+51,8% khi gấp đôi) [simulated].
- Kết quả B3: giới hạn 2 lần chạy có chi phí cả hệ thống thấp nhất, 6.901.220 đ [simulated].
- Kết quả B4: xem lại 100% có chi phí 11.743 đ/việc khi làm lại 9 phút/ca và 12.415 đ/việc khi làm lại 15,3 phút/ca [simulated].
- `report/team/bang_loi.md`: 20 nhãn độc lập của Người gắn nhãn 1 (Mai Danh Hiếu), tỉ lệ đồng thuận 19/20 = 95%, quy tắc phân biệt ca 9 và bảng khắc phục 5 ca đại diện có event đo lường và vai trò phụ trách duy nhất.
- `TEAM.md`: cập nhật vai trò `Người viết code (CP1–CP2) kiêm Người gắn nhãn 1`.

## 5. Công cụ AI đã dùng

Sử dụng Codex / Antigravity để hỗ trợ viết code, rà soát báo cáo CP1–CP3 và đối chiếu quy chuẩn nộp bài. Tự kiểm tra bằng cách chạy `python lab13.py`, xác nhận ba phép thử A1 **ĐẠT** và đối chiếu A2–B4 với tài liệu `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; kiểm tra phép chia của B4 khi số làm tròn trong hướng dẫn lệch 1 đ; rà soát thủ công 20 ca gắn nhãn độc lập CP3 theo nguyên nhân gốc trước khi đối chiếu.

## 6. Tự đánh giá

Đã hoàn thành phần code và số liệu CP1–CP2 cùng phần gắn nhãn độc lập CP3 (Người gắn nhãn 1). Kết quả chi phí nhân sự hiện dựa trên các cột `_simulated`, chưa phải số đo vận hành thực tế.
