from mutantValidation import is_mutant
from validations import validateInput, matrixToUpper
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class RequestInput(BaseModel):
  dna: list[str]

app = FastAPI()

@app.get('/')
async def root():
  return {
    'mutantDnaExample': ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"],
    'notMutantDnaExample': ["ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"]
  }

@app.post('/mutant')
async def getMutantValidation(input: RequestInput):
  dnaValue = input.dna
  validation, message = validateInput(dnaValue)

  if not validation:
    # Matrix can not be analysed by the code correctly
    return JSONResponse(
      status_code=status.HTTP_400_BAD_REQUEST, 
      content={
        "status": "Error",
        "message": message
        }
      )
  
  matrixToUpper(dnaValue)
  result, _ = is_mutant(dnaValue)
  
  if not result:
    # Is human
    return JSONResponse(
      status_code=status.HTTP_403_FORBIDDEN, 
      content={
        "status": "Ok",
        "is_mutant": result
      }
    )
  
  else:
    # Is mutant
    return JSONResponse(
      status_code=status.HTTP_200_OK, 
      content={
        "status": "Ok", 
        "is_mutant": result,
        "dnaAnalysed": dnaValue
        }
      )

# In the future, this endpoint could change to a get, with an id as param. Returning details of another execution, saved in a DDBB.
@app.post('/mutant/details')
async def getMutantValidationDetails(input: RequestInput):
  dnaValue = input.dna
  validation, message = validateInput(dnaValue)

  if not validation:
    # Matrix can not be analysed by the code correctly
    return JSONResponse(
      status_code=status.HTTP_400_BAD_REQUEST, 
      content={
        "status": "Error",
        "message": message
        }
      )
  
  matrixToUpper(dnaValue)
  _, result = is_mutant(dnaValue)

  if not result:
    # Is human
    return JSONResponse(
      status_code=status.HTTP_403_FORBIDDEN, 
      content={
        "status": "Ok",
        "is_mutant": result
        }
      )
  
  else:
    # Is mutant
    return JSONResponse(
      status_code=status.HTTP_200_OK, 
      content={
        "status": "Ok", 
        **result,
        "dnaAnalysed": dnaValue
        }
      )