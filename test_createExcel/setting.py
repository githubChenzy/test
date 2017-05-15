
#-*- coding:utf-8 -*-

import os
import logging
import logging.config

mysql_config = dict(
	host='xxxx',
	user='xxxx',
	passwd='xxxx',
	port=xxxx,
	db='xxxxx',
	charset='xxxx',
)

log_path = os.path.join(os.path.dirname(__file__), 'log')
print(log_path)

def create_log_dir(path):
	if not os.path.isdir(path):
		os.mkdir(path)

def create_log_file(path, filename):
	create_log_dir(path)
	return os.path.join(path, filename)

LOGGING = {
	'version': 1,  # 必须为 整型 1
	'disable_existing_loggers': True,
	'formatters': {   # 配置格式
		'fmt_error': {
			'datefmt': '%Y-%m-%d %H:%M:%S',
			'format': '%(asctime)s %(message)s'
		},
		'fmt': {
			# 'datefmt': '%Y-%m-%d %H:%M:%S',
			'datefmt': '%a, %b %Y %m %d %H:%M:%S',
			'format': '%(asctime)s [level: %(levelname)s] [filename: %(filename)s] [line: %(lineno)s]: %(message)s'
		}
	},
	'handlers': {  # 各种handler的一些配置参数
		'null': {
			'class': 'logging.NullHandler',  # handler的类型
			'level': 'DEBUG'				# 日志等级
		},
		'console': {
			'class': 'logging.StreamHandler',
			'level': 'DEBUG',
			'formatter': 'fmt'
		},
		'errors': {
			'class': 'logging.handlers.RotatingFileHandler',
			'level': 'ERROR',
			'filename': create_log_file(log_path, 'error.log'),
			'formatter': 'fmt',
			'encoding': 'utf-8',
			'maxBytes': 1024 * 1024 * 10,
			'backupCount': 5
		},
		'info': {
			'class': 'logging.handlers.RotatingFileHandler',
			'level': 'INFO',
			'filename': create_log_file(log_path, 'info.log'),
			'formatter': 'fmt',
			'encoding': 'utf-8',
			'maxBytes': 1024 * 1024 * 10,
			'backupCount': 5
		},
		'notes': {
			'class': 'logging.handlers.RotatingFileHandler',
			'level': 'DEBUG',
			'filename': create_log_file(log_path, 'all.log'),
			'formatter': 'fmt',
			'encoding': 'utf-8',
			'maxBytes': 1024 * 1024 * 10,
			'backupCount': 5
		}
	},
	'loggers': {
		'mylogger': {
			'level': 'DEBUG',
			'handlers': ['console', 'notes', 'info', 'errors'],
			'propagate': True,
		}
	}
}



if __name__ == '__main__':
	logging.config.dictConfig(LOGGING)
	logger = logging.getLogger('mylogger')
	logger.error("test logging error")
	logger.info("test logging info")

	print('github ')
