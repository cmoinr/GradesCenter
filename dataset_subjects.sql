INSERT INTO
    subjects(id, name, department_id, semester, credits, sections)
    VALUES  -- SE70 - Ingeniería en Sistemas
            ('MA001', 'Math 1',            'SE70', 1, 5, 3),
            ('LM002', 'Logic & Math',      'SE70', 1, 3, 3),
            ('LA003', 'Language',          'SE70', 1, 2, 3),
            ('EN004', 'English 1',         'SE70', 1, 2, 3),
            ('DE005', 'Digital Economics', 'SE70', 1, 2, 3),
            ('MA006', 'Math 2',            'SE70', 2, 5, 3),
            ('DS007', 'Data Structures',   'SE70', 2, 4, 3),
            ('OS008', 'Operating Systems', 'SE70', 3, 5, 3),
            ('DB009', 'Databases',         'SE70', 3, 4, 3),
            ('AI010', 'Artificial Intelligence', 'SE70', 4, 5, 3),
            ('WD011', 'Web Development',   'SE70', 4, 4, 3),
            ('CN012', 'Computer Networks', 'SE70', 5, 5, 3),
            ('ML013', 'Machine Learning',  'SE70', 6, 5, 3),
            ('SE014', 'Software Engineering', 'SE70', 7, 4, 3),
            ('CS015', 'Cybersecurity',     'SE70', 8, 4, 3),
            ('CP016', 'Capstone Project',  'SE70', 10, 6, 3),

            -- ME02 - Medicina
            ('HA011', 'Human Anatomy',          'ME02', 1, 5, 3),
            ('HE012', 'Histology & Embryology', 'ME02', 1, 4, 3),
            ('GM013', 'General Medicine',       'ME02', 1, 5, 3),
            ('PM014', 'Preventive Medicine',    'ME02', 1, 3, 3),
            ('AN015', 'Anthropology',           'ME02', 1, 4, 3),
            ('PH016', 'Physiology',        'ME02', 2, 5, 3),
            ('BI017', 'Biochemistry',      'ME02', 2, 4, 3),
            ('PA018', 'Pathology',         'ME02', 3, 5, 3),
            ('PH019', 'Pharmacology',      'ME02', 4, 4, 3),
            ('MI020', 'Microbiology',      'ME02', 5, 5, 3),
            ('IM021', 'Internal Medicine', 'ME02', 6, 5, 3),
            ('SU022', 'Surgery',           'ME02', 7, 5, 3),
            ('PE023', 'Pediatrics',        'ME02', 8, 4, 3),
            ('OB024', 'Obstetrics',        'ME02', 9, 4, 3),
            ('RE025', 'Residency',         'ME02', 10, 6, 3),

            -- EC03 - Economía
            ('MI021', 'Microeconomics',    'EC03', 1, 5, 3),
            ('MA022', 'Macroeconomics',    'EC03', 1, 3, 3),
            ('EC023', 'Econometrics',      'EC03', 1, 2, 3),
            ('CF024', 'Corporate Finance', 'EC03', 1, 3, 3),
            ('GT025', 'Game Theory',       'EC03', 1, 2, 3),
            ('MI026', 'Microeconomics 2',  'EC03', 2, 5, 3),
            ('MA027', 'Macroeconomics 2',  'EC03', 2, 4, 3),
            ('FI028', 'Financial Markets', 'EC03', 3, 5, 3),
            ('IN029', 'International Trade', 'EC03', 4, 4, 3),
            ('PU030', 'Public Economics',  'EC03', 5, 5, 3),
            ('DE031', 'Development Economics', 'EC03', 6, 5, 3),
            ('BE032', 'Behavioral Economics', 'EC03', 7, 4, 3),
            ('PO033', 'Political Economy', 'EC03', 8, 4, 3),
            ('TH034', 'Thesis',            'EC03', 10, 6, 3),

            -- DE04 - Odontología
            ('OA031', 'Oral Anatomy',        'DE04', 1, 5, 3),
            ('EN032', 'Endodontics',         'DE04', 1, 4, 3),
            ('PE033', 'Periodontics',        'DE04', 1, 4, 3),
            ('DP034', 'Dental Prosthetics',  'DE04', 1, 3, 3),
            ('PD035', 'Pediatric Dentistry', 'DE04', 1, 3, 3),
            ('OR036', 'Oral Radiology',    'DE04', 2, 5, 3),
            ('PA037', 'Pathology',         'DE04', 3, 4, 3),
            ('OR038', 'Orthodontics',      'DE04', 4, 5, 3),
            ('IM039', 'Implantology',      'DE04', 5, 4, 3),
            ('PE040', 'Pediatric Dentistry 2', 'DE04', 6, 5, 3),
            ('SU041', 'Surgical Dentistry', 'DE04', 7, 5, 3),
            ('CO042', 'Community Dentistry', 'DE04', 8, 4, 3),
            ('TH043', 'Thesis',            'DE04', 10, 6, 3),                       

            -- AG05 - Agronomía
            ('SO041', 'Soils',                  'AG05', 1, 5, 3),
            ('PP042', 'Plant Pathology',        'AG05', 1, 4, 3),
            ('GE043', 'Genetics',               'AG05', 1, 4, 3),
            ('HY044', 'Hydrology',              'AG05', 1, 3, 3),
            ('AE045', 'Agricultural Economics', 'AG05', 1, 3, 3),
            ('CR046', 'Crop Science',      'AG05', 2, 5, 3),
            ('AG047', 'Agronomy 2',        'AG05', 3, 4, 3),
            ('IR048', 'Irrigation Systems','AG05', 4, 5, 3),
            ('AE049', 'Agroecology',       'AG05', 5, 4, 3),
            ('FM050', 'Farm Management',   'AG05', 6, 5, 3),
            ('PL051', 'Plant Breeding',    'AG05', 7, 5, 3),
            ('TH052', 'Thesis',            'AG05', 10, 6, 3),

            -- SC06 - Ciencias de la Comunicación
            ('CT051', 'Communication Theory',   'SC06', 1, 5, 3),
            ('JW052', 'Journalism Writing',     'SC06', 1, 4, 3),
            ('AP053', 'Audiovisual Production', 'SC06', 1, 4, 3),
            ('SE054', 'Semiotics',              'SC06', 1, 3, 3),
            ('MR055', 'Market Research',        'SC06', 1, 3, 3),
            ('ME056', 'Media Ethics',     'SC06', 2, 5, 3),
            ('PR057', 'Public Relations', 'SC06', 3, 4, 3),
            ('AD058', 'Advertising',      'SC06', 4, 5, 3),
            ('BR059', 'Broadcasting',     'SC06', 5, 4, 3),
            ('DI060', 'Digital Media',    'SC06', 6, 5, 3),
            ('TH061', 'Thesis',           'SC06', 10, 6, 3),

            -- PO90 - Ciencias Políticas
            ('PT061', 'Political Theory',               'PO90', 1, 5, 3),
            ('PS062', 'Political Science',              'PO90', 1, 4, 3),
            ('IR063', 'International Relations',        'PO90', 1, 4, 3),
            ('CL064', 'Constitutional Law',             'PO90', 1, 3, 3),
            ('PM065', 'Political Research Methodology', 'PO90', 1, 3, 3),
            ('CO066', 'Comparative Politics', 'PO90', 2, 5, 3),
            ('PU067', 'Public Policy',        'PO90', 3, 4, 3),
            ('DI068', 'Diplomacy',            'PO90', 4, 5, 3),
            ('GE069', 'Geopolitics',          'PO90', 5, 4, 3),
            ('TH070', 'Thesis',               'PO90', 10, 6, 3);