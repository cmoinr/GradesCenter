-- Inserta 3 secciones para cada materia en la tabla "subjects"
INSERT INTO sections (subject_id, section_number, period)
SELECT 
    subjects.id AS subject_id,
    section_number,
    '2025-2' AS period -- Cambia el periodo según sea necesario
FROM subjects
CROSS JOIN (
    SELECT 1 AS section_number
    UNION ALL
    SELECT 2
    UNION ALL
    SELECT 3
) AS sections_per_subject;