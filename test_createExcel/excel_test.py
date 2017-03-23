
#-*- coding:utf-8 -*-
import os
import time
from openpyxl import Workbook

def setFieldNameMap():
	return {
		'username': u'注册账号',
		'flag': u'账号状态',
		'reg_time': u'注册时间',
		'imeil': u'IMEI码',
		'reg_time': u'创建时间',
		'gameid': u'游戏',
		'agent': u'渠道名称',  # 使用 cy_department表中去查询顶级渠道名
		# 'channel_id': '顶级渠道',
		'id': {
			'status': u'支付状态',
			'login_time': u'最后一次登录时间',
			'count(id)': u'累计充值次数',
			'sum(amount)': u'累计充值金额',
		}
	}

titleMap = setFieldNameMap()
title_name = titleMap.keys()

def createSheet(wb, sheetName):
    ws = wb.create_sheet(
        unicode(sheetName),
        0
    )
    return ws

def setSheetName():
    return u"用户注册表"

def setTitle(ws, title_name):
    title_row = []

    for key in title_name:
        if key == 'id':
            id_title = titleMap.get(key).values()
            for val in id_title:
                title_row.append(val)
        else:
            title_row.append(unicode(titleMap.get(key)))

    ws.append(title_row)

doc_dir = os.path.join(os.path.dirname(__file__), 'report')
print('report dir', doc_dir)

def createDocDir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def createReportFile(path):
    if not os.path.isdir(path):
        createDocDir(path)
    filename = str(int(time.time())) + '.xlsx'
    return os.path.join(path, filename)


if __name__ == '__main__':
    wb = Workbook()
    ws = createSheet(wb, setSheetName())
    setTitle(ws, title_name)
    wb.save(createReportFile(doc_dir))
