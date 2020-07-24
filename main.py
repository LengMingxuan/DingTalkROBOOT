from urllib import parse, request
import json
def ding_api(contents):
    url = "https://oapi.dingtalk.com/robot/send?access_token=15c55f69a3f07b470c72513ab70336f7f4264f2496d4df266e91e1c4a9d3ac0c"

    postdata = json.dumps({
        "msgtype": "markdown",
     "markdown": {
         "title":"【网小工】周末到了~",
         "text": "#### 放假第一个周结束了~\n> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n> 今天是暑假的第7天，离暑假结束还有35天！\n周末准备去哪玩？忙碌了一个周的你该找个好吃的地方犒劳一下自己了～！ ![大学英语4](http://www.lengmingxuan.top/wp-content/uploads/2019/12/contact.jpg)\n> ###### 网工小天地 Trello 已上线，快来看看吧[网工小天地](https://trello.com/b/eNxnmgzT) \n"
     },
        "at": {
            "atMobiles": [

            ],
            "isAtAll": False  # @所有人时：true，否则为：false
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



