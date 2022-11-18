CREATE TABLE IF NOT EXISTS users(
    id INTEGER NOT NULL PRIMARY KEY,
    login VARCHAR(100) NOT NULL UNIQUE
    password VARCHAR(100) NOT NULL);

CREATE TABLE IF NOT EXISTS staff(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    name VARCHAR(15) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    code_departments VARCHAR(100) NOT NULL,
    positions VARCHAR(100) NOT NULL,
    scientific_degree VARCHAR(100) NOT NULL
    FOREIGN KEY(code_departaments)
        REFERENCES departaments(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY (scientific_degree)
        REFERENCES degree(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS conference(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    name_conference VARCHAR(100) NOT NULL,
    code_department VARCHAR(100) NOT NULL,
    code_director VARCHAR(100) NOT NULL,
    nachalo_provedenie VARCHAR(100) NOT NULL,
    konec_provedenie VARCHAR(100) NOT NULL,
    code_type_provedenie INTEGER NOT NULL,
    classroom INTEGER NOT NULL,
    code_plan INTEGER NOT NULL,
    code_report INTEGER NOT NULL,
    code_order INTEGER NOT NULL,
    code_sections INTEGER NOT NULL
    FOREIGN KEY (departaments)
        REFERENCES code_departaments(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY (code_type_provedenie)
        REFERENCES type_conference(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY (code_director)
        REFERENCES staff(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY (code_plan)
        REFERENCES plans(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY (code_sections)
        REFERENCES sections(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS universities(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    name_university VARCHAR(100) NOT NULL,
    telephone INTEGER NOT NULL,
    address VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    code_faculty INTEGER NOT NULL,
    code_city INTEGER NOT NULL,
    number_of_universities INTEGER NOT NULL
    FOREIGN KEY (code_faculty)
        REFERENCES faculty(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS faculty(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    name_faculty VARCHAR(100) NOT NULL,
    telephone INTEGER NOT NULL,
    email VARCHAR(100) NOT NULL,
    code_departaments INTEGER NOT NULL
    FOREIGN KEY (code_departaments)
        REFERENCES departaments(id)
    ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS departments(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    name_departments VARCHAR(100) NOT NULL,
    telephone INTEGER NOT NULL,
    email VARCHAR(100) NOT NULL,
    code_specialty INTEGER NOT NULL);

CREATE TABLE IF NOT EXISTS students(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    FIO VARCHAR(100) NOT NULL,
    code_department INTEGER NOT NULL,
    code_gruop VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL
    FOREIGN KEY (code_department)
        REFERENCES departaments(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY (code_gruop)
        REFERENCES gruop(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS academic_degrees(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    scientific_degree VARCHAR(100) NOT NULL);

CREATE TABLE IF NOT EXISTS approving(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    code_employee INTEGER NOT NULL
    FOREIGN KEY (code_employee)
        REFERENCES staff(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS type_conference(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    type_conference VARCHAR(100) NOT NULL);

CREATE TABLE IF NOT EXISTS plans(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    code_provedenie INTEGER NOT NULL,
    calendar_year DATE NOT NULL);

CREATE TABLE IF NOT EXISTS sections(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    name_sections VARCHAR(100) NOT NULL,
    code_doclada INTEGER NOT NULL
    FOREIGN KEY (code_doclada)
        REFERENCES doclad(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS doclad(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    topic_doclad VARCHAR(100) NOT NULL,
    code_students INTEGER NOT NULL
    FOREIGN KEY (code_students)
        REFERENCES students(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);




INSERT INTO users(login, password)
VALUES ('login','password'),('login1','password1');

INSERT INTO staff(name, surname)
VALUES ('name','surname','departaments','positions','scientific_degree'),('name1','surname1','departaments1','positions1','scientific_degree1');