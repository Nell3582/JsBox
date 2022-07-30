hostname = *.snssdk.com,*.tenpay.com,api3-normal-c-*.snssdk.com,veishop.iboxpay.com,api.bigfun.cn，dkd-api.dysdk.com, api3-normal-c-*.huoshan.com, ymz.iphonezhuan.com, api.hemayoudao.cn,ranlv.lvfacn.com, api-9f9d25.sz365.cn,cf-api.douzhuanapi.cn ,wx.tiantianaiyuedu.site,play.gxhuancai.com,wn.xingguozuliao.com,api.langooo.com,.*.top,app.hubonews.com,iosvsh.zwzanwm.cn,ex.jwshq.cn,account.huami.com,www.xiaeke.com,

#腾讯自选股
https://(zqact|wzq).tenpay.com/cgi-bin/activity_sign_task.fcgi? url script-request-header https://raw.githubusercontent.com/CenBoMin/GithubSync/main/TXSTOCK/txs_cookie.js

https://wzq.tenpay.com/activity/page/welwareCenter/ url script-request-header https://raw.githubusercontent.com/CenBoMin/GithubSync/main/TXSTOCK/txs_cookie.js

https://wzq.tenpay.com/resources/vtools url script-request-header https://raw.githubusercontent.com/CenBoMin/GithubSync/main/TXSTOCK/txs_cookie.js

https://wzq.tenpay.com/cgi-bin/activity_usercenter.fcgi? url script-request-header https://raw.githubusercontent.com/CenBoMin/GithubSync/main/TXSTOCK/txs_cookie.js

#笑谱
https:\/\/veishop\.iboxpay\.com\/nf_gateway\/nf_customer_activity\/day_cash\/v1\/give_gold_coin_by_video\.json url script-request-body https://raw.githubusercontent.com/ZhiYi-N/Private-Script/master/Scripts/xp.js

#小米运动
^https:\/\/account\.huami\.com\/v2\/client\/login url script-response-body https://gitee.com/lxk0301/jd_scripts/raw/master/backUp/xmSports.js

# APP-滴滴
^https:\/\/as\.xiaojukeji\.com\/ep\/as\/toggles\? url script-request-header https://raw.githubusercontent.com/zZPiglet/Task/master/DiDi/DiDi_new.js
# WeChat-MiniApp-滴滴
^https:\/\/common\.diditaxi\.com\.cn\/webapp\/config\/sidebar\? url script-request-header https://raw.githubusercontent.com/zZPiglet/Task/master/DiDi/DiDi_new.js

^https://api.hemayoudao.cn/admin-dotask/app/spirit/v1/finish-task url script-request-header https://raw.githubusercontent.com/age174/-/main/mhdsp.js

https://ranlv.lvfacn.com/api.php/Common/pvlog url script-request-header https://raw.githubusercontent.com/ZhiYi-N/Private-Script/master/Scripts/ranlv.js

^https://api-9f9d25.sz365.cn/api/virtual_currency_v2/reward url script-request-header https://raw.githubusercontent.com/age174/-/main/sz.js

#春风转
http://cf-api.douzhuanapi.cn:10002/api/ url script-request-header https://raw.githubusercontent.com/age174/-/main/cfz.js

^http://wx.tiantianaiyuedu.site/ url script-request-body https://raw.githubusercontent.com/age174/-/main/wkzz.js
https://play.gxhuancai.com/hlplay/task/doTasks url script-request-header https://raw.githubusercontent.com/age174/-/main/hlyy.js

http://wn.xingguozuliao.com/login/login2/hydata.html url script-request-body https://raw.githubusercontent.com/age174/-/main/zqwn.js
# 朗果英语
http://api.langooo.com/task/daily/taskList url script-request-body https://raw.githubusercontent.com/age174/-/main/lgyy.js

#西梅
https://.*/.*/articles/list url script-request-body https://raw.githubusercontent.com/age174/-/main/ximei.js

#V生活
http://iosvsh.zwzanwm.cn/ url script-request-body https://raw.githubusercontent.com/age174/-/main/vsh.js

#生活圈
https://ex.jwshq.cn/app/commentator/getActivityItemPage url script-request-header https://raw.githubusercontent.com/age174/-/main/shq.js
me/MorningTree/gainEnergy? url script-request-header https://raw.githubusercontent.com/xl2101200/-/main/keep.js
>>>>>>> origin/master
