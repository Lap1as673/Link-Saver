from sqlalchemy.orm import Session
from typing import Optional  # ДОБАВЬТЕ ЭТУ СТРОЧКУ!
from . import models, schemas

# CRUD для списков
def get_list(db: Session, list_id: int):
    return db.query(models.List).filter(models.List.id == list_id).first()

def get_lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.List).offset(skip).limit(limit).all()

def create_list(db: Session, list: schemas.ListCreate):
    db_list = models.List(name=list.name)
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list

# CRUD для ссылок
def get_links(db: Session, skip: int = 0, limit: int = 100, list_id: Optional[int] = None):
    query = db.query(models.Link)
    if list_id:
        query = query.filter(models.Link.list_id == list_id)
    return query.offset(skip).limit(limit).all()

def create_link(db: Session, link: schemas.LinkCreate):
    db_link = models.Link(
        url=link.url,
        title=link.title,
        description=link.description,
        list_id=link.list_id
    )
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

def delete_link(db: Session, link_id: int):
    db_link = db.query(models.Link).filter(models.Link.id == link_id).first()
    if db_link:
        db.delete(db_link)
        db.commit()
    return db_link  