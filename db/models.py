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
        
        
