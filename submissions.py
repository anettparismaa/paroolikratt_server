from fastapi import HTTPException, Response, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import APIRouter
import base64 
from database import get_db, engine
import models
import schemas

router = APIRouter(
    prefix='/submissions',
    tags=['Submission']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_submission(submission_create: schemas.CreateSubmission, db: Session = Depends(get_db)) -> Response:
    submission_input = submission_create.dict()

    user_input = base64.b64encode(submission_input['content'].encode()).decode()

    leaked_query = select(models.LeakedPassword).where(models.LeakedPassword.content==user_input)
    leaked_response = db.execute(leaked_query)
    leaked_matched = leaked_response.first() != None
    submission_input["matched_leak"] = leaked_matched

    generated_query = select(models.GeneratedPassword).where(models.GeneratedPassword.content==user_input)
    generated_response = db.execute(generated_query)
    generated_matched = generated_response.first() != None
    submission_input["matched_generated"] = generated_matched

    submission_query = select(models.Submission).where(models.Submission.content==user_input)
    submission_response = db.execute(submission_query)
    submission_matched = submission_response.first() != None
    submission_input["matched_submission"] = submission_matched

    submission_input['content'] = user_input
    new_submission = models.Submission(**submission_input)
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)

    return JSONResponse(content={"leaked": leaked_matched or submission_matched, "dangerous": generated_matched})

