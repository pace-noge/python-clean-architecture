import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base configuration"""


class ProductionConfig(Config):
    """Production config"""


class DevelopmentConfig(Config):
    """Development config"""


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True

