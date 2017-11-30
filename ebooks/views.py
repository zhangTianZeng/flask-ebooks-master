#coding:utf-8
from ebooks import app
from flask import render_template
from models import *
listT = [0,0,0,0,576,616,642,643,1228,1229,1256,1272]
listL = [0,250,500,750,250,0,750,500,250,0,500,750]
listH =[338,333,327,332,339,335,317,338,320,318,342,340]

@app.route("/")
def index():
    paginate = YanQingBooks.query.order_by(YanQingBooks.id).paginate(
        page=1, per_page=12,error_out=False)
    return render_template('index.html',all_books=paginate.items, has_next=paginate.has_next,listT=listT,listL=listL,listH=listH)

@app.route("/dushi/")
def dushi():
    paginate = DuShiBooks.query.order_by(DuShiBooks.id).paginate(
        page=1, per_page=12,error_out=False)
    return render_template('dushi.html',all_books=paginate.items, has_next=paginate.has_next,listT=listT,listL=listL,listH=listH)

@app.route("/gengmei/")
def gengmei():
    paginate = GengMeiBooks.query.order_by(GengMeiBooks.id).paginate(
        page=1, per_page=12,error_out=False)
    return render_template('gengmei.html',all_books=paginate.items, has_next=paginate.has_next,listT=listT,listL=listL,listH=listH)

@app.route("/chuanyue/")
def chuanyue():
    paginate = ChuanYueBooks.query.order_by(ChuanYueBooks.id).paginate(
        page=1, per_page=12,error_out=False)
    return render_template('chuanyue.html',all_books=paginate.items, has_next=paginate.has_next,listT=listT,listL=listL,listH=listH)

@app.route("/xuanhuan/")
def xuanhuan():
    paginate = XuanHuanBooks.query.order_by(XuanHuanBooks.id).paginate(
        page=1, per_page=12,error_out=False)
    return render_template('xuanhuan.html',all_books=paginate.items, has_next=paginate.has_next,listT=listT,listL=listL,listH=listH)

@app.route("/wangyou/")
def wangyou():
    paginate = WangYouBooks.query.order_by(WangYouBooks.id).paginate(
        page=1, per_page=12,error_out=False)
    return render_template('wangyou.html',all_books=paginate.items, has_next=paginate.has_next,listT=listT,listL=listL,listH=listH)

@app.route("/wuxia/")
def wuxia():
    paginate = WuXiaBooks.query.order_by(WuXiaBooks.id).paginate(
        page=1, per_page=12,error_out=False)
    return render_template('wuxia.html',all_books=paginate.items, has_next=paginate.has_next,listT=listT,listL=listL,listH=listH)

@app.route("/lishi/")
def lishi():
    paginate = LiShiBooks.query.order_by(LiShiBooks.id).paginate(
        page=1, per_page=12,error_out=False)
    return render_template('lishi.html',all_books=paginate.items, has_next=paginate.has_next,listT=listT,listL=listL,listH=listH)

@app.route("/xuanyi/")
def xuanyi():
    paginate = XuanYiBooks.query.order_by(XuanYiBooks.id).paginate(
        page=1, per_page=12,error_out=False)
    return render_template('xuanyi.html',all_books=paginate.items, has_next=paginate.has_next,listT=listT,listL=listL,listH=listH)

@app.route("/tongren/")
def tongren():
    paginate = TongRenBooks.query.order_by(TongRenBooks.id).paginate(
        page=1, per_page=12,error_out=False)
    return render_template('tongren.html',all_books=paginate.items, has_next=paginate.has_next,listT=listT,listL=listL,listH=listH)
