from urllib import parse, request
import json
def ding_api(contents):
    url = "https://oapi.dingtalk.com/robot/send?access_token=15c55f69a3f07b470c72513ab70336f7f4264f2496d4df266e91e1c4a9d3ac0c"

    postdata = json.dumps({
        "msgtype": "markdown",
     "markdown": {
         "title":"【网小工】英语IV成绩可查询",
         "text": " #### 英语IV成绩教务系统开放查询~\n> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n> 今天是暑假的第6天，离暑假结束还有36天！\n各位同学，如果发现今日校园没有按时推送，请在上午等待app推送通知再及时填写，健康打卡没有特出情况会一直有的，**每天都需要填写哦~** \n> ![五四广场夜景](http://www.lengmingxuan.top/wp-content/uploads/2019/12/timg-scaled.jpeg)\n> ###### 问候不一定要慎重其事，但一定要真诚感人。[临沂大学](https://www.lyu.edu.cn/) \n"
     },
        "at": {
            "atMobiles": [

            ],
            "isAtAll": True  # @所有人时：true，否则为：false
        }
    }).encode('utf-8')

    req = request.Request(url=url, data=postdata)
    req.add_header('Content-Type', 'application/json')
    r = request.urlopen(req)
    r_data = r.read().decode('utf-8')
    return r_data


if __name__ == "__main__":
    a = ding_api("我就是我，一个特立独行的我")
    print(a)



