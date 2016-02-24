# -*- coding: utf-8 -*-
import scrapy
import random
from Everything.items import ShanbayItem
from Everything.misc.proxy import PROXIES
import re

TAG_RE = re.compile(r'<[^>]+>')

URL = 'http://www.shanbay.com/bdc/review/progress/%d'

# 279
# ======== 1 ==========
# 1489
start_user_id = 948653
end_user_id= 1111111

# ======== 2 ==========
#
# start_user_id = 14249245
# end_user_id= 24249245

# ======== 3 ==========
#
# start_user_id = 24249245
# end_user_id= 34249245

# 35000000
#35249245


class ShanbaySpider(scrapy.Spider):
    name = "shanbay"
    allowed_domains = ["shanbay.com"]

    def __init__(self):
        self.current = start_user_id

    def start_requests(self):
        for i in range(start_user_id,end_user_id):
            request = scrapy.Request(URL % i,self.parse_item)
            request.meta['proxy'] = "http://"+PROXIES[random.randint(0,len(PROXIES)-1)]
            yield request

    def parse_item(self, response):
        # print response.url
        # 已经可以完成正常的数据抓取
        # 两个name都获取不到则不是用户界面

        sel = response
        item =  ShanbayItem()

        user_id = response.url
        user_id = user_id[user_id.find("ress/")+5:]
        user_id = int(user_id)

        username = sel.css("#profile div.profile h2 small").extract()
        if len(username) == 0:
            return
        username = username[0]
        username = username[username.find("(")+1:username.find(")")]


        nickname = sel.css("#profile div.profile h2").extract()
        if len(nickname) == 0:
            return
        nickname = nickname[0]
        nickname = nickname[4:nickname.find("<small>")]


        growth_stat = sel.css("#profile div.profile a").extract()
        if len(growth_stat) == 0:
            growth_stat = -1
            pass
        else:
            growth_stat = growth_stat[0]
            growth_stat = growth_stat[growth_stat.find("title=")+11:growth_stat.find("\"><span")]
            if growth_stat == "":
                growth_stat = -1
                pass
            growth_stat = int(growth_stat)

        words_count_list = sel.css("#total-stats span span").extract()
        if len(words_count_list) == 0:
            words_count_list = -1
            pass
        else:
            words_count = words_count_list[0]
            words_count = self.remove_tags(words_count)
            if words_count == "":
                words_count = 0
                pass
            words_count = int(words_count)

        words_learned_count = words_count_list[1]
        words_learned_count = self.remove_tags(words_learned_count)
        if words_learned_count == "":
            words_learned_count = 0
            pass
        words_learned_count = int(words_learned_count)

        words_learning_count = words_count_list[2]
        words_learning_count = self.remove_tags(words_learning_count)
        if words_learning_count == "":
            words_learning_count = 0
            pass
        words_learning_count = int(words_learning_count)

        words_new_count = words_count_list[3]
        words_new_count = self.remove_tags(words_new_count)
        if words_new_count == "":
            words_new_count = 0
            pass
        words_new_count = int(words_new_count)

        checkin_days_count = sel.css("#profile-container > ul:nth-child(4) > li:nth-child(2) > a").extract()[0]
        # print checkin_days_count
        if len(checkin_days_count) == 0:
            checkin_days_count = -1;
            pass
        else:
            # print repr(checkin_days_count)
            checkin_days_count = re.search('卡\\((\d+?)天', str(checkin_days_count)).group(1)
            # print checkin_days_count
            if checkin_days_count == "":
                checkin_days_count = 0
                pass
            checkin_days_count = int(checkin_days_count)

        item['user_id'] = user_id
        item['username'] = username
        item['nickname'] = nickname
        item['growth_stat'] = growth_stat
        item['words_count'] = words_count
        item['words_learned_count'] = words_learned_count
        item['words_learning_count'] = words_learning_count
        item['words_new_count'] = words_new_count
        item['checkin_days_count'] = checkin_days_count

        print "request user " + "---" +str(user_id)+ "---"+username


        yield item


    def remove_tags(self,text):
        return TAG_RE.sub('', text)


