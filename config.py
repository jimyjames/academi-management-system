import os

class Config():
    SECRET_KEY = '1a2b3c4d5e'
   
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config): 
    SQLALCHEMY_DATABASE_URI= 'sqlite:///blog.db'


config={
        "development":DevelopmentConfig,
        "default": DevelopmentConfig
        }