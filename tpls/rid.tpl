% rebase('tpls/base.tpl')
<h3 style="text-align: center;">报修信息</h3>
<table class="pure-table pure-table-bordered"  style='margin:0 auto;'>
    <tr><td>申请编号：</td><td>{{id}}</td></tr>
    <tr><td>设备名称：</td><td>{{machine_name}}</td></tr>
    <tr><td>故障描述：</td><td>{{fault}}</td></tr>
    <tr><td>报修时间：</td><td>{{date_time}}</td></tr>
    <tr><td>报 修 人：</td><td>{{name}}</td></tr>
</table>
