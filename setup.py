from setuptools import setup

import os

# Put here required packages or
# Uncomment one or more lines below in the install_requires section
# for the specific client drivers/modules your application needs.
packages = ['Django<=1.7',
            'static3',  # If you want serve the static files in the same server
            'mysqlclient',
            # 'mysql-connector-python',
            # 'pymongo',
            # 'psycopg2',
           ]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='Expenses', version='0.1',
      install_requires=packages,
     )
