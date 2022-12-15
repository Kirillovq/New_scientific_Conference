from sql_base import base_worker
from sql_base import models


def new_subject(staff: models.staff) -> int:
    new_id = base_worker.insert_date("INSERT INTO staff(id, named, surname, code_deportaments, positions, scientific_degree)"
                                 "VALUES (?, ?, ?, ?, ?, ?)"
                                 "RETURNING id",
                                 (staff.id, staff.named, staff.surname, staff.code_deportaments, staff.positions,staff.scientific_degree))
    return new_id


