# Báo cáo cá nhân — Bùi Ngọc Hùng (2A202603770)

## 1. Thông tin thành viên

- Họ tên: Bùi Ngọc Hùng
- MSSV: 2A202603770
- Email: Chưa điền

## 2. Phần việc phụ trách

- CP1–CP2: xây dựng baseline, tối ưu prompt và mô tả tool; chạy các vòng đánh giá v0–v3.
- Bonus: thực hiện các thử nghiệm model local, bổ sung tool xử lý nguồn, Telegram sau xác nhận và kiểm thử hồi quy theo phân công nhóm.

## 3. Đóng góp cụ thể

- Ghi nhận baseline v0 và cập nhật `system_prompt.md` qua các phiên bản; phân tích lỗi và điều chỉnh mô tả tool trong `tools.yaml` cho v1–v3.
- Chạy và so sánh các eval v0–v3 bằng OpenRouter; kết quả tăng từ 14/20 (0.70) ở v0 lên 19/20 (0.95) ở v3.
- Thử nghiệm Qwen2.5:7b và Qwen2.5:3b với Ollama, thực hiện các vòng tối ưu local v4/v5 và kiểm tra chéo artifact local trên OpenRouter.
- Tham gia hoàn thiện các tool bonus xử lý nguồn, eval mở rộng, gửi Telegram chỉ sau xác nhận, và các unit test offline.

## 4. Bằng chứng

- `starter_v0/artifacts/system_prompt.md`, `starter_v0/artifacts/tools.yaml`, `starter_v0/artifacts/version_log.csv`.
- Run v0–v3: `starter_v0/runs/v0_B_base_openrouter_20261110T174808932044.json` đến `starter_v0/runs/v3_B_base_openrouter_20261110T180412507897.json`.
- Bonus local: các run `v3-qwen7b`, `v3-qwen3b`, `v4-local-qwen7b`, `v5-local-qwen7b` và `v5-local-on-cloud` trong `starter_v0/runs/`.
- Bonus tools/tests: `starter_v0/data/eval_bonus_tools.json`, `starter_v0/runs/bonus-tools-v1_B_extension_openrouter_20261111T094527513436.json`, `starter_v0/runs/pytest_bonus_20261111.txt`.
- Telegram: `starter_v0/transcripts/bonus-telegram_openrouter_20261111T101621746672.transcript.json` ghi nhận hỏi xác nhận, người dùng đồng ý, rồi gửi thành công.
- Commit CP1–CP2 hiện có trên lịch sử nhánh: `2da7e6e`.
- AI/công cụ: dùng agent hỗ trợ đọc hướng dẫn, phân tích lỗi và soạn chỉnh sửa; tự đối chiếu run JSON, hash artifact, transcript và kết quả pytest đã lưu.

## 5. Tự đánh giá

Các vòng prompt và tool declaration cải thiện độ chính xác trên bộ base từ 0.70 lên 0.95. Kết quả local thấp hơn cloud; thử nghiệm cũng cho thấy các ví dụ bổ sung cho model local chưa cải thiện v5. Lỗi ranh giới R12 còn tồn tại ở run v3 và được ghi rõ trong báo cáo nhóm. Cần bổ sung email và commit cuối sau khi chốt các thay đổi nộp bài.
