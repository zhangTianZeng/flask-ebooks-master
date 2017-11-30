#coding:utf-8

from flask_script import Manager
from ebooks import app
from ebooks.sqlalchemy import db
from ebooks.models import *
manager = Manager(app)

@manager.command
def init_database():


    file = open(r"C:\Users\Administrator\Desktop\ebooks\ChuanYue.txt","r")
    while True:
        findstrr =file.readline()
        print(findstrr)
        if not findstrr:
            break

        strlist = findstrr.split("##")
        print(len(strlist))
        if len(strlist)==8:
            db.session.add(ChuanYueBooks(unicode(strlist[0]),unicode(strlist[1]),unicode(strlist[2]),
                                        unicode(strlist[3]),unicode(strlist[4]),unicode(strlist[5]),unicode(strlist[6])))
            db.session.commit()
        pass



if __name__=="__main__":
    init_database()
    manager.run()
