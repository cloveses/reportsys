import os
import datetime
import math
from pony.orm import *

db = Database()

class Recorder(db.Entity):
    name = Required(str)
    machine_name = Required(str)
    fault = Required(str)
    date_time = Required(datetime.datetime,default=datetime.datetime.now())
    status = Required(bool,default=False)

class User(db.Entity):
    name = Required(str)
    tel = Required(str)

set_sql_debug(True)
filename = os.path.join(os.path.abspath(os.curdir),'my.db')
db.bind(provider='sqlite', filename=filename, create_db=True)
db.generate_mapping(create_tables=True)

@db_session
def add_recorder(params):
    r = Recorder(**params)
    commit()
    return r.id

@db_session
def get_recorder(rid):
    r = Recorder[rid]
    return r

@db_session
def get_pages(page):
    pages_num =math.ceil(count(r for r in Recorder) / 20)
    if pages_num >= 7 and page >= 3:
        pages_nums = list(range(page-3,page+3))
    else:
        pages_nums = list(range(pages_num))
    pages_nums = [n + 1 for n in pages_nums]
    if page > pages_num:
        page = 0
    res = select(r for r in Recorder).order_by(Recorder.date_time)[page*20:(page+1) * 20]
    if res:
        return pages_nums,res
    else:
        return pages_nums,[]

@db_session
def add_user():
    import csv
    if os.path.exists('data.csv') and not count(u for u in User):
        with open('data.csv') as f:
            rows = csv.reader(f)
            for row in rows:
                print(row[0],row[1])
                User(name=row[0],tel=row[1])

@db_session
def verify(name,tel):
    if select(u for u in User if u.name==name and u.tel==tel):
        return True