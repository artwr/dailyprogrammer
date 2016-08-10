from setuptools import setup, find_packages

setup(
    name='dailyprogrammer',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'praw',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        dailyprog=dailyprogrammer.bin.dailyprogrammer:cli
    ''',
)