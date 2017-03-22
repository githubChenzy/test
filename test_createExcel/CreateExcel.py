
#-*- coding:utf-8 -*-

import os
import time
import logging
import logging.config
from openpyxl import Workbook

import setting

logging.config.dictConfig(setting.LOGGING)
logger = logging.getLogger('mylogger')


class RegisterList(object):

	def __init__(self):
		self.wb = Workbook()
		self.sheetName = self.setSheetname()
		self.fieldNameMap = self.setFieldNameMap()
		self.initializeSheet()
		self.setTitle(self.fieldNameMap.keys())
		self.finish()

	def setSheetname(self):
		return u'用户注册表'

	def setFieldNameMap(self):
		return {
			'username': u'注册账号',
			'flag': u'账号状态',
			'reg_time': u'注册时间',
			'imeil': u'IMEI码',
			'reg_time': u'创建时间',
			'gameid': u'游戏',
			'agent': u'渠道名称',   # 使用 cy_department表中去查询顶级渠道名
			'channel_id': u'顶级渠道',
			# 'id': {
			'status': u'支付状态',
			'login_time': u'最后一次登录时间',
			'count(id)': u'累计充值次数',
			'sum(amount)': u'累计充值金额',
			# }
		}

	def createPage(self, data, dbfield):
		pass

	def create(self):
		pass

	def initializeSheet(self):
		self.ws = self.wb.create_sheet(
			self.sheetName,
			0
		)

	def setTitle(self, dbfield):
		title_row = []
		print("dbfield", dbfield)
		for field in dbfield:
			if field in self.fieldNameMap:
				title_row.append(self.fieldNameMap.get(field))

		self.ws.append(title_row)

	@staticmethod
	def create_reportDir(path):
		if not os.path.isdir(path):
			os.mkdir(path)

	def finish(self):
		report_dir = os.path.join(os.path.dirname(__file__), 'report')
		self.create_reportDir(report_dir)
		filename = str(int(time.time())) + '.xlsx'
		self.wb.save(os.path.join(report_dir, filename))

if __name__ == "__main__":
	RegisterList()
	print("he")
