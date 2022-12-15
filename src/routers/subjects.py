from fastapi import APIRouter
from sql_base import subjects
import resolvers.subjects

subj_router = APIRouter

@subj_router-post('/')
def new_subject(subject: subjects):
    new_id = resolvers.subjects.new_subject(subject)
    return f'{{code: 201, id: {new_id}}}'

