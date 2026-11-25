# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51 / 1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp có mở gợi ý trợ lý | Số `request_id` có event `agent_suggestion_shown` chia tổng yêu cầu của nhóm dùng trợ lý | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền phát hiện qua kiểm tra mẫu | Số đơn lệch số tiền trong event `audit_sample_checked` chia tổng số đơn mẫu kiểm tra hằng tuần (100 đơn/tuần) | Không cần tính |

Chỉ số chính trong đợt chạy thử là **82,83%** (không viết "trợ lý đã nâng chỉ số", vì đợt chạy thử không có nhóm đối chứng).

## Danh sách event

Mười event cốt lõi, mọi event đều có `trace_id` để nối với trace của agent:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien_vnd`, `arm`, `staff_id`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy (kể cả lỗi) |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiển thị cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai`, `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id`, `phut_lam_lai`, `ly_do`, `trace_id` | Khi nhân viên xử lý lại xong một ca lỗi |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi bút toán hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `reason`, `tom_tat`, `trace_id` | Khi trợ lý chuyển yêu cầu sang nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `trace_id` | Khi đóng yêu cầu hoàn phí |
| `ticket_reopened` | App khách / CSKH | `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | `so_tien_da_hoan`, `so_tien_dung`, `phien_ban_bang_gia`, `trace_id` | Khi kiểm tra mẫu 100 đơn hằng tuần |

**Kiểm tra chéo:**
- **Chỉ số chính (`dong_trong_24h` & không `mo_lai_trong_7_ngay`):** tính từ `refund_request_created` + `ticket_closed` + `ticket_reopened` theo `trace_id`/`request_id`.
- **Chỉ số dùng (tỉ lệ bỏ qua gợi ý):** tính từ `staff_review_decision` (đếm `sua` + `bo` chia tổng quyết định) và `agent_suggestion_shown`.
- **Chỉ số an toàn (lỗi lọt đến khách):** tính từ `ticket_reopened` trong vòng 7 ngày sau `ticket_closed`.
- **Hai chỉ số tự đề xuất:** lần lượt tính từ `agent_suggestion_shown` ÷ `refund_request_created` (nhóm can thiệp) và `audit_sample_checked`. Mọi chỉ số đều đo được trực tiếp từ danh sách event trên.

## E2 · Rủi ro kinh tế

Số lấy trực tiếp từ bảng độ nhạy (`bang_chi_phi.md`), các số dùng thời gian giả lập đều gắn nhãn `simulated`:

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, lên **6.787 đ/việc** [simulated] | Tỉ lệ ca `lam_lai` theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi `noi_dia` + `hang_nang`) | Thu hẹp về `noi_dia`, rà 20 trace `lam_lai` gần nhất để sửa lỗi | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | Lên **11.743 đ** (0,98×) nếu làm lại 9 phút, hoặc **12.415 đ** (1,03×) nếu làm lại 15,3 phút/ca [simulated] | % yêu cầu được xem lại > 50% ở cuối bước rollout 0,25 hoặc phút xem lại > 4,8 phút | Áp lộ trình giảm xem lại theo bậc khi tỉ lệ `sua + bo` < 15% | Trưởng nhóm CSKH |
| Khối lượng xử lý thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yc/tháng, tăng thành +2.370 đ/việc (tổng 5.784 đ) nếu còn một nửa khối lượng [simulated] | Số việc thành công hằng tuần < 50% kế hoạch tháng | Tạm dừng mở rộng phạm vi, đàm phán lại chi phí cố định | PM trợ lý hoàn phí |
