# https://youtu.be/kNke39OZ2k0?t=65

from setuptools import setup

setup(
        name='bcwallet-btx',
        version='1.2.11',
        description='Simple BIP32 HD cryptocurrecy command line wallet',
        author='David Bergen',
        author_email='david.bergen@gmx.net',
        url='https://github.com/dalijolijo/bcwallet-btx/',
        py_modules=['bcwallet-btx'],
        python_requires='>2.7',
	install_requires=[
            'clint==0.4.1',
            'blockcypher==1.0.69',
            'bitmerchant-btx==0.1.9',
            'tzlocal==1.2',
            ],
        entry_points='''
            [console_scripts]
            bcwallet-btx=bcwallet_btx:invoke_cli
        ''',
        packages=['bcwallet-btx'],
        )
