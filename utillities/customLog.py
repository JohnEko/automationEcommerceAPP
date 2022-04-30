import logging

class Loggen:

    @staticmethod
    def logger():
        logging.basicConfig(filename=".\\Logs\\testautomation.log",
                     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

