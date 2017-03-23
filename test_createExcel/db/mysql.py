
#-*- coding:utf-8 -*-
import os
import sys
import logging.config
sys.path.append(r'C:\Users\Administrator\Desktop\Python_code\czy\test\test_createExcel')
# setting = __import__(os.path.basename(os.path.abspath('..')), globals(), locals(), ['LOGGING'])

try:
	import MySQLdb
except Exception as e:
	import pymysql as MySQLdb

import setting


logging.config.dictConfig(setting.LOGGING)
logger = logging.getLogger('mylogger')


def Singleton(cls, *args, **kwargs):
	instance = {}
	def _signle():
		if cls not in instance:
			instance[cls] = cls(*args, **kwargs)
		return instance[cls]
	return _signle


@Singleton
class ExcuteSql(object):

	def __init__(self):
		self.__connect()

	def __connect(self):
		try:
			self.__conn = MySQLdb.connect(
				host=setting.mysql_conf['host'],
				user=setting.mysql_conf['user'],
				passwd=setting.mysql_conf['passwd'],
				port=setting.mysql_conf['port'],
				charset=setting.mysql_conf['charset'],
				db=setting.mysql_conf['db']
			)
		except Exception as e:
			logger.error(e)

	def query_sql(self, sql):
		try:
			cur = self.__conn.cursor()
			cur.execute(sql)
		except Exception as e:
			logger.error(e)
		dbfelfd = tuple([field[0] for field in cur.description]) # description 返回的为一个tuple 每个元素也为 tuple，每个tuple的第一个元素为数据的字段名
		print(dbfelfd)
		query_result = cur.fetchall() # 返回一次查询的所有结果
		cur.close() #
		return dbfelfd, query_result

	def __del__(self):
		return
		try:
			self.__conn.close()
		except Exception as e:
			pass


if __name__ == "__main__":
	print(ExcuteSql().query_sql('select username,flag,gameid,id,reg_time,agent,imeil from cy_members limit 2'))
	# print(sys.path)
	# print(os.path.basename(os.path.abspath('..')))
	# print(setting.LOGGING)
