
#-*- coding:utf-8 -*-

import os
import logging


LOGGING = {
	
	'version': 1,
	'formatters': {
		'fmt': {
			'datafmt': '%Y-%m-%d %H:%M:%S',
			'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
		}
	},
	'handlers'; {
		'console': {
			'class': 'logging.StringHandler',
			'level': 'logging.DEBUG',
			'formatter': 'fmt',
		},
		'error':{
			'class': 'logging.RotatingFileHandler',
			'level': 'logging.DEBUG',
			'encoding': 'utf-8',
			'maxBytes': 1024 * 10,
			'formatter': 'fmt',
		},


	},
	'mylogger': {

	}

}


if __name__ == '__main__':
	print('github ')