-- SELECT subjects.name, faculty.field, subjects.semester
-- FROM subjects
-- JOIN faculty ON subjects.id_faculty = faculty.id
-- JOIN teaching ON subjects.id = teaching.id_subject
-- JOIN teachers ON teaching.id_teacher = teachers.id
-- WHERE teaching.id_teacher = 29959129

-- SELECT id, names, surnames, semester FROM students
-- JOIN studying ON students.id = studying.id_student
-- WHERE studying.id_subject = ?

-- SELECT students.id, students.names, students.surnames, grades.grade
-- FROM students
-- JOIN studying ON students.id = studying.id_student
-- JOIN grades ON studying.id_subject = grades.id_subject
-- WHERE studying.id_subject = 'MA101'

-- SELECT subjects.name, subjects.semester, subjects.credits, grades.grade, teachers.names, teachers.surnames
-- FROM subjects
-- JOIN grades ON subjects.id = grades.id_subject
-- JOIN studying ON grades.id_student = studying.id_student
-- JOIN teaching ON subjects.id = teaching.id_subject
-- JOIN teachers ON teaching.id_teacher = teachers.id
-- WHERE studying.id_student = 25000100

-- SELECT subjects.name, subjects.semester, subjects.credits, grades.grade, teachers.names, teachers.surnames
-- FROM studying
-- JOIN students ON studying.id_student = students.id
-- JOIN grades ON studying.id_subject = grades.id_subject
-- JOIN subjects ON studying.id_subject = subjects.id
-- JOIN teaching ON studying.id_subject = teaching.id_subject
-- JOIN teachers ON teaching.id_teacher = teachers.id
-- WHERE studying.id_student = 25000100

-- DELETE FROM teaching
-- WHERE id_teacher = 23500120;