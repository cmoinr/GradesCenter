-- SELECT subjects.name, faculty.field, subjects.semester
-- FROM subjects
-- JOIN faculty ON subjects.id_faculty = faculty.id
-- JOIN teaching ON subjects.id = teaching.id_subject
-- JOIN teachers ON teaching.id_teacher = teachers.id
-- WHERE teaching.id_teacher = 29959129

-- SELECT id, names, surnames, semester FROM students
-- JOIN studying ON students.id = studying.id_student
-- WHERE studying.id_subject = ?

SELECT students.id, students.names, students.surnames, grades.grade
FROM students
JOIN studying ON students.id = studying.id_student
JOIN grades ON studying.id_subject = grades.id_subject
WHERE studying.id_subject = 'MA101'