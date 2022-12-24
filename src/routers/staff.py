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

@staff_router.get(f'/{staff_id}')
def get_staff(staff_id: int):
    staff = resolvers.get_staff(staff_id)
    return 'staff: {name_of_the_organization: название организации, address: адрес}'


@staff_router.put(f'/{staff_id}')
def update_staff(staff_id: int):
     return f'Update staff {staff_id}'


@staff_router.delete(f'/{staff_id}')
def delelte_staff(staff_id: int):
     return f'delete staff {staff_id}'