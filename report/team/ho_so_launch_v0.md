# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: HuuDuyen · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc (gấp 16,3× hoá đơn token+tool chia cho 1.200 yc là 274,7 đ); phạm vi `noi_dia` + `hang_nang` gồm cố định 40 tr/tháng là 4.599 đ/việc ở 45.000 yc/tháng (5.784 đ ở 1/2 khối lượng) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%, lên 6.787 đ); 2. Tỉ lệ xem lại (+40,7%, lên 6.292 đ); 3. Lương nhân viên (+23,1%, lên 5.506 đ) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | `noi_dia` 2.696 đ (0,22×) & `hang_nang` 8.221 đ (0,69×) rẻ hơn 12.000 đ; `quoc_te` 22.515 đ (1,88×) lỗ nặng; xem lại 100% lên 11.743–12.415 đ (0,98×–1,03×) [simulated] | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính: 82,83% (994/1.200 đóng 24h & không mở lại 7 ngày); Dùng: 27,12% (48/177 bỏ qua gợi ý); An toàn: 4,25% (51/1.200 mở lại 7 ngày) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi đạt 5 nhóm chuẩn Google PAIR, đồng thuận 95% (19/20); 5 giải pháp đo lường được (idempotency, đối soát sổ cái, kiểm mẫu tuần, template giải thích) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên (20 dùng trợ lý vs 20 đối chứng); MDE 6 điểm (n=859/nhóm, m≥299 yc/người); 3 luật dừng an toàn/chi phí/sử dụng có rollback 30 phút | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Số ca làm lại tăng gấp đôi làm chi phí tăng +51,8% lên 6.787 đ; xem lại 100% kéo dài làm chi phí lên 11.743–12.415 đ (có thể đắt hơn 12.000 đ) [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện

- **Điều kiện 1:** Kỹ sư trưởng agent triển khai khoá chống trùng (idempotency key) và đối soát sổ cái tự động (khắc phục ca 7, 20) trước ngày bắt đầu pilot (2026-12-01).
- **Điều kiện 2:** Giám đốc vận hành ký duyệt chấp nhận MDE 6 điểm (power 0,64 ở mức 5 điểm) do giới hạn 40 nhân viên CSKH.
- **Điều kiện 3:** Bật đủ logging 10 event có `trace_id`; sau tuần 1 thay số phút giả lập bằng dữ liệu đo thời gian thực tế.
- **Điều kiện 4:** Trưởng nhóm CSKH có kế hoạch giảm tỉ lệ xem lại theo bậc (từ 50% xuống 20% khi tỉ lệ sửa/bỏ < 15%), tránh rủi ro xem lại 100% gây lỗ (B4).
