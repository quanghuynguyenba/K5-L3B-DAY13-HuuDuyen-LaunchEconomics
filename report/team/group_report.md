# Báo cáo nhóm

## 1. Thông tin nhóm

- Tên nhóm: HuuDuyen
- Lớp: L3B
- Thành viên: Mai Danh Hiếu, Lê Tuấn Đạt, Vũ Huy Hiệu, Nguyễn Bá Quang Huy
- Phân vai: xem `TEAM.md`.

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá hiệu quả kinh tế và rủi ro vận hành của trợ lý hoàn phí LogiX-VN trên bộ dữ liệu giả lập gồm 1.200 yêu cầu và 1.624 lần chạy. Mục tiêu là chuẩn bị hồ sơ xin duyệt kế hoạch pilot tại Gate 2a, không phải xin mở rộng triển khai chính thức.

Nhóm thực hiện mô hình chi phí và phân tích độ nhạy (A–B), gắn nhãn độc lập 20 ca lỗi (C), tính cỡ mẫu và lập kế hoạch pilot (D), sau đó tổng hợp chỉ số, event và rủi ro (E).

## 3. Kết quả chính

- **Chi phí (A):** Tổng mô hình là 4.373.585đ cho 978 việc thành công, tương đương khoảng 4.472đ/việc. Hoá đơn token và tool chia cho 1.200 yêu cầu là 274,7đ/yêu cầu; tỷ số khoảng 16,3 lần. Chi phí xem lại và làm lại dựa trên dữ liệu `_simulated`, nên tổng chi phí và chi phí mỗi việc thành công có phần giả lập.
- **Phạm vi và độ nhạy (A–B):** `noi_dia` là 2.696đ/việc (0,22× mức 12.000đ của nhân viên) và `hang_nang` là 8.221đ (0,69×); `quoc_te` là 22.515đ (1,88×). Số ca làm lại là yếu tố nhạy nhất: tăng gấp đôi làm chi phí lên 6.787đ/việc (+51,8%). Giới hạn 2 lần chạy có tổng chi phí hệ thống thấp nhất trong ba phương án, 6.901.220đ. Các kết quả có phần giả lập.
- **Phân loại lỗi (C):** Hai người gắn nhãn độc lập đạt 19/20 ca, tương đương 95% đồng thuận. Ca bất đồng là ca 9; nhóm thống nhất nhãn “Do người dùng” theo nguyên nhân gốc. Bảng khắc phục có đủ năm loại lỗi.
- **Kế hoạch pilot (D):** Nhóm chọn chia theo nhân viên: 20 người dùng trợ lý và 20 người đối chứng. Với giới hạn 40 nhân viên, không đủ mẫu để phát hiện mức chênh 5 điểm; nhóm chấp nhận MDE 6 điểm, cần 859 yêu cầu mỗi nhóm và tối thiểu 299 yêu cầu mỗi nhân viên. Nếu tác động thật chỉ là 5 điểm, power ước tính khoảng 0,64.
- **Chỉ số (E):** Chỉ số chính trong bộ dữ liệu là 82,83% (994/1.200); tỉ lệ bỏ qua gợi ý là 27,12% (48/177); tỉ lệ mở lại trong 7 ngày là 4,25% (51/1.200). Đây là số liệu chạy thử, không chứng minh trợ lý đã cải thiện kết quả so với đối chứng.

Chi tiết xem tại [bang_chi_phi.md](bang_chi_phi.md), [bang_loi.md](bang_loi.md), [pilot_plan.yaml](pilot_plan.yaml), [chi_so.md](chi_so.md) và [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Đề xuất Gate 2a

Nhóm đề xuất **Go có điều kiện** cho pilot giới hạn ở `noi_dia` và `hang_nang`. Điều kiện gồm triển khai idempotency key và đối soát sổ cái, bật logging cần thiết, ghi rõ việc chấp nhận MDE 6 điểm, và thay các giả định thời gian giả lập bằng số đo thực tế trong pilot. Áp dụng các luật dừng và rollback đã ghi trong `pilot_plan.yaml`.

## 5. Khó khăn và hạn chế

- Thời gian xem lại và làm lại hiện lấy từ các cột `_simulated`; cần đo thời gian thực qua event trong pilot.
- Cỡ mẫu hiện có không đủ để phát hiện mức chênh 5 điểm theo thiết kế cụm; lựa chọn MDE 6 điểm làm giảm khả năng phát hiện hiệu quả nhỏ hơn.
- Cần kiểm tra mẫu định kỳ để phát hiện lỗi ngầm về số tiền hoàn và phiên bản bảng giá.

## 6. Đóng góp của thành viên

- **Mai Danh Hiếu (2A202603948), người viết code:** phụ trách code và kết quả A–B trong `src/lab13.py` và `report/team/bang_chi_phi.md`.
- **Lê Tuấn Đạt (2A202603949), người gắn nhãn 2 kiêm giữ hồ sơ:** phụ trách bộ nhãn độc lập thứ hai và hồ sơ launch; chi tiết trong `report/team/2A202603949_LeTuanDat.md`.
- **Vũ Huy Hiệu (2A202603979), người gắn nhãn 1:** phụ trách bộ nhãn độc lập thứ nhất; chi tiết trong `report/team/2A202603979_VuHuyHieu.md`.
- **Nguyễn Bá Quang Huy (2A202603926), người kiểm số:** đối chiếu phép tính và số liệu trong bảng chi phí; chi tiết trong `report/team/2A202603926_NguyenBaQuangHuy.md`.

## 7. Duyệt chéo

Kết quả hội đồng: **chưa cập nhật**. Bổ sung điểm, lý do và câu hỏi/câu trả lời sau phiên duyệt chéo theo `report/team/phieu_cham.md`; không suy đoán kết quả trước khi có phiếu.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương “Errors + Graceful Failure”, https://pair.withgoogle.com
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`stats.power`).
