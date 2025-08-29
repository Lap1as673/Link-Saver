from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional

from . import models, schemas, crud
from .database import engine, get_db

# Создаем таблицы
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Link Saver API", version="1.0.0")

# НАСТРОЙКА CORS - ДОБАВЬТЕ ЭТО
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Все адреса фронтенда
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, etc.)
    allow_headers=["*"],  # Разрешить все заголовки
)

# Остальной код без изменений...
@app.post("/lists/", response_model=schemas.List)
def create_list(list: schemas.ListCreate, db: Session = Depends(get_db)):
    return crud.create_list(db=db, list=list)

@app.get("/lists/", response_model=List[schemas.List])
def read_lists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lists = crud.get_lists(db, skip=skip, limit=limit)
    return lists

@app.post("/links/", response_model=schemas.Link)
def create_link(link: schemas.LinkCreate, db: Session = Depends(get_db)):
    return crud.create_link(db=db, link=link)

@app.get("/links/", response_model=List[schemas.Link])
def read_links(skip: int = 0, limit: int = 100, list_id: Optional[int] = None, db: Session = Depends(get_db)):
    links = crud.get_links(db, skip=skip, limit=limit, list_id=list_id)
    return links

@app.delete("/links/{link_id}")
def delete_link(link_id: int, db: Session = Depends(get_db)):
    link = crud.delete_link(db, link_id=link_id)
    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return {"message": "Link deleted successfully"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}