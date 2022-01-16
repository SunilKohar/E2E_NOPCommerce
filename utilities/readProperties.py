import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig():
    @staticmethod
    def get_application_url():
        url = config.get('URL', 'baseURL')
        return url

    @staticmethod
    def get_username():
        username = config.get('URL','username')
        return username

    @staticmethod
    def get_password():
        password = config.get('URL', 'password')
        return password