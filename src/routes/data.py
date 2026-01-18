<<<<<<< HEAD
from fastapi import APIRouter, Depends, UploadFile,status
=======
from fastapi import APIRouter, Depends, UploadFile,status , Request
>>>>>>> tut-006
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers.DataController import DataController
from controllers.ProjectController import ProjectController
from controllers.ProcessController import ProcessController
import aiofiles
from models import ResponseSignal
import os
import logging
from .cheames.data import ProcessRequest
<<<<<<< HEAD
=======
from models.ProjectModel import ProjectModel
>>>>>>> tut-006

logger=logging.getLogger('uvicorn.error')


data_router = APIRouter(
    prefix="/api/v1/data", 
    tags=["api_v1","data"],
    )

@data_router.post("/upload/{project_id}")
async def upload_data(
<<<<<<< HEAD
=======
 request:Request,
>>>>>>> tut-006
 project_id: str,
 file: UploadFile,
 app_settings: Settings =Depends(get_settings)):

<<<<<<< HEAD
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
  file_path , file_id =data_Controller.generate_uniqe_filepath(
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
         "signal":ResponseSignal.FILE_UPLOAD_FAILED.value

      }
    ) 

  return JSONResponse(
      content={
         "signal":ResponseSignal.FILE_UPLOAD_SUCCESS.value,
         "file_id":file_id
      }
    ) 
=======
      project_model=ProjectModel(
        db_client=request.app.db_client
      )

      project = await project_model.get_project_or_create_one(
         project_id=project_id
      )

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
      file_path , file_id =data_Controller.generate_uniqe_filepath(
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
            "signal":ResponseSignal.FILE_UPLOAD_FAILED.value

              }
           ) 

      return JSONResponse(
          content={
            "signal":ResponseSignal.FILE_UPLOAD_SUCCESS.value,
            "file_id":file_id,
            "project_id":str(project._id)
          }
         ) 
>>>>>>> tut-006
@data_router.post("/process/{project_id}")
async def process_endpoint(project_id:str, process_request:ProcessRequest):
  file_id= process_request.file_id
  chunk_size=process_request.chunk_size
  overlap_size=process_request.overlap_size
  
  process_controller=ProcessController(project_id=project_id)

  file_content=process_controller.get_file_content(file_id=file_id)

  file_chunk=process_controller.process_file_content(
    file_content=file_content,
    file_id=file_id,
    chunk_size=chunk_size,
    overlap_size=overlap_size
  )

  if file_chunk is None or len(file_chunk)==0:
    return JSONResponse(
      status_code=status.HTTP_400_BAD_REQUEST,
      content={
         "signal":ResponseSignal.PROCESSING_FAILED.value

      }
    ) 
  return file_chunk
  
  
 