from fastapi import APIRouter, Depends, UploadFile,status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers.DataController import DataController
from controllers.ProjectController import ProjectController
import aiofiles
from models import ResponseSignal
import os
import logging

logger=logging.getLogger('uvicorn.error')


data_router = APIRouter(
    prefix="/api/v1/data", 
    tags=["api_v1","data"],
    )

@data_router.post("/upload/{project_id}")
async def upload_data(
 project_id: str,
 file: UploadFile,
 app_settings: Settings =Depends(get_settings)):

  #validate the file properties
  data_Controller=DataController()
  is_valid, resulte_signal=data_Controller.validate_uploaded_file(file=file)

  if not is_valid:
    return JSONResponse(
      status_code=status.HTTP_400_BAD_REQUEST,
      content={
         "signal":resulte_signal

      }
    ) 
    
  project_dir_path=ProjectController().get_project_path(project_id=project_id)
  file_path=data_Controller.generate_uniqe_filename(
    orig_file_name=file.filename,
    project_id=project_id
  )
  try:
    async with aiofiles.open(file_path,"wb")as f:
     while chunk:=await file.read(app_settings.FILE_DEFFAULT_CHUNK_SIZE):
      await f.write(chunk)
  except Exception as e:
    logger.error(f"Error while uploading file:{e}")
    return JSONResponse(
      status_code=status.HTTP_400_BAD_REQUEST,
      content={
         "signal":ResponseSignal.FILE_UPLOAD_FALED.value

      }
    ) 

  
    
    return JSONResponse(
      content={
         "signal":ResponseSignal.FILE_UPLOAD_SUCCESS.value

      }
    ) 

  
 