# -*- coding:utf-8 -*-

import os
from bottle import route,run,error,static_file,request,response,template,redirect
from setting import secret
from tools.verify_gen import get_verify
from bottle import Bottle
from db import models

app = Bottle()


@app.error(404)
def err(err):
    return '404'

@app.route('/static/<filename:re:.*.[js|css|jpg|jpeg|png]$>')
def get_tatic(filename):
    rootdir = './img'
    if filename.endswith('js'):
        rootdir = './js'
    if filename.endswith('css'):
        rootdir = './css'
    return static_file(filename,root=rootdir)


@app.route('/verify')
def verify():
    img,text = get_verify()
    response.set_cookie('verify_text',text,secret=secret)
    return img

def get_params(keys):
    params = {}
    for key in keys:
        params[key] = request.forms.getunicode(key)
    return params

@app.route('/',method=["GET","POST"])
def index():
    if request.method == 'GET':
        info = request.get_cookie('info',secret=secret)
        info = response.set_cookie('info','',secret=secret)
        response.set_cookie('info','',secret=secret)
        return template('tpls/index.tpl', info=info)

    elif request.method == 'POST':
        verify_text = request.get_cookie('verify_text',secret=secret)
        response.set_cookie('verify_text','',secret=secret)
        if verify_text and verify_text.lower() == \
            request.forms.getunicode('verify_text').lower().strip():
            keys = ('machine_name','name','fault')
            params = get_params(keys)
            rid = models.add_recorder(params)
            # if rid:
            #     # return(template('tpls/'))
            #     pass
            # else:
            #     response.set_cookie('info',"提交失败！",
            #         secret=secret)
            #     redirect('/')
        else:
            response.set_cookie('info',"验证码错误，请重新登录！",
                secret=secret)
            redirect('/')

@app.route('/<rid:int>',method=["GET",])
def get_recorder(plid=0):
    if plid:

    # info = request.get_cookie('info',secret=secret)
    # info = response.set_cookie('info','',secret=secret)
    # response.set_cookie('info','',secret=secret)
    # navs = level.get_next_lvls('')
    # newslist = [(nav,news.get_lvl_news(str(nav.id))[:7]) 
    #             for nav in navs]
    # activeimgs = tools.get_imgs('./activeimg/')
    # if request.method == 'GET':
        # name = request.get_cookie('name',secret=secret)
        # id = request.get_cookie('id',secret=secret)
        # return template('tpls/index.tpl')
    # elif request.method == 'POST':

# @app.route('/<plid:int>',method=["GET",])
# @app.route('/<plid:int>/<page:int>',method=["GET",])
# def pindex(plid=0,page=0):
#     info = request.get_cookie('info',secret=secret)
#     info = response.set_cookie('info','',secret=secret)
#     response.set_cookie('info','',secret=secret)
#     navs = level.get_next_lvls(plid)
#     mnewslist,sum_pages = news.get_lvl_page_news(plid,limit=20,page=page)
#     pages = tools.get_pages(sum_pages,page)
#     all_navs = [level.get_lvl(plid),]
#     newslist = [(nav,news.get_lvl_news(str(nav.id))[:7]) 
#                 for nav in navs]
#     if not navs:
#         all_navs = level.get_brother_lvls(plid)
#     else:
#         all_navs.extend(navs)
#     name = request.get_cookie('name',secret=secret)
#     id = request.get_cookie('id',secret=secret)
#     return template('tpls/more.tpl',
#         name=name,
#         id=id,
#         info=info,
#         navs=all_navs,
#         mnewslist=mnewslist,
#         pages=pages,
#         newslist=newslist,
#         plid=str(plid)
#         )


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)