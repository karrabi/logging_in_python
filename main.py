import datetime
import logging as lg
import logging.config


def initLogging():
    filename = datetime.datetime.now().strftime('./logs/log_%Y_%m_%d__%H_%M_%S.log')
    lg.config.fileConfig('log.config', disable_existing_loggers=False, defaults={'logfilename': filename})
    lg.debug('Logging initialized successfully')


def main():
    initLogging()
    lg.info("Program Started...")


if __name__ == '__main__':
    main()