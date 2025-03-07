CREATE TABLE students (
    id VARCHAR(16),
    names VARCHAR(32) NOT NULL,
    last_names VARCHAR(32) NOT NULL,
    pw VARCHAR(255) NOT NULL,
    department_id VARCHAR(16) NOT NULL,
    email VARCHAR(64),
    phone VARCHAR(32),
    PRIMARY KEY(id),
    FOREIGN KEY(department_id) REFERENCES departments(id)
);

CREATE TABLE grades (
    id INTEGER,
    student_id INTEGER NOT NULL,
    subject_id VARCHAR(16) NOT NULL,
    teacher_id INTEGER NOT NULL,
    grade INTEGER NOT NULL,
    date DATE DEFAULT CURRENT_DATE,
    PRIMARY KEY(id),
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
);

CREATE TABLE subjects (
    id VARCHAR(16),
    name TEXT NOT NULL,
    department_id VARCHAR(16) NOT NULL,
    semester INTEGER NOT NULL,
    credits INTEGER NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(department_id) REFERENCES departments(id)
);

CREATE TABLE teachers (
    id VARCHAR(16),
    names VARCHAR(32) NOT NULL,
    last_names VARCHAR(32) NOT NULL,
    pw VARCHAR(255) NOT NULL,
    email VARCHAR(64),
    phone VARCHAR(32),
    PRIMARY KEY(id)
);

CREATE TABLE departments (
    id VARCHAR(16),
    field TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE teaching (
    teacher_id VARCHAR(16) NOT NULL,
    subject_id VARCHAR(16) NOT NULL,
    PRIMARY KEY(teacher_id, subject_id),
    FOREIGN KEY(teacher_id) REFERENCES teachers(id),
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
);

CREATE TABLE studying (
    student_id VARCHAR(16) NOT NULL,
    subject_id VARCHAR(16) NOT NULL,
    PRIMARY KEY(student_id, subject_id),
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
);

CREATE TABLE strategies (
    id INTEGER,
    type TEXT NOT NULL,
    topic TEXT,
    percentage INTEGER NOT NULL,
    subject_id VARCHAR(16) NOT NULL,
    teacher_id INTEGER NOT NULL,
    date DATE DEFAULT CURRENT_DATE,
    PRIMARY KEY(id),
    FOREIGN KEY(teacher_id) REFERENCES teachers(id),
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
);

CREATE TABLE evaluated (
    strategy_id INTEGER NOT NULL,
    student_id VARCHAR(16) NOT NULL,
    PRIMARY KEY(strategy_id, student_id),
    FOREIGN KEY(strategy_id) REFERENCES strategies(id),
    FOREIGN KEY(student_id) REFERENCES students(id)
);