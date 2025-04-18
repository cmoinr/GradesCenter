CREATE TABLE IF NOT EXISTS students (
    id VARCHAR(16),
    names VARCHAR(32) NOT NULL,
    last_names VARCHAR(32) NOT NULL,
    pw VARCHAR(255) NOT NULL,
    department_id VARCHAR(16) NOT NULL,
    email VARCHAR(64),
    phone VARCHAR(32),
    PRIMARY KEY(id),
    FOREIGN KEY(department_id) REFERENCES departments(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS grades (
    id INTEGER,
    student_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    section_id INTEGER NOT NULL,
    grade INTEGER NOT NULL,
    date DATE DEFAULT CURRENT_DATE,
    PRIMARY KEY(id),
    FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY(teacher_id) REFERENCES teachers(id) ON DELETE CASCADE,
    FOREIGN KEY(section_id) REFERENCES sections(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS subjects (
    id VARCHAR(16),
    name TEXT NOT NULL,
    department_id VARCHAR(16) NOT NULL,
    semester INTEGER NOT NULL,
    credits INTEGER NOT NULL,
    sections INTEGER NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(department_id) REFERENCES departments(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS sections (
    id INTEGER,
    subject_id INTEGER NOT NULL,
    section_number INTEGER NOT NULL,
    period TEXT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS teachers (
    id VARCHAR(16),
    names VARCHAR(32) NOT NULL,
    last_names VARCHAR(32) NOT NULL,
    pw VARCHAR(255) NOT NULL,
    email VARCHAR(64),
    phone VARCHAR(32),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS departments (
    id VARCHAR(16),
    field TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS teaching (
    teacher_id VARCHAR(16) NOT NULL,
    section_id VARCHAR(16) NOT NULL,
    PRIMARY KEY(teacher_id, section_id),
    FOREIGN KEY(teacher_id) REFERENCES teachers(id) ON DELETE CASCADE,
    FOREIGN KEY(section_id) REFERENCES sections(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS studying (
    student_id VARCHAR(16) NOT NULL,
    section_id VARCHAR(16) NOT NULL,
    PRIMARY KEY(student_id, section_id),
    FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY(section_id) REFERENCES sections(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS strategies (
    id INTEGER,
    type TEXT NOT NULL,
    topic TEXT,
    percentage INTEGER NOT NULL,
    section_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    date DATE DEFAULT CURRENT_DATE,
    PRIMARY KEY(id),
    FOREIGN KEY(teacher_id) REFERENCES teachers(id) ON DELETE CASCADE,
    FOREIGN KEY(section_id) REFERENCES sections(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS evaluated (
    strategy_id INTEGER NOT NULL,
    student_id VARCHAR(16) NOT NULL,
    grade INTEGER,
    PRIMARY KEY(strategy_id, student_id),
    FOREIGN KEY(strategy_id) REFERENCES strategies(id) ON DELETE CASCADE,
    FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE
);