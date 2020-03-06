# -*- encoding: utf-8 -*-
'''
@File    :   LoggingUtil.py
@Time    :   2020/03/05 09:54:28
@Author  :   peace_su
@Version :   1.0
@Contact :   peace_su@163.com
@WebSite :   https://me.csdn.net/u010098760
'''

# here put the import lib
import yaml
import logging.config
import os



class LoggingUtil(object):
    '''类注释
    详细描述

    Attributes:
        属性说明
    '''

    def __init__(self):
        '''Class1类初始化方法

        Args:
            paramter1: 入参说明
            paramter2: 入参说明
        '''
        pass

    def setup_logging(self, default_path='config/logging.yaml', default_level=logging.INFO):
        '''Setup logging configuration
        方法描述

        Args:
        paramter1: 入参说明
        paramter2: 入参说明

        Returns:
            返回描述

        Raises:
            抛出异常说明
        '''
        if os.path.exists('mylog'):
            pass
        else:
            os.mkdir('mylog')
        path = default_path
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
            logger = logging.getLogger()
            logger.error('未找到config/logging.yaml文件，请检查！')


if __name__ == '__main__':
    LoggingUtil.setup_logging(LoggingUtil)
    logger = logging.getLogger()
    logger.info('123')
