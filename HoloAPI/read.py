import configparser

config = configparser.ConfigParser()
config.read("secret.ini")


class Conf():
    def __init__(self):
        self.USER = config["Config"]["USER"]
        self.NAME = config["Config"]["NAME"]
        self.PASSWORD = config["Config"]["PASSWORD"]
        self.HOST = config["Config"]["HOST"]
        self.PORT = config["Config"]["PORT"]

config_data = Conf()