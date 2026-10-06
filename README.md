# PTE Prep

Kho tài liệu ôn tập và media luyện **PTE Academic** có thể tái sử dụng và mở rộng liên tục. Lộ trình học cấp tốc 7 ngày (hướng tới **overall ≥40**) được cung cấp như một chiến lược tùy chọn, nhưng workspace này không giới hạn thời gian học, khối lượng câu hỏi hay quy mô dữ liệu.

## Bắt đầu

1. Đọc [STUDY_PLAN.md](./STUDY_PLAN.md): làm bài đầu vào, xem ưu tiên, rồi theo lịch từng ngày.
2. Mở README của dạng bài bên dưới: đọc cách làm nhanh, scoring, kiến thức cần có và ví dụ, rồi luyện theo plan.
3. Xem [SOURCES.md](./SOURCES.md) trước khi dùng hoặc thêm bất kỳ question bank/media nào. Chỉ dùng canonical media đã qua source gate; nếu chưa có thì luyện qua nguồn chính thức hoặc `private-materials/` local-only.
4. Ghi lỗi, chữa lỗi và làm lại hôm sau. Không cần đợi kho dữ liệu đầy mới bắt đầu.

Hướng dẫn từng dạng và media có vòng kiểm tra riêng. Có README không đồng nghĩa đã có audio/image/item để luyện; dùng nguồn chính thức khi local chưa có asset phù hợp.

## Bốn tài liệu gốc

| File | Chứa gì |
| --- | --- |
| [AGENTS.md](./AGENTS.md) | Quy tắc biên soạn, cấu trúc item, quality gate và completion gate |
| [SOURCES.md](./SOURCES.md) | Danh sách nguồn được phép dùng, nguồn personal-only và nội dung bị cấm |
| README.md | Điểm bắt đầu và chỉ mục folder |
| [STUDY_PLAN.md](./STUDY_PLAN.md) | Mục tiêu, ưu tiên 22 dạng, lộ trình học tùy chọn (vd: 7 ngày), tự kiểm tra và điều chỉnh |

## Tài liệu cá nhân tải từ bên thứ ba

`private-materials/` là vùng **chỉ dùng local để học cá nhân** cho prediction PDF, question bank, ảnh, audio hoặc tài liệu tương tự được tải hợp lệ từ nhà cung cấp. Nội dung tải xuống trong vùng này bị `.gitignore` và không được push lên GitHub; chỉ file policy `private-materials/README.md` được theo dõi.

Dùng các tài liệu này để tăng độ phong phú của prompt và luyện phản xạ, nhưng không coi nhãn "prediction/high-frequency" hay sample answer của bên thứ ba là scoring authority của Pearson. Không sao chép chúng vào dataset reusable hoặc app nếu chưa có quyền tái sử dụng rõ ràng. Nguồn personal-study được khóa trong [SOURCES.md](./SOURCES.md).

## Trạng thái canonical dataset

Canonical `media/` **không được phép chứa item tự bịa để lấp quota**. LLM-generated question, synthetic TTS, AI image, placeholder chart và item chưa human-review đều bị cấm. Nếu chưa có item đạt source gate thì để trống; mục tiêu 297 không phải lý do để tạo dữ liệu giả.

## Chỉ mục dạng bài

Folder giữ thứ tự dạng bài Pearson công bố. Mức ưu tiên luyện được ghi riêng trong study plan. Personal Introduction không tính điểm được luyện trong plan, không cần folder riêng.

| Số | Phần | Dạng / folder |
| --- | --- | --- |
| 01 | Speaking & Writing | [Read Aloud](./01-read-aloud/README.md) |
| 02 | Speaking & Writing | [Repeat Sentence](./02-repeat-sentence/README.md) |
| 03 | Speaking & Writing | [Describe Image](./03-describe-image/README.md) |
| 04 | Speaking & Writing | [Retell Lecture](./04-retell-lecture/README.md) |
| 05 | Speaking & Writing | [Answer Short Question](./05-answer-short-question/README.md) |
| 06 | Speaking & Writing | [Summarize Group Discussion](./06-summarize-group-discussion/README.md) |
| 07 | Speaking & Writing | [Respond to a Situation](./07-respond-to-a-situation/README.md) |
| 08 | Speaking & Writing | [Summarize Written Text](./08-summarize-written-text/README.md) |
| 09 | Speaking & Writing | [Write Essay](./09-write-essay/README.md) |
| 10 | Reading | [Fill in the Blanks (Dropdown)](./10-reading-fill-in-the-blanks-dropdown/README.md) |
| 11 | Reading | [Multiple Choice, Multiple Answers](./11-reading-multiple-choice-multiple-answers/README.md) |
| 12 | Reading | [Reorder Paragraph](./12-reorder-paragraph/README.md) |
| 13 | Reading | [Fill in the Blanks (Drag and Drop)](./13-reading-fill-in-the-blanks-drag-and-drop/README.md) |
| 14 | Reading | [Multiple Choice, Single Answer](./14-reading-multiple-choice-single-answer/README.md) |
| 15 | Listening | [Summarize Spoken Text](./15-summarize-spoken-text/README.md) |
| 16 | Listening | [Multiple Choice, Multiple Answers](./16-listening-multiple-choice-multiple-answers/README.md) |
| 17 | Listening | [Fill in the Blanks (Type In)](./17-listening-fill-in-the-blanks-type-in/README.md) |
| 18 | Listening | [Highlight Correct Summary](./18-highlight-correct-summary/README.md) |
| 19 | Listening | [Multiple Choice, Single Answer](./19-listening-multiple-choice-single-answer/README.md) |
| 20 | Listening | [Select Missing Word](./20-select-missing-word/README.md) |
| 21 | Listening | [Highlight Incorrect Words](./21-highlight-incorrect-words/README.md) |
| 22 | Listening | [Write from Dictation](./22-write-from-dictation/README.md) |

## Cấu trúc nội dung

Mỗi folder dạng bài luôn có hướng dẫn `README.md`; chỉ tạo `media/<item-id>/` khi item đạt source/review gate. Dạng chỉ dùng văn bản không cần audio. Hợp đồng chi tiết nằm trong [AGENTS.md](./AGENTS.md), còn source allowlist và promotion rule nằm trong [SOURCES.md](./SOURCES.md).

Tài liệu giải thích bằng tiếng Việt; câu hỏi, đáp án mẫu và tên dạng giữ tiếng Anh. Một item tốt phải sát định dạng, có đáp án/hướng dẫn đánh giá đúng và có nguồn sử dụng rõ ràng.

## Cách đọc rubric

- **Content:** nội dung câu trả lời so với prompt; **Form:** yêu cầu hình thức.
- **Pronunciation:** phát âm; **Oral Fluency:** nhịp nói.
- **Grammar / Vocabulary / Spelling:** ngữ pháp / từ vựng / chính tả.
- **Development, Structure and Coherence:** triển khai, tổ chức và liên kết ý.
- **General Linguistic Range:** phạm vi ngôn ngữ diễn đạt.

README từng dạng ghi raw points/trait và cách chữa; các giá trị này không tự quy thành điểm 90. Ví dụ tự biên soạn dùng để hiểu cách làm. Với câu nói, cần nghe bản thu mới nhận xét được phát âm/fluency; transcript không đủ.

## Nguồn chính thức

Đối chiếu ngày **2026-10-05**:

- [Pearson Score Guide](https://www.pearsonpte.com/content/dam/ELL/pte/pearsonpte/pdfs/pte-academic-pdfs/PTE-Academic-Test-Taker-Score-Guide.pdf): nguồn chính cho kỹ năng được chấm và tiêu chí chấm.
- [Speaking & Writing](https://www.pearsonpte.com/pte-academic/test-format/speaking-writing/), [Reading](https://www.pearsonpte.com/pte-academic/test-format/reading/), [Listening](https://www.pearsonpte.com/pte-academic/test-format/listening/): định dạng và thao tác từng dạng.
- [Pearson Preparation / Smart Prep](https://www.pearsonpte.com/pte-academic/preparation/): tài liệu luyện miễn phí và trả phí.

Smart Prep có tài liệu hướng dẫn luyện miễn phí. Scored Practice Test là lựa chọn trả phí để kiểm tra mức sẵn sàng bằng scoring engine của Pearson. Plan vẫn dùng được khi chỉ chọn nguồn miễn phí; lúc đó chưa có điểm Pearson để xác nhận mục tiêu.

Media công khai hoặc miễn phí chưa chắc được phép sao chép vào kho. Dùng tài liệu Pearson qua giao diện được phép; chỉ nhập asset có quyền tái sử dụng được ghi rõ. Xem chính sách trong AGENTS.md.
