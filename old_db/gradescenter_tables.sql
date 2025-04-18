CREATE TABLE students (
    id INTEGER NOT NULL,
    names TEXT NOT NULL,
    surnames TEXT NOT NULL,
    semester INTEGER,
    credits INTEGER,
    hash TEXT NOT NULL,
    id_faculty TEXT NOT NULL,
    PRIMARY KEY(id)
    FOREIGN KEY(id_faculty) REFERENCES faculty(id)
);

CREATE TABLE faculty (
    id TEXT NOT NULL,
    field TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE teachers (
    id INTEGER NOT NULL,
    names TEXT NOT NULL,
    surnames TEXT NOT NULL,
    hash TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE subjects (
    id TEXT NOT NULL,
    name TEXT NOT NULL,
    id_faculty TEXT NOT NULL,
    semester INTEGER NOT NULL,
    credits INTEGER NOT NULL,
    PRIMARY KEY(id)
    FOREIGN KEY(id_faculty) REFERENCES faculty(id)
);

CREATE TABLE grades (
    id_student INTEGER NOT NULL,
    id_subject TEXT NOT NULL,
    grade INTEGER NOT NULL,
    FOREIGN KEY(id_student) REFERENCES students(id)
    FOREIGN KEY(id_subject) REFERENCES subjects(id)
);

CREATE TABLE teaching (
    id_teacher INTEGER NOT NULL,
    id_subject TEXT NOT NULL,
    FOREIGN KEY(id_teacher) REFERENCES teachers(id)
    FOREIGN KEY(id_subject) REFERENCES subjects(id)
);

CREATE TABLE studying (
    id_student INTEGER NOT NULL,
    id_subject TEXT NOT NULL,
    FOREIGN KEY(id_student) REFERENCES students(id)
    FOREIGN KEY(id_subject) REFERENCES subjects(id)
);