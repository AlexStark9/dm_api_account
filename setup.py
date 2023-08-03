from distutils.core import setup
REQUIRES = [
    'structlog',
    'records',
    'allure-pytest'
]

setup(
    name='dm_api_account',
    version='0.0.1',
    packages=['dm_api_account'],
    url='https://github.com/AlexStark9/dm_api_account.git',
    license='MIT',
    author='Alex Stark',
    author_email='-',
    install_requires=REQUIRES,
    description='dm_api_account client with apis and models'
)
