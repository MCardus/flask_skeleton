from distutils.core import setup

setup(
    name='flask_api',
    version='0.1',
    author='MCardus',
    packages=['api'],
    license='LICENSE.txt',
    description='Flask skeleton',
    long_description=open('README.md').read(),
    install_requires=["Flask,PyYAML"]
)
