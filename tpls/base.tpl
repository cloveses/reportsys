<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <script language="javascript" type="text/javascript" src="/static/jquerymin.js"></script>
    <link rel="stylesheet" type="text/css" href="/static/main.css" />
    <link rel="stylesheet" type="text/css" href="/static/purecss/base-min.css" />
    <link rel="stylesheet" type="text/css" href="/static/purecss/pure-min.css" />
    <title>故障报修系统</title>
</head>
<body style="background-color:#FFF;">
<div class="pure-g" style="text-align: center;color: green;">
    <div  class="pure-u-1-1">
        <h2>宿州环保工程学校 故障报修系统</h2>
    </div>
</div>

<div class="pure-g">
    <div  class="pure-u-1-1" id='info'>
        %if info:
        info:{{info if info else ''}}
        %end
    </div>
</div>
    <div id='pure-g'>
        <div class="pure-u-1-5"></div>
        <div class="pure-u-3-5">
    {{!base}}
        </div>
        <div class="pure-u-1-5"></div>
    </div>
<div class="pure-g">
    <div class="pure-u-1-1" style="text-align: center;">
        <footer>&copy;2018 宿州环保工程学校 故障报修系统</footer>
    </div>
</div>
</body>
</html>