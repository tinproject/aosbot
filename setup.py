from setuptools import setup


setup(
    name='aosbot',
    version='0.0.1dev',
    packages=['aosbot', 'aosbot.tg'],
    author='Agustín Herranz',
    description='AWS Lambda functions for a Telegram Bot',

    package_data={},
    include_package_data=True,
    classifiers=[
        "Dumb :: Do Not Upload"
    ],
    install_requires=[]
)
