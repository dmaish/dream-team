class Config(object):
    """common configurations that are common across all environments"""

    DEBUG = True


class DevelopmentConfig(Config):
    """Development configurations"""

    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """production configurations"""

    DEBUG = False


class TestingConfig(Config):
    """ Testing configurations """
    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
    }
