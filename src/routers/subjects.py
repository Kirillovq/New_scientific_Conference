from fastapi import APIRouter
from src.sql_base import subjects
import resolvers.subjects

subj_router = APIRouter

@subj_router.put('/')
def new_subject(subject: subjects):
    new_id = resolvers.subjects.new_subject(subject)
    return f'{{code: 201, id: {new_id}}}'

