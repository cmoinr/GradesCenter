-- SELECT s.id, s.name, d.field, s.semester, COUNT(studying.student_id) AS 'enrolled'
-- FROM subjects s
-- JOIN departments d ON s.department_id = d.id
-- JOIN teaching t ON s.id = t.subject_id
-- JOIN teachers ts ON t.teacher_id = ts.id
-- JOIN studying ON s.id = studying.subject_id
-- WHERE t.teacher_id = ?
-- GROUP BY s.id;

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

-- INSERT INTO grades(student_id, subject_id, teacher_id, grade)
-- VALUES ('22020202', 'SE70', '4857673', 7);

-- SELECT s.id, s.names, s.last_names, grades.grade
-- FROM students s
-- JOIN studying ON s.id = studying.student_id
-- JOIN grades ON studying.subject_id = grades.subject_id
-- WHERE studying.subject_id = 'MA001';

-- SELECT subjects.name, subjects.semester, subjects.credits, grades.grade, teachers.names, teachers.last_names
-- FROM studying
-- JOIN subjects ON studying.subject_id = subjects.id
-- JOIN grades ON studying.student_id = grades.student_id AND studying.subject_id = grades.subject_id
-- JOIN teaching ON studying.subject_id = teaching.subject_id
-- JOIN teachers ON teaching.teacher_id = teachers.id
-- WHERE studying.student_id = ?

-- ALTER TABLE evaluated
-- ADD COLUMN grade INTEGER;

-- ALTER TABLE studying, teaching
-- ADD COLUMN section TEXT;

-- INSERT INTO evaluated (strategy_id, student_id)
-- SELECT 5, students.id
-- FROM studying
-- JOIN grades ON studying.student_id = grades.student_id AND studying.subject_id = grades.subject_id
-- JOIN students ON studying.student_id = students.id
-- WHERE studying.subject_id = 'LM002'

-- SELECT evaluated.student_id, students.names, students.last_names, evaluated.grade
-- FROM evaluated
-- JOIN students ON evaluated.student_id = students.id
-- WHERE evaluated.strategy_id = ?

-- DELETE FROM studying;

-- SELECT s.id, s.name, d.field, s.semester, COUNT(studying.student_id) AS 'enrolled'
-- FROM subjects s
-- JOIN departments d ON s.department_id = d.id
-- JOIN teaching t ON s.id = t.subject_id AND s.id = t.section
-- JOIN teachers ts ON t.teacher_id = ts.id
-- JOIN studying ON s.id = studying.subject_id
-- WHERE t.teacher_id = '23500120'
-- GROUP BY s.id

-- SELECT
--     sections.period,
--     subjects.id, 
--     subjects.name, 
--     sections.section_number, 
--     departments.field, 
--     subjects.semester, 
--     COUNT(studying.student_id) AS 'enrolled'
-- FROM teaching
-- JOIN sections ON teaching.section_id = sections.id
-- JOIN subjects ON sections.subject_id = subjects.id
-- JOIN departments ON subjects.department_id = departments.id
-- LEFT JOIN studying ON teaching.section_id = studying.section_id
-- WHERE teaching.teacher_id = '23500120'
-- GROUP BY teaching.section_id;

-- SELECT teaching.section_id
-- FROM teaching
-- JOIN sections ON teaching.section_id = sections.id
-- WHERE teaching.teacher_id = '23500120'
-- AND sections.section_number = 2;

-- SELECT teaching.teacher_id
-- FROM sections
-- JOIN teaching ON sections.id = teaching.section_id
-- WHERE sections.subject_id = 'MA001'
-- AND sections.section_number = 2;

-- SELECT subjects.name 
-- FROM sections 
-- JOIN subjects ON sections.subject_id = subjects.id            
-- WHERE sections.id = 64;

-- SELECT sections.id, teaching.teacher_id
-- FROM sections
-- JOIN teaching ON sections.id = teaching.section_id
-- WHERE sections.subject_id = 'MA001'  
-- AND sections.section_number = 1
-- AND sections.period = '2025-2';

-- SELECT studying.student_id
-- FROM sections
-- JOIN studying ON sections.id = studying.section_id
-- WHERE sections.subject_id = 'MA001'
-- AND sections.period = '2025-2'
-- AND studying.student_id = '30500100';

-- SELECT subjects.id, subjects.name, subjects.semester, subjects.credits, subjects.sections
-- FROM subjects
-- JOIN students ON subjects.department_id = students.department_id
-- WHERE students.id = '30500100'
-- EXCEPT
-- SELECT subjects.id, subjects.name, subjects.semester, subjects.credits, subjects.sections
-- FROM studying
-- JOIN sections ON studying.section_id = sections.id 
-- JOIN subjects ON sections.subject_id = subjects.id
-- JOIN grades ON studying.student_id = grades.student_id AND studying.section_id = grades.section_id
-- JOIN teaching ON studying.section_id = teaching.section_id
-- JOIN teachers ON teaching.teacher_id = teachers.id
-- WHERE studying.student_id = '30500100';

-- INSERT INTO studying (student_id, section_id)
-- SELECT id, 28
-- FROM students
-- WHERE department_id = 'SE70'
-- LIMIT 50;

-- INSERT INTO grades (student_id, section_id, grade, teacher_id) 
-- SELECT id, 28, 0, '23500120'
-- FROM students
-- WHERE department_id = 'SE70'
-- LIMIT 50;

-- UPDATE grades
-- SET grade = (
--     SELECT AVG(grade) FROM evaluated
--     WHERE student_id = '12621509'
-- )
-- WHERE section_id = 28;

-- UPDATE grades
-- SET grade = (
--     SELECT SUM(e.grade * s.percentage) / 100.0
--     FROM evaluated e
--     JOIN strategies s ON e.strategy_id = s.id
--     WHERE e.student_id = grades.student_id
--       AND s.section_id = 64
-- )
-- WHERE section_id = 64;

-- UPDATE evaluated SET grade = 0
-- WHERE grade IS NULL;

-- SELECT *
-- FROM grades
-- WHERE student_id = '11005171';

SELECT COUNT(student_id) AS 'enrolled'
FROM studying
WHERE section_id = 28;