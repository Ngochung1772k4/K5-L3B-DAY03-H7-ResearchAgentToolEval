# Báo cáo cá nhân — Phạm Minh Đức (2A202603758)

## 1. Thông tin thành viên

- Họ tên: Phạm Minh Đức
- MSSV: 2A202603758
- Email: 26ai.ducpm@vinuni.edu.vn

## 2. Phần việc phụ trách

- CP4–CP5: kiểm chứng lưu transcript của luồng chat nhiều lượt và khả năng ghi nhận lỗi provider/tool.

## 3. Đóng góp cụ thể

- Review luồng Streamlit/chat và phát hiện `write_transcript()` ghi trực tiếp vào file đích, có thể để lại JSON không hoàn chỉnh nếu bị ngắt khi lưu.
- Cập nhật `write_transcript()` theo cơ chế ghi file tạm rồi thay thế file đích, giúp transcript xuất/tải chỉ xuất hiện dưới dạng JSON hoàn chỉnh.
- Viết hai regression test offline cho transcript của chat CLI dùng chung với UI: một response thành công và một lỗi provider. Cả hai test xác nhận turn được lưu với trạng thái và nội dung lỗi/kết quả đúng; đồng thời không còn file tạm sau khi lưu.

## 4. Bằng chứng

- Files: `starter_v0/chat.py`, `starter_v0/tests/test_chat_transcripts.py`, `starter_v0/transcripts/`.
- Test: chạy `pytest -q tests/test_chat_transcripts.py` từ `starter_v0/` (offline, fake provider, không dùng API key).
- Kết quả kiểm tra tại máy: `py -3 -m py_compile chat.py tests/test_chat_transcripts.py` và `git diff --check` pass. `pytest` chưa chạy được vì Python 3.15 của máy chưa có module `pytest`; không ghi nhận kết quả pass giả.
- AI/công cụ đã dùng: trợ lý AI hỗ trợ rà soát mã và soạn nháp; hai regression test dùng fake provider để không gọi API/key khi môi trường pytest sẵn sàng.

## 5. Tự đánh giá

Đã bổ sung kiểm chứng tự động cho hai tình huống quan trọng của CP4–CP5 và tăng độ bền khi lưu transcript. Không nhận phần triển khai UI/transcript ban đầu của thành viên khác.
