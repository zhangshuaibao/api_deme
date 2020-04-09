import logging

from logging import handlers

from setting import LOG_PATH


def init_logging():
    # 1 初始化日志器
    logger = logging.getLogger()
    # 2 设置日志等级
    logger.setLevel(logging.INFO)
    # 3 创建控制处理器
    sh = logging.StreamHandler()
    # 4 创建文件处理器
    fh = logging.handlers.TimedRotatingFileHandler(filename=LOG_PATH, when='D', interval=1, backupCount=7,
                                                   encoding='utf-8')
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s %(funcName)s:%(lineno)d] - [%(message)s]"
    formatter = logging.Formatter(fmt)
    # 6 将格式化器添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 7 将处理器添加到日志
    logger.addHandler(sh)
    logger.addHandler(fh)


if __name__ == '__main__':
    init_logging()
    logging.info('——————————————你2020必暴富——————————————————')
