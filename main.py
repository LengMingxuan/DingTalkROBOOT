from urllib import parse, request
import json
def ding_api(contents):
    url = "https://oapi.dingtalk.com/robot/send?access_token=****"

    postdata = json.dumps({
        "msgtype": "markdown",
     "markdown": {
         "title":"【网小工】英语IV成绩可查询",
         "text": " #### 英语IV成绩教务系统开放查询~\n> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n> 今天是暑假的第5天，离暑假结束还有37天！\n大学英语IV成绩已在教务系统公布，但未推送，同学们可点击下方蓝字手动查询~ ![大学英语4](https://courseres.sflep.com/resource/images/course/2bdc0feac5d14a1bb8c19f3f11aaed87.jpg)\n> ###### 点击右侧“蓝字”查询英语成绩(超级课程表提供支持)[成绩查询](https://score.super.cn/Score/score.html?schoolIdentity=50FC9CD6FAA8855F91F425302C07C1E7&identity=7F59C830687546D012962F1661C94862) \n"
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



