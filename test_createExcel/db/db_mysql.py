
#-*- coding:utf-8 -*-
import os
import sys
import logging.config
sys.path.append(r'C:\Users\Administrator\Desktop\Python_code\czy\test\test_createExcel')
# setting = __import__(os.path.basename(os.path.abspath('..')), globals(), locals(), ['LOGGING'])
from collections import OrderedDict
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
				host=setting.mysql_config['host'],
				user=setting.mysql_config['user'],
				passwd=setting.mysql_config['passwd'],
				port=setting.mysql_config['port'],
				charset=setting.mysql_config['charset'],
				db=setting.mysql_config['db']
			)
		except Exception as e:
			logger.error(e)

	def query_sql(self, sql):
		try:
			cur = self.__conn.cursor()
			cur.execute(sql)
		except Exception as e:
			logger.error(e)
		try:
			dbfield = tuple([field[0] for field in cur.description]) # description 返回的为一个tuple 每个元素也为 tuple，每个tuple的第一个元素为数据的字段名
			query_result = cur.fetchall() # 返回一次查询的所有结果
		except Exception as e:
			logger.info(e, sql)
		cur.close() #
		return dbfield, query_result

	def __del__(self):
		return
		try:
			self.__conn.close()
		except Exception as e:
			pass


if __name__ == "__main__":
	dbfield, dbdata = ExcuteSql().query_sql('select username,flag,gameid,id,reg_time,agent,imeil from cy_members limit 2')
	print(dbfield,dbdata)
	print(dbfield,zip(*dbdata))

	print(OrderedDict(zip(dbfield,zip(*dbdata)))['username'])  # 将数据 解析成 field_name: db_field_data
	dict_data = {}.fromkeys(dbfield, [])
	for field_index in range(len(dbfield)):
		for data in dbdata:
			dict_data[dbfield[field_index]].append(data[field_index])

	print('dict_data-->', dict_data)

	data1 = {
		field: d for field in dbfield for data in dbdata for d in data
	}
	print("--->", data1)
	# print(sys.path)
	# print(os.path.basename(os.path.abspath('..')))
	# print(setting.LOGGING)
