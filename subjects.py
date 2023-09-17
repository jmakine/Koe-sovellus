from db import db
from sqlalchemy.sql import text

def get_subjects():
    sql = "SELECT * from subjects;"
    return db.session.execute(text(sql)).fetchall()

def get_subject(id):
    sql = "SELECT * FROM subjects WHERE id=:id;"
    return db.session.execute(text(sql), {"id":id}).fetchone()

def add_subject(name):
    try:
        sql = "INSERT INTO subjects (name) VALUES (:name)"
        db.session.execute(text(sql), {"name":name})
        db.session.commit()
    except:
        return False

def delete_subject(id):
    try:
        sql = "DELETE FROM subjects WHERE id=:id"
        db.session.execute(text(sql), {"id":id})
        db.session.commit()
    except:
        return False

def subjectname_exists(name):
    sql = "SELECT COUNT(name) FROM subjects WHERE name=:name GROUP by name"
    subjectname_exists = db.session.execute(text(sql), {"name":name}).fetchall()
    return subjectname_exists != []