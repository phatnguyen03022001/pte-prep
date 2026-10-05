# 21 — Highlight Incorrect Words

[Chỉ mục](../README.md) · [Ưu tiên và lịch 7 ngày](../STUDY_PLAN.md)

Đối chiếu Pearson: **2026-10-05**. Các dòng **[S]/[F]** là thông tin chính thức từ nguồn cuối file; chiến thuật, khối lượng luyện và ví dụ là hướng dẫn tự biên soạn cho mục tiêu 40+. Ví dụ minh hoạ không phải đề Pearson hay dự đoán đề thi.

## 1. Làm bài nhanh

1. Skim transcript hiển thị để biết chủ đề.
2. Theo từng từ khi nghe, chọn từ trên màn hình không khớp audio.
3. Không chọn vì thấy grammar lạ nếu audio vẫn nói đúng từ đó.

**Format:** Chọn từ trên màn hình khác audio [F].

## 2. Quy tắc và cách chấm

**Kỹ năng được chấm:** Listening + Reading [S].

**Rubric / điểm raw:** +1/đúng; −1/sai; sàn item 0 [S].

Chọn sai bị −1; sàn item 0 [S]. Cần click từ sai đang hiển thị, không gõ từ đúng thay thế.

Điểm raw/trait trong câu này không quy đổi trực tiếp sang thang 90. Mức 40+ cần xem toàn bài; checklist hoặc nhận xét ChatGPT chỉ hỗ trợ luyện. Cách đọc tên trait được giải thích ở [README gốc](../README.md#cách-đọc-rubric).

## 3. Kiến thức cần có

- Phân biệt âm/từ gần nhau: fifteen/fifty, increase/decrease.
- Theo vị trí text đồng thời nghe; giữ nhịp con trỏ.
- Spelling và hình dạng từ giúp đọc nhanh.
- Hiểu nhiệm vụ so audio–text, khác sửa lỗi ngữ pháp thông thường.

## 4. Chiến thuật luyện 40+

1. Tập trung đối chiếu trực tiếp, không ghi notes dài.
2. Nếu bỏ lỡ một từ, tiếp tục vị trí hiện tại; đừng click đoán hàng loạt.
3. Chọn có căn cứ vì false positives làm mất điểm.
4. Khi chữa, phân loại bỏ sót mismatch và chọn nhầm từ thực ra khớp.

## 5. Ví dụ có giải thích

**Audio script chuẩn tự biên soạn:**

> The class starts at nine in room four.

**Text hiển thị:**

> The class starts at ten in room five.

**Cần chọn:** **ten**, **five** trên màn hình.

Audio nói “nine” và “four”; đó là từ đúng trong audio, không phải mục để click trong text. Chọn đúng hai mismatch được 2 raw; chọn thêm “class” còn 1. Ví dụ chưa có file audio, nên chỉ minh hoạ phép đối chiếu.

## 6. Lỗi, vòng luyện và checklist

### Lỗi thường gặp

- Click từ vì câu nghe kỳ mà không khác audio → đối chiếu thật.
- Mất vị trí và đoán → bám nhịp, bỏ qua điểm đã lỡ.
- Gõ từ thay thế → tập thao tác chọn trên text.

### Luyện và chữa

3 đoạn mới; ghi separately misses và false positives. Ưu tiên giảm chọn nhầm trước khi tăng tốc/audio khó.

Lượt mới dùng đúng timer và điều kiện format; lượt chữa được dừng/tra/nghe lại. Ghi nguyên nhân, làm lại sau nghỉ hoặc hôm sau, rồi kiểm tra bằng câu chưa thấy. Khối lượng cụ thể tùy bài đầu vào; xem STUDY_PLAN.md.

### Tự kiểm tra

- [ ] Đang click từ hiển thị sai?
- [ ] Mỗi click có mismatch nghe được?
- [ ] Không click tràn sau khi mất dấu?

## 7. Media local

Item cần audio chuẩn, displayed transcript có lỗi và key định vị token ổn định. Ghi cả chuẩn và bản sai để tránh answer key mơ hồ khi một từ lặp nhiều lần.

Khi thêm item, dùng `media/<item-id>/metadata.json` và asset cần thiết theo [AGENTS.md](../AGENTS.md#media-item-contract). Chỉ có README không đồng nghĩa đã có media. Luyện qua [Pearson Smart Prep](https://www.pearsonpte.com/pte-academic/preparation/) khi local chưa có item phù hợp. Giữ prompt/đáp án chuẩn trong metadata; chỉ nhập asset có quyền tái sử dụng rõ ràng.

## 8. Nguồn

- **[S]** [Pearson Score Guide](https://www.pearsonpte.com/content/dam/ELL/pte/pearsonpte/pdfs/pte-academic-pdfs/PTE-Academic-Test-Taker-Score-Guide.pdf), trang in 43: kỹ năng, trait và điểm raw. Ưu tiên nguồn này khi website còn ghi chú scoring mâu thuẫn.
- **[F]** [Pearson Listening format](https://www.pearsonpte.com/pte-academic/test-format/listening/): thao tác/timing.
- Kiểm chứng lần cuối: **2026-10-05**. Các lời giải/ví dụ trong file là nội dung tự biên soạn; không gán điểm chính thức cho response mẫu.
