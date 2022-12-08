from typing import Optional
from pydantic import BaseModel


class Staff(BaseModel):
    id: Optional[int]
    name: Optional[str]
    surname: Optional[str]
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


class User(BaseModel):
    login: str
    password: str