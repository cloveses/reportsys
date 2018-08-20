% rebase('tpls/base.tpl')
<form class="pure-form pure-form-stacked pure-form-aligned" action="/" method="POST">
设备名称：<input type="text" name="machine_name" size="60" placeholder="设备名称" reqired />
故障描述：<input type="text" name="fault" size="60" placeholder="故障描述" reqired />
报 修 人：<input type="text" name="name" size="60" placeholder="报修人" reqired />
联系电话：<input type="text" name="tel" size="60" placeholder="联系电话" reqired />
验 证 码：<input type="text" name="verify_text" size="6" placeholder="验证码" reqired /><img src='verify' style="display:inline" /><br/>
<input type="reset" name="reset"  class="pure-button"/>
<input type="submit" value="保存" class="pure-button  pure-button-primary" />
</form>
