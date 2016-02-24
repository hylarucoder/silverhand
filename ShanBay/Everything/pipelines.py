# -*- coding: utf-8 -*-
#设置默认编码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
conn_string = "host='localhost' dbname='shanbaydb' user='twocucao' password=''"
class EverythingPipeline(object):

    def process_item(self, item, spider):
        return item


class ShanbayPipeline(object):



    def __init__(self):
        self.conn = None
        dispatcher.connect(self.initialize,signals.engine_started)
        dispatcher.connect(self.finalize,signals.engine_stopped)

    def initialize(self):
        if self.conn == None:
            self.conn = psycopg2.connect(conn_string)
            pass
        self.cur = self.conn.cursor()

    def create_database(self):

        pass
    def process_item(self, item, spider):

        # self.cur.execute("SELECT * FROM shanbay_user")
        # print self.cur.fetchall()

        # print item
        insert_user_sql  = 'INSERT INTO shanbay_user \
                          ( user_id, username, nickname, growth_stat, words_count, words_learned_count,\
                          words_learning_count, words_new_count, checkin_days_count)\
                          values ( %d , \'%s\' , \'%s\', %d , %d , %d , %d , %d , %d)'\
                          % ( item['user_id'] ,item['username'] ,item['nickname'] ,item['growth_stat'] ,item['words_count'] ,item['words_learned_count'],\
                             item['words_learning_count']  ,item['words_new_count']  ,item['checkin_days_count'])
        print(insert_user_sql)
        try:
            self.cur.execute(insert_user_sql)
            self.conn.commit()
        except Exception :
            self.conn.rollback()

        return item

    def finalize(self):

        if self.conn is not None:
            self.cur.close()
            self.conn.commit()
            self.conn.close()
            self.conn=None
