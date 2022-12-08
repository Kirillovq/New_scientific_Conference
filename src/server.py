from fastap1 import FastAPI
from sql_base import base_worker
from settings import BASE_PATH
from routers.students import stud_router


base_worker.set_base_path(BASE_PATH)

in not base_worker.check_base():
    base_worker.create_base('../sql/base.sql')

app = FastAPI()
app.include_router(stud_router, prefix='/conferentce')