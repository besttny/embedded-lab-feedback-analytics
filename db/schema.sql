-- Drop table if exists (for testing or reloading)
DROP TABLE IF EXISTS feedback;

-- Create main table
CREATE TABLE feedback (
    anon_id     VARCHAR(20) PRIMARY KEY,           -- anonymized unique ID
    section     VARCHAR(50) NOT NULL,              -- main topic section (Timing, Document, Other, etc.)
    lab_no      VARCHAR(20),                       -- lab numbers (e.g., "1", "1,2,3", or null)
    category    VARCHAR(50),                       -- category of comment (e.g., time, document, ta, equipment)
    comment     TEXT NOT NULL,                     -- feedback content
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- insertion timestamp
);

CREATE INDEX idx_feedback_section  ON feedback(section);
CREATE INDEX idx_feedback_category ON feedback(category);
