class Config():
    DEBUG = False

class Dev_config(Config):
    DEBUG = True
    
class Prod_config(Config):
    pass

config_options = {
    'development':Dev_config,
    'production':Prod_config
}