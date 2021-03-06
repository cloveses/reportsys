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
        response.set_cookie('info','',secret=secret)
        return template('tpls/index.tpl', info=info)

    elif request.method == 'POST':
        verify_text = request.get_cookie('verify_text',secret=secret)
        response.set_cookie('verify_text','',secret=secret)
        if verify_text and verify_text.lower() == \
            request.forms.getunicode('verify_text').lower().strip():
            tel = request.forms.getunicode('tel')
            keys = ('machine_name','name','fault')
            params = get_params(keys)
            if models.verify(params['name'],tel):
                rid = models.add_recorder(params)
                if rid:
                    redirect('/recorder/' + str(rid))
                else:
                    response.set_cookie('info',"提交失败！",secret=secret)
                    redirect('/')
            else:
                response.set_cookie('info',"用户不存在！",secret=secret)
                redirect('/')
        else:
            response.set_cookie('info',"验证码错误，请重新登录！",
                secret=secret)
            redirect('/')

@app.route('/recorder/<rid:int>',method=["GET",])
def get_recorder(rid=0):
    info = request.get_cookie('info',secret=secret)
    if rid:
        r = models.get_recorder(rid)
        if r:
            response.set_cookie('info',"提交成功，请勿重复申请！",
                secret=secret)

            return template('tpls/rid.tpl',**r.to_dict(),info=info)
        else:
            response.set_cookie('info',"查询失败！",
                secret=secret)
            redirect('/')

@app.route('/mgr',method=["GET",])
@app.route('/mgr/<page:int>',method=["GET",])
def mgr(page=0):
    info = request.get_cookie('info',secret=secret)
    if page > 0:
        page -= 1
    pages,res = models.get_pages(page)
    print(pages)
    return template('tpls/mgr.tpl',res=res,info=info,pages=pages)

if __name__ == '__main__':
    models.add_user()
    run(app, host='localhost', port=8080, debug=True)