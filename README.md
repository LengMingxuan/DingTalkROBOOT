# DingTalkROBOOT
最简易的钉钉群机器人，只听过发送内容的建议SKD(独立可运行)

![](https://img.shields.io/badge/DingTalk-PC%205.1.11-blue)

### 使用方法
讲此项目zip下载并解压，云翔压缩包内的Main.py文件即可。可根据下方的消息类型更改机器人的消息类型。本项目只提供钉钉群机器人最主要的发送接口，更多新鲜好玩的功能等待各位自行开发。

### 消息类型及数据格式
#### text类型
```python
{
    "msgtype": "text", 
    "text": {
        "content": "我就是我, 是不一样的烟火@156xxxx8827"
    }, 
    "at": {
        "atMobiles": [
            "156xxxx8827", 
            "189xxxx8325"
        ], 
        "isAtAll": false
    }
}
```
| 参数        | 参数类型    | 必须 | 说明                         |
|-----------|---------|----|----------------------------|
| msgtype   | String  | 是  | 消息类型，此时固定为：text            |
| content   | String  | 是  | 消息内容                       |
| atMobiles | Array   | 否  | 被@人的手机号（在content里添加@人的手机号） |
| isAtAll   | Boolean | 否  | 是否@所有人                     |

![1](https://img.alicdn.com/tfs/TB1jFpqaRxRMKJjy0FdXXaifFXa-497-133.png)

#### link类型
```python
{
    "msgtype": "link", 
    "link": {
        "text": "这个即将发布的新版本，创始人xx称它为红树林。而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是红树林", 
        "title": "时代的火车向前开", 
        "picUrl": "", 
        "messageUrl": "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI"
    }
}
```
| 参数         | 参数类型   | 必须 | 说明              |
|------------|--------|----|-----------------|
| msgtype    | String | 是  | 消息类型，此时固定为：link |
| title      | String | 是  | 消息标题            |
| text       | String | 是  | 消息内容。如果太长只会部分展示 |
| messageUrl | String | 是  | 点击消息跳转的URL      |
| picUrl     | String | 否  | 图片URL           |

#### markdown类型
```python
{
     "msgtype": "markdown",
     "markdown": {
         "title":"杭州天气",
         "text": "#### 杭州天气 @150XXXXXXXX \n> 9度，西北风1级，空气良89，相对温度73%\n> ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n> ###### 10点20分发布 [天气](https://www.dingtalk.com) \n"
     },
      "at": {
          "atMobiles": [
              "150XXXXXXXX"
          ],
          "isAtAll": false
      }
 }
 ```
 | 参数        | 类型      | 必选 | 说明                      |
|-----------|---------|----|-------------------------|
| msgtype   | String  | 是  | 此消息类型为固定markdown        |
| title     | String  | 是  | 首屏会话透出的展示内容             |
| text      | String  | 是  | markdown格式的消息           |
| atMobiles | Array   | 否  | 被@人的手机号（在text内容里要有@手机号） |
| isAtAll   | Boolean | 否  | 是否@所有人                  |

 **说明：目前只支持md语法的子集，具体支持的元素如下：**
 ```markdown
 标题
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题

引用
> A man who stands for nothing will fall for anything.

文字加粗、斜体
**bold**
*italic*

链接
[this is a link](http://name.com)

图片
![](http://name.com/pic.jpg)

无序列表
- item1
- item2

有序列表
1. item1
2. item2
```
 
