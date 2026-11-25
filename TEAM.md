# Team

## Thông tin nhóm

- Tên nhóm: HuuDuyen
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-HuuDuyen-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/quanghuynguyenba/K5-L3B-DAY13-HuuDuyen-LaunchEconomics · Nhánh: main · Commit chốt: 2a8ad1a

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Mai Danh Hiếu | 2A202603948 | danhhieu123ns@gmail.com | danhhieu204ns | Người viết code (CP1–CP2) |
|   2 | Lê Tuấn Đạt | 2A202603949 | letuandat@vinuni.edu.vn | letuandat131 | Người gắn nhãn 2 kiêm giữ hồ sơ |
|   3 | Vũ Huy Hiệu | 2A202603979 | hieuvippro531@gmail.com | hieunhangia | Người gắn nhãn 1 (CP3) |
|   4 | Nguyễn Bá Quang Huy | 2A202603926 | quanghuynguyenba@gmail.com | quanghuynguyenba | Người kiểm số |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## MaiDanhHieu-2A202603948

### Phần việc phụ trách

- Người viết code (CP1–CP2): Phụ trách viết và chạy code CP1 (A1–A4) và CP2 (B1–B4) trong `src/lab13.py`; cung cấp kết quả cho bảng chi phí.

### Đóng góp cụ thể

- Viết ba hàm A1: số lần chạy kỳ vọng, tỉ lệ thành công và hệ số chi phí mỗi việc thành công.
- Hoàn thiện `mo_hinh()` để tính chi phí token, tool, xem lại, làm lại từ hai file CSV; tính số việc thành công và chi phí mỗi việc thành công (4.472 đ/việc [simulated]).
- Tính kết quả theo bốn loại yêu cầu (A3) và phân bổ chi phí cố định 40 triệu đồng/tháng cho phạm vi `noi_dia` + `hang_nang` ở hai mức khối lượng (A4).
- Điền kết quả A1–A4 vào `report/team/bang_chi_phi.md`; đánh dấu `simulated` cho số sử dụng thời gian giả lập.
- Tính chín kịch bản độ nhạy B1, kịch bản kết hợp và xếp hạng B2; so sánh giới hạn 1–3 lần chạy theo chi phí cả hệ thống B3.
- Tính B4 cho trường hợp xem lại 100% trong phạm vi pilot, với hai giả định thời gian làm lại (11.743 đ – 12.415 đ [simulated]); điền B1–B4 vào bảng chi phí.

### Bằng chứng

- `src/lab13.py`: chạy `python lab13.py` từ thư mục `src/`, ba phép thử A1 in **ĐẠT**.
- `report/team/bang_chi_phi.md`: bảng A1–A4, B1–B4.
- Báo cáo cá nhân: `report/team/2A202603948_MaiDanhHieu.md`.
- Commit `47d45bd`, `6c9cec7`, `b732f3b` (merge qua PR #1).

## LeTuanDat-2A202603949

### Phần việc phụ trách

- Người gắn nhãn 2 kiêm giữ hồ sơ: gắn nhãn độc lập 20 ca lỗi (CP3), giữ và điền `report/team/ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi chạy thử theo 5 nhóm nguyên nhân gốc của Google PAIR (Nhiệm vụ C).
- Bộ nhãn người 2 cho 20 ca, đối chiếu với người gắn nhãn 1 (Vũ Huy Hiệu): 19/20 ca trùng (95%), thống nhất ca 9 là "Do người dùng" (`report/team/bang_loi.md`).
- Xây dựng 5 giải pháp phòng ngừa đo lường được (idempotency key chống hoàn trùng, kiểm tra mẫu ngẫu nhiên tuần, template làm rõ cách tính tiền).
- Điền đầy đủ hồ sơ Gate 2a 1 trang `report/team/ho_so_launch_v0.md` (7 mục, đề xuất Go có điều kiện kèm 4 điều kiện có người phụ trách và ngày kiểm tra cụ thể).
- Cập nhật `TEAM.md` đủ 4 thành viên kèm vai trò, đóng góp và commit chốt.
- Báo cáo cá nhân: `report/team/2A202603949_LeTuanDat.md`.

### Bằng chứng

- File nhãn lỗi: `report/team/bang_loi.md` (cột Nhãn người 2 - Lê Tuấn Đạt, tỉ lệ đồng thuận 95% và bảng khắc phục 5 ca lỗi).
- File hồ sơ tổng hợp Gate 2a: `report/team/ho_so_launch_v0.md`.
- Báo cáo cá nhân: `report/team/2A202603949_LeTuanDat.md`.
- Commit `27f0d0d`, `e61b0c1`, `4774c3c`, `3b4e225`, `0407f8a`, `aeb7a50` (merge qua PR #2, PR #4, PR #6).
- Lưu ý: 5 commit đầu hiện tác giả là "Lê Tuấn Đạt <letuandat@vinuni.edu.vn>". Email này đã được cấu hình trong git trên máy cá nhân và được bổ sung xác minh trên tài khoản GitHub `letuandat131` để gắn lại đóng góp.

## VuHuyHieu-2A202603979

### Phần việc phụ trách

- Người gắn nhãn 1 (CP3): Gắn nhãn độc lập 20 ca lỗi chạy thử theo 5 nhóm nguyên nhân gốc của Google PAIR (Nhiệm vụ C).

### Đóng góp cụ thể

- Độc lập phân loại 20 ca lỗi dựa trên nguyên nhân gốc theo khung chuẩn Google PAIR.
- Đối chiếu nhãn với Lê Tuấn Đạt đạt tỉ lệ đồng thuận cao 19/20 ca (95%).
- Tham gia tranh luận ở ca số 9: Thống nhất chuyển sang "Do người dùng" vì nguyên nhân gốc là khách hàng nhập sai định dạng mã đầu vào.
- Cùng đóng góp hoàn thành bảng 5 giải pháp khắc phục có event đo lường được và chức danh chịu trách nhiệm duy nhất trong `report/team/bang_loi.md`.

### Bằng chứng

- File nhãn lỗi: `report/team/bang_loi.md` (cột Nhãn người 1 - Vũ Huy Hiệu, tỉ lệ đồng thuận 95% và biên bản ca 9).
- Báo cáo cá nhân: `report/team/2A202603979_VuHuyHieu.md`.
- Commit `63c2263`, `2e7df61`.

## NguyenBaQuangHuy-2A202603926

### Phần việc phụ trách

- Người kiểm số, Nhóm trưởng: Tự tính một số liệu để đối chiếu kết quả mô hình, kiểm tra các phép tính trong bảng chi phí và ghi số đã đối chiếu vào `report/team/bang_chi_phi.md`.

### Đóng góp cụ thể

- Kiểm tra các phép thử A1 theo đáp án mẫu: 1,20; 1,25; 1,25.
- Đối chiếu chi phí mỗi việc thành công: 4.373.585 / 978 ≈ 4.472 đ.
- Kiểm tra hoá đơn token và tool bình quân: (245.585 + 84.000) / 1.200 ≈ 274,7 đ/yêu cầu; tỷ số 4.472 / 274,7 ≈ 16,3 lần.
- Kiểm tra phần chi phí làm lại: 2.264.000 / 4.373.585 ≈ 51,8% tổng chi phí.
- Ghi nhận các số dựa trên thời gian xem lại/làm lại giả lập cần mang nhãn `simulated`.
- Quản trị repository nhóm, duyệt và merge các pull request của các thành viên (PR #1, PR #2, PR #4, PR #6).

### Bằng chứng

- `report/team/bang_chi_phi.md`: kết quả A1 và bảng A2.
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`: số tham chiếu để đối chiếu.
- Báo cáo cá nhân: `report/team/2A202603926_NguyenBaQuangHuy.md`.
- Lịch sử quản trị PR và commit `bf47e39` trên repo nhóm.
