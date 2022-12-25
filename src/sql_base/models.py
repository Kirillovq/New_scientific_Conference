from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    login: str
    password: str
    post: Optional[int]
    reg_date: Optional[datetime]

class Subjects(BaseModel):
    id: Optional[int]
    name: str

class staff(BaseModel):
    id: Optional[int]
    name: str
    surname: str
    code_departments: Optional[int]
    positions: Optional[str]
    scientific_degree: Optional[str]


class conference(BaseModel):
    id: Optional[int]
    name_conference: Optional[str]
    code_department: Optional[int]
    code_director: Optional[str]
    nachalo_provedenie: Optional[str]
    konec_provedenie: Optional[str]
    code_type_provedenie: Optional[str]
    classroom: Optional[str]
    code_plan: Optional[str]
    code_report: Optional[str]
    code_order: Optional[str]
    code_sections: Optional[str]

class universities(BaseModel):
    id: Optional[int]
    name_university: Optional[str]
    telephone: Optional[int]
    address: Optional[str]
    email: Optional[str]
    code_faculty: Optional[str]
    code_city: Optional[str]
    number_of_universities: Optional[str]

class faculty(BaseModel):
    id: Optional[int]
    name_faculty: Optional[str]
    telephone: Optional[int]
    email: Optional[str]
    code_departments: Optional[str]

class departments(BaseModel):
    id: Optional[int]
    name_departments: Optional[str]
    telephone: Optional[int]
    email: Optional[str]
    code_specialty: Optional[str]

class students(BaseModel):
    id: Optional[int]
    FIO: str
    code_department: Optional[int]
    code_group: Optional[str]
    date_of_birth: Optional[str]

class academic_degrees(BaseModel):
    id: Optional[int]
    scientific_degree: Optional[str]

class approving(BaseModel):
    id: Optional[int]
    code_employee: Optional[str]

class type_conference(BaseModel):
    id: Optional[int]
    type_conference: Optional[str]

class plans(BaseModel):
    id: Optional[int]
    code_provedenie: Optional[str]
    calendar_year: Optional[str]

class sections(BaseModel):
    id: Optional[int]
    name_sections: Optional[str]
    code_doclada: Optional[str]

class doclad(BaseModel):
    id: Optional[int]
    topic_doclad: Optional[str]
    code_students: Optional[str]

