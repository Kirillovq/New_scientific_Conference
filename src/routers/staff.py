from fastapi import APIRouter
from sql_base.models import staff
import resolvers.staff


staff_router = APIRouter()

@staff_router.get('/')
def get_staff():
    return f'Response:{{text:Страница со списком сотрудников}}'

@staff_router.post("/")
def new_staff(staff: staff,):
    new_id = resolvers.staff.new_staff(staff)
    return f"{{code: 201, id: {new_id}}}"

@staff_router.get('/{staff_id}')
def get_student(staff_id: int):
    staff = resolvers.get_staff(staff_id)
    return f'Staff: {{name: имя студена, surname: фамилия, id: {staff_id}}}'


@staff_router.put('/{staff_id}')
def update_staff(staff_id: int):
    return f'Update staff {staff_id}'


@staff_router.delete('/{staff_id}')
def delete_staff(staff_id: int):
    return f'delete staff {staff_id}'