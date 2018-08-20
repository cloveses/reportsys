import os
import datetime
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