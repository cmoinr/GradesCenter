INSERT INTO 
    subjects(id,      name,                id_faculty, semester, credits)
    VALUES  ('MA101', 'Math 1',            'SE70',     1,        5),
            ('LM002', 'Logic & Math',      'SE70',     1,        3),
            ('LA003', 'Language',          'SE70',     1,        2),
            ('EN104', 'English 1',         'SE70',     1,        2),
            ('DE005', 'Digital Economics', 'SE70',     1,        2);

INSERT INTO
    faculty (id, field)
    VALUES  ('SE70', 'Systems Engineering'),
            ('ME02', 'Medicine'),
            ('EC03', 'Economics'),
            ('DE04', 'Dentistry'),
            ('AG05', 'Agronomy'),
            ('SC06', 'Social Communication'),
            ('PO90', 'Politics');