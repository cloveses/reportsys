% rebase('tpls/base.tpl')
    <h3 style="text-align: center;">报修列表</h3>
<table  class="pure-table pure-table-bordered"  style='margin:0 auto;'>
    <tr><td>申请编号</td><td>设备名称</td><td>故障描述</td><td>报修时间</td><td>报 修 人</td></tr>
        %for r in res:
    <tr>
            <td>{{r.id}}</td>
            <td>{{r.machine_name}}</td>
            <td>{{r.fault}}</td>
            <td>{{r.date_time}}</td>
            <td>{{r.name}}</td>
    </tr>
        %end
</table>
<div style="text-align: center;" >
%for i in pages:
<a href="/mgr/{{i}}">第{{i}}页</a>
%end
</div>


