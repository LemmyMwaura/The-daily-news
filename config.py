from distutils.debug import DEBUG

import os
class Config():
    api_key = os.environ.get('NEWS_API_KEY')
    DEBUG = False

class Dev_config(Config):
    DEBUG = True
    
class Prod_config(Config):
    pass

config_options = {
    'development':Dev_config,
    'production':Prod_config
}