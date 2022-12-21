from sql_base import base_worker
from sql_base import models


def new_staff(staff: models.staff) -> int:
    new_id = base_worker.insert_data("INSERT INTO staff(id, name, surname, code_departments, positions, scientific_degree)"
                                 "VALUES (?, ?, ?, ?, ?, ?)"
                                 "RETURNING id",
                                 (staff.id, staff.name, staff.surname, staff.code_departments, staff.positions, staff.scientific_degree))
    return new_id

def get_staff(staff_id: int):
    return base_worker.insert_data("SELECT id, name, surname, code_deportaments, positions, scientific_degree FROM staff WHERE id =?",
                               (staff_id,))

def delete_staff(staff_id: int):
    return base_worker.insert_data("DELETE FROM staff WHERE id=? ",
                               (staff_id,))