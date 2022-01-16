import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('.\\Logs\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        #logging.basicConfig(filename="C:\\Users\\hp\\PycharmProjects\\E2E_NOPCommerce\\LogsLogs\\newfile.txt",
         #                   format='%(asctime)s %(message)s',
         #                   filemode='w')
        #logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
