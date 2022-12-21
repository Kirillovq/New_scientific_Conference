from fastapi import APIRouter
from sql_base.models import conference
import resolvers.conference


conference_router = APIRouter()

@conference_router.get('/')
def get_conference():
    return f'Response:{{text:Страница со списком конференций}}'

@conference_router.post("/")
def new_conference(conference: conference,):
    new_id = resolvers.conference.new_conference(conference)
    return f"{{code: 201, id: {new_id}}}"

