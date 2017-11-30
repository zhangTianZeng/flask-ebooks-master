#coding:utf-8
from ebooks.sqlalchemy import db
from flask import json
from models import *
from ebooks import app
from views import listH,listT,listL

@app.route("/yanqing_api/<int:page>/<int:per_page>/")
def yanqing_api(page,per_page):
    paginates = YanQingBooks.query.order_by(YanQingBooks.id).paginate(page=page, per_page=per_page, error_out=False)
    map = {'has_next': paginates.has_next}
    yanqing = []
    for i in range(len(paginates.items)):
        con = {
            'id': paginates.items[i].id,
            'title': paginates.items[i].title,
            'img': paginates.items[i].img,
            'cate': paginates.items[i].cate,
            'author': paginates.items[i].author,
            'size':paginates.items[i].size,
            'date':paginates.items[i].date,
            'down':paginates.items[i].down,
            'listT':listT[i],
            'listL':listL[i],
            'listH':listH[i]
        }
        yanqing.append(con)
    map['yanqing'] = yanqing
    return json.dumps(map)

@app.route("/dushi_api/<int:page>/<int:per_page>/")
def dushi_api(page,per_page):
    paginates = DuShiBooks.query.order_by(DuShiBooks.id).paginate(page=page, per_page=per_page, error_out=False)
    map = {'has_next': paginates.has_next}
    yanqing = []
    for i in range(len(paginates.items)):
        con = {
            'id': paginates.items[i].id,
            'title': paginates.items[i].title,
            'img': paginates.items[i].img,
            'cate': paginates.items[i].cate,
            'author': paginates.items[i].author,
            'size':paginates.items[i].size,
            'date':paginates.items[i].date,
            'down':paginates.items[i].down,
            'listT':listT[i],
            'listL':listL[i],
            'listH':listH[i]
        }
        yanqing.append(con)
    map['yanqing'] = yanqing
    return json.dumps(map)

@app.route("/gengmei_api/<int:page>/<int:per_page>/")
def gengmei_api(page,per_page):
    paginates = GengMeiBooks.query.order_by(GengMeiBooks.id).paginate(page=page, per_page=per_page, error_out=False)
    map = {'has_next': paginates.has_next}
    yanqing = []
    for i in range(len(paginates.items)):
        con = {
            'id': paginates.items[i].id,
            'title': paginates.items[i].title,
            'img': paginates.items[i].img,
            'cate': paginates.items[i].cate,
            'author': paginates.items[i].author,
            'size':paginates.items[i].size,
            'date':paginates.items[i].date,
            'down':paginates.items[i].down,
            'listT':listT[i],
            'listL':listL[i],
            'listH':listH[i]
        }
        yanqing.append(con)
    map['yanqing'] = yanqing
    return json.dumps(map)

@app.route("/chuanyue_api/<int:page>/<int:per_page>/")
def chuanyue_api(page,per_page):
    paginates = ChuanYueBooks.query.order_by(ChuanYueBooks.id).paginate(page=page, per_page=per_page, error_out=False)
    map = {'has_next': paginates.has_next}
    yanqing = []
    for i in range(len(paginates.items)):
        con = {
            'id': paginates.items[i].id,
            'title': paginates.items[i].title,
            'img': paginates.items[i].img,
            'cate': paginates.items[i].cate,
            'author': paginates.items[i].author,
            'size':paginates.items[i].size,
            'date':paginates.items[i].date,
            'down':paginates.items[i].down,
            'listT':listT[i],
            'listL':listL[i],
            'listH':listH[i]
        }
        yanqing.append(con)
    map['yanqing'] = yanqing
    return json.dumps(map)

@app.route("/xuanhuan_api/<int:page>/<int:per_page>/")
def xuanhuan_api(page,per_page):
    paginates = XuanHuanBooks.query.order_by(XuanHuanBooks.id).paginate(page=page, per_page=per_page, error_out=False)
    map = {'has_next': paginates.has_next}
    yanqing = []
    for i in range(len(paginates.items)):
        con = {
            'id': paginates.items[i].id,
            'title': paginates.items[i].title,
            'img': paginates.items[i].img,
            'cate': paginates.items[i].cate,
            'author': paginates.items[i].author,
            'size':paginates.items[i].size,
            'date':paginates.items[i].date,
            'down':paginates.items[i].down,
            'listT':listT[i],
            'listL':listL[i],
            'listH':listH[i]
        }
        yanqing.append(con)
    map['yanqing'] = yanqing
    return json.dumps(map)

@app.route("/wangyou_api/<int:page>/<int:per_page>/")
def wangyou_api(page,per_page):
    paginates = WangYouBooks.query.order_by(WangYouBooks.id).paginate(page=page, per_page=per_page, error_out=False)
    map = {'has_next': paginates.has_next}
    yanqing = []
    for i in range(len(paginates.items)):
        con = {
            'id': paginates.items[i].id,
            'title': paginates.items[i].title,
            'img': paginates.items[i].img,
            'cate': paginates.items[i].cate,
            'author': paginates.items[i].author,
            'size':paginates.items[i].size,
            'date':paginates.items[i].date,
            'down':paginates.items[i].down,
            'listT':listT[i],
            'listL':listL[i],
            'listH':listH[i]
        }
        yanqing.append(con)
    map['yanqing'] = yanqing
    return json.dumps(map)

@app.route("/wuxia_api/<int:page>/<int:per_page>/")
def wuxia_api(page,per_page):
    paginates = WuXiaBooks.query.order_by(WuXiaBooks.id).paginate(page=page, per_page=per_page, error_out=False)
    map = {'has_next': paginates.has_next}
    yanqing = []
    for i in range(len(paginates.items)):
        con = {
            'id': paginates.items[i].id,
            'title': paginates.items[i].title,
            'img': paginates.items[i].img,
            'cate': paginates.items[i].cate,
            'author': paginates.items[i].author,
            'size':paginates.items[i].size,
            'date':paginates.items[i].date,
            'down':paginates.items[i].down,
            'listT':listT[i],
            'listL':listL[i],
            'listH':listH[i]
        }
        yanqing.append(con)
    map['yanqing'] = yanqing
    return json.dumps(map)

@app.route("/lishi_api/<int:page>/<int:per_page>/")
def lishi_api(page,per_page):
    paginates = LiShiBooks.query.order_by(LiShiBooks.id).paginate(page=page, per_page=per_page, error_out=False)
    map = {'has_next': paginates.has_next}
    yanqing = []
    for i in range(len(paginates.items)):
        con = {
            'id': paginates.items[i].id,
            'title': paginates.items[i].title,
            'img': paginates.items[i].img,
            'cate': paginates.items[i].cate,
            'author': paginates.items[i].author,
            'size':paginates.items[i].size,
            'date':paginates.items[i].date,
            'down':paginates.items[i].down,
            'listT':listT[i],
            'listL':listL[i],
            'listH':listH[i]
        }
        yanqing.append(con)
    map['yanqing'] = yanqing
    return json.dumps(map)

@app.route("/xuanyi_api/<int:page>/<int:per_page>/")
def xuanyi_api(page,per_page):
    paginates = XuanYiBooks.query.order_by(XuanYiBooks.id).paginate(page=page, per_page=per_page, error_out=False)
    map = {'has_next': paginates.has_next}
    yanqing = []
    for i in range(len(paginates.items)):
        con = {
            'id': paginates.items[i].id,
            'title': paginates.items[i].title,
            'img': paginates.items[i].img,
            'cate': paginates.items[i].cate,
            'author': paginates.items[i].author,
            'size':paginates.items[i].size,
            'date':paginates.items[i].date,
            'down':paginates.items[i].down,
            'listT':listT[i],
            'listL':listL[i],
            'listH':listH[i]
        }
        yanqing.append(con)
    map['yanqing'] = yanqing
    return json.dumps(map)

@app.route("/tongren_api/<int:page>/<int:per_page>/")
def tongren_api(page,per_page):
    paginates = TongRenBooks.query.order_by(TongRenBooks.id).paginate(page=page, per_page=per_page, error_out=False)
    map = {'has_next': paginates.has_next}
    yanqing = []
    for i in range(len(paginates.items)):
        con = {
            'id': paginates.items[i].id,
            'title': paginates.items[i].title,
            'img': paginates.items[i].img,
            'cate': paginates.items[i].cate,
            'author': paginates.items[i].author,
            'size':paginates.items[i].size,
            'date':paginates.items[i].date,
            'down':paginates.items[i].down,
            'listT':listT[i],
            'listL':listL[i],
            'listH':listH[i]
        }
        yanqing.append(con)
    map['yanqing'] = yanqing
    return json.dumps(map)