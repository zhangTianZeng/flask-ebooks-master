#coding:utf-8

from sqlalchemy import db


#言情
class YanQingBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    img = db.Column(db.String(500))
    cate = db.Column(db.String(20))
    author = db.Column(db.String(20))
    size = db.Column(db.String(20))
    date = db.Column(db.String(20))
    down = db.Column(db.String(20))
    def __init__(self,title,img,cate,author,size,date,down):
        self.title = title
        self.img = img
        self.cate = cate
        self.author =author
        self.size = size
        self.date = date
        self.down =down
    def __repr__(self):
        return "<YanQingBooks %d %s>" % (self.id,self.title)
#都市
class DuShiBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    img = db.Column(db.String(500))
    cate = db.Column(db.String(20))
    author = db.Column(db.String(20))
    size = db.Column(db.String(20))
    date = db.Column(db.String(20))
    down = db.Column(db.String(20))
    def __init__(self,title,img,cate,author,size,date,down):
        self.title = title
        self.img = img
        self.cate = cate
        self.author =author
        self.size = size
        self.date = date
        self.down =down
    def __repr__(self):
        return "<DuShiBooks %d %s>" % (self.id,self.title)
#穿越
class ChuanYueBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    img = db.Column(db.String(500))
    cate = db.Column(db.String(20))
    author = db.Column(db.String(20))
    size = db.Column(db.String(20))
    date = db.Column(db.String(20))
    down = db.Column(db.String(20))
    def __init__(self,title,img,cate,author,size,date,down):
        self.title = title
        self.img = img
        self.cate = cate
        self.author =author
        self.size = size
        self.date = date
        self.down =down
    def __repr__(self):
        return "<ChuanYueBooks %d %s>" % (self.id,self.title)
#耿美
class GengMeiBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    img = db.Column(db.String(500))
    cate = db.Column(db.String(20))
    author = db.Column(db.String(20))
    size = db.Column(db.String(20))
    date = db.Column(db.String(20))
    down = db.Column(db.String(20))
    def __init__(self,title,img,cate,author,size,date,down):
        self.title = title
        self.img = img
        self.cate = cate
        self.author =author
        self.size = size
        self.date = date
        self.down =down
    def __repr__(self):
        return "<GengMeiBooks %d %s>" % (self.id,self.title)
#玄幻
class XuanHuanBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    img = db.Column(db.String(500))
    cate = db.Column(db.String(20))
    author = db.Column(db.String(20))
    size = db.Column(db.String(20))
    date = db.Column(db.String(20))
    down = db.Column(db.String(20))
    def __init__(self,title,img,cate,author,size,date,down):
        self.title = title
        self.img = img
        self.cate = cate
        self.author =author
        self.size = size
        self.date = date
        self.down =down
    def __repr__(self):
        return "<XuanHuanBooks %d %s>" % (self.id,self.title)
#网游
class WangYouBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    img = db.Column(db.String(500))
    cate = db.Column(db.String(20))
    author = db.Column(db.String(20))
    size = db.Column(db.String(20))
    date = db.Column(db.String(20))
    down = db.Column(db.String(20))
    def __init__(self,title,img,cate,author,size,date,down):
        self.title = title
        self.img = img
        self.cate = cate
        self.author =author
        self.size = size
        self.date = date
        self.down =down
    def __repr__(self):
        return "<WangYouBooks %d %s>" % (self.id,self.title)

#武侠
class WuXiaBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    img = db.Column(db.String(500))
    cate = db.Column(db.String(20))
    author = db.Column(db.String(20))
    size = db.Column(db.String(20))
    date = db.Column(db.String(20))
    down = db.Column(db.String(20))
    def __init__(self,title,img,cate,author,size,date,down):
        self.title = title
        self.img = img
        self.cate = cate
        self.author =author
        self.size = size
        self.date = date
        self.down =down
    def __repr__(self):
        return "<WuXiaBooks %d %s>" % (self.id,self.title)

#历史
class LiShiBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    img = db.Column(db.String(500))
    cate = db.Column(db.String(20))
    author = db.Column(db.String(20))
    size = db.Column(db.String(20))
    date = db.Column(db.String(20))
    down = db.Column(db.String(20))
    def __init__(self,title,img,cate,author,size,date,down):
        self.title = title
        self.img = img
        self.cate = cate
        self.author =author
        self.size = size
        self.date = date
        self.down =down
    def __repr__(self):
        return "<LiShiBooks %d %s>" % (self.id,self.title)

#悬疑
class XuanYiBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    img = db.Column(db.String(500))
    cate = db.Column(db.String(20))
    author = db.Column(db.String(20))
    size = db.Column(db.String(20))
    date = db.Column(db.String(20))
    down = db.Column(db.String(20))
    def __init__(self,title,img,cate,author,size,date,down):
        self.title = title
        self.img = img
        self.cate = cate
        self.author =author
        self.size = size
        self.date = date
        self.down =down
    def __repr__(self):
        return "<XuanYiBooks %d %s>" % (self.id,self.title)

#同人
class TongRenBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    img = db.Column(db.String(500))
    cate = db.Column(db.String(20))
    author = db.Column(db.String(20))
    size = db.Column(db.String(20))
    date = db.Column(db.String(20))
    down = db.Column(db.String(20))
    def __init__(self,title,img,cate,author,size,date,down):
        self.title = title
        self.img = img
        self.cate = cate
        self.author =author
        self.size = size
        self.date = date
        self.down =down
    def __repr__(self):
        return "<TongRenBooks %d %s>" % (self.id,self.title)