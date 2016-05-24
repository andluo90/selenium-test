# -*- encoding:utf-8 -*-
import logging

# create logger
log = logging.getLogger('testLogger')
log.setLevel(logging.INFO)

# create file handler
log_path = "./log/log.log"
fh = logging.FileHandler(log_path)

# create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d  %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

# add handler and formatter to log
fh.setFormatter(formatter)
log.addHandler(fh)

log.info("==========================")

