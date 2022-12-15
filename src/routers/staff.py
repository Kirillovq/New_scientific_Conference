from fastapi import APIRouter
from sql_base.models import staff
import resolvers.staff


staff_router = APIRouter()


@staff_router.post("/staff")
def new_staff(staff: staff,):
    new_id = resolvers.staff.new_staff(staff)
    return f"{{code: 201, id: {new_id}}}"