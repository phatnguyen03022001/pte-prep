# 12 — Reorder Paragraph

[Chỉ mục](../README.md) · [Ưu tiên và lộ trình học](../STUDY_PLAN.md)

Đối chiếu Pearson: **2026-10-05**. Các dòng **[S]/[F]** là thông tin chính thức từ nguồn cuối file; chiến thuật, khối lượng luyện và ví dụ là hướng dẫn tự biên soạn cho mục tiêu 40+. Ví dụ minh hoạ không phải đề Pearson hay dự đoán đề thi.

## 1. Làm bài nhanh

1. Đọc từng textbox và tìm câu mở chủ đề.
2. Ghép các cặp có quan hệ chắc.
3. Kiểm tra dòng ý của toàn đoạn.

**Format:** Sắp xếp textbox; timer chung của Reading [F].

## 2. Quy tắc và cách chấm

**Kỹ năng được chấm:** Reading [S].

**Rubric / điểm raw:** +1/cặp liền kề đúng [S].

Điểm tính theo cặp đúng liền kề, không theo số textbox ở đúng vị trí [S]. Đặt câu mở đúng chưa tự tạo nhiều điểm nếu các cặp sau sai.

Điểm raw/trait trong câu này không quy đổi trực tiếp sang thang 90. Mức 40+ cần xem toàn bài; checklist hoặc nhận xét ChatGPT chỉ hỗ trợ luyện. Cách đọc tên trait được giải thích ở [README gốc](../README.md#cách-đọc-rubric).

## 3. Kiến thức cần có

- Đại từ tham chiếu: this method, they, these results cần antecedent thích hợp.
- Trình tự: first/then/finally; vấn đề → phương pháp → kết quả.
- Thông tin cũ/mới: câu giới thiệu đối tượng thường trước câu dùng the/this để nhắc lại.
- Quan hệ nguyên nhân, đối lập và ví dụ; không coi một dấu hiệu là luật tuyệt đối.

## 4. Chiến thuật luyện 40+

1. Tìm câu có thể tự đứng làm mở đầu, nhưng vẫn đọc các câu khác để kiểm chứng.
2. Giữ một cặp chắc làm khối, rồi tìm câu đứng trước/sau khối.
3. Đọc thử toàn bộ thứ tự; nếu câu có “then” mà chưa có bước trước, xem lại.
4. Mốc luyện khoảng 1–2 phút/item; dừng đảo vô hạn khi đã hết ngân sách phần.

## 5. Ví dụ có giải thích

**Textbox tự biên soạn:**

- A. The researchers then compared the scores of the two groups.
- B. Researchers wanted to know whether background music affected memory.
- C. To investigate this, they asked one group to study with music and another to study in silence.
- D. The results showed that the group studying in silence remembered more words.

**Thứ tự:** B → C → A → D.

B nêu câu hỏi; “this” trong C trỏ về câu hỏi đó. A là bước so sánh sau khi có hai nhóm; D là kết quả. Ba cặp đúng là B–C, C–A, A–D. Thứ tự B–C–D–A chỉ có cặp B–C đúng, nên 1 raw point trong ví dụ.

## 6. Lỗi, vòng luyện và checklist

### Lỗi thường gặp

- Sắp theo keyword lặp mà bỏ quan hệ → giải thích mỗi cặp.
- Coi mọi câu có the không thể mở đầu → kiểm tra nghĩa, không dùng mẹo tuyệt đối.
- Đổi một câu phá cặp đang chắc → di chuyển cả khối.

### Luyện và chữa

3 đoạn mới; ghi lý do của từng cặp. Hôm sau xáo lại đoạn và thử một đoạn mới cùng kiểu logic.

Lượt mới dùng đúng timer và điều kiện format; lượt chữa được dừng/tra/nghe lại. Ghi nguyên nhân, làm lại sau nghỉ hoặc hôm sau, rồi kiểm tra bằng câu chưa thấy. Khối lượng cụ thể tùy bài đầu vào; xem STUDY_PLAN.md.

### Tự kiểm tra

- [ ] Đại từ có đối tượng để trỏ về?
- [ ] Các bước/kết quả đúng thứ tự?
- [ ] Có kiểm tra từng cặp thay vì chỉ câu đầu?

## 7. Media local

Item cần textbox IDs ổn định và thứ tự chuẩn; đáp án lưu bằng IDs, không phụ thuộc vị trí hiển thị ngẫu nhiên.

Khi thêm item, dùng `media/<item-id>/metadata.json` và asset cần thiết theo [AGENTS.md](../AGENTS.md#media-item-contract). Chỉ có README không đồng nghĩa đã có media. Luyện qua [Pearson Smart Prep](https://www.pearsonpte.com/pte-academic/preparation/) khi local chưa có item phù hợp. Giữ prompt/đáp án chuẩn trong metadata; chỉ nhập asset có quyền tái sử dụng rõ ràng.

## 8. Nguồn

- **[S]** [Pearson Score Guide](https://www.pearsonpte.com/content/dam/ELL/pte/pearsonpte/pdfs/pte-academic-pdfs/PTE-Academic-Test-Taker-Score-Guide.pdf), trang in 39: kỹ năng, trait và điểm raw. Ưu tiên nguồn này khi website còn ghi chú scoring mâu thuẫn.
- **[F]** [Pearson Reading format](https://www.pearsonpte.com/pte-academic/test-format/reading/): thao tác/timing.
- Kiểm chứng lần cuối: **2026-10-05**. Các lời giải/ví dụ trong file là nội dung tự biên soạn; không gán điểm chính thức cho response mẫu.
