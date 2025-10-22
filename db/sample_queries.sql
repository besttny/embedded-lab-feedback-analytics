-- Sample Queries for Embedded Lab Feedback Analytics
-- ===================================================

-- ดูข้อมูลตัวอย่าง
SELECT * FROM feedback LIMIT 10;

-- นับจำนวน feedback ทั้งหมด
SELECT COUNT(*) AS total_feedbacks FROM feedback;

-- แยกตาม section (Document / Timing / Other)
SELECT section, COUNT(*) AS num_feedbacks
FROM feedback
GROUP BY section
ORDER BY num_feedbacks DESC;

-- แยกตาม category เช่น time, document, teaching, ta, ...
SELECT category, COUNT(*) AS num_feedbacks
FROM feedback
GROUP BY category
ORDER BY num_feedbacks DESC;

-- นับจำนวน comment ต่อ lab_no (ถ้ามี)
SELECT lab_no, COUNT(*) AS num_feedbacks
FROM feedback
WHERE lab_no IS NOT NULL
GROUP BY lab_no
ORDER BY lab_no;

-- ตัวอย่าง filter: ความเห็นที่เกี่ยวกับ TA
SELECT anon_id, comment
FROM feedback
WHERE category = 'ta' OR comment ILIKE '%TA%';

-- ความเห็นที่พูดถึงเวลา / deadline
SELECT anon_id, comment
FROM feedback
WHERE category = 'time' OR comment ILIKE '%เวลา%';

-- รวมผลแบบ pivot: จำนวน feedback แยกตาม section และ category
SELECT section, category, COUNT(*) AS count
FROM feedback
GROUP BY section, category
ORDER BY section, count DESC;

-- หา comment ที่ยาวที่สุด (ตรวจดูความหลากหลายของ feedback)
SELECT anon_id, LENGTH(comment) AS length, comment
FROM feedback
ORDER BY length DESC
LIMIT 5;

-- ดูจำนวนคอมเมนต์ที่มีคำว่า "ไม่" (เชิงลบ)
SELECT COUNT(*) AS negative_feedbacks
FROM feedback
WHERE comment LIKE '%ไม่%';
