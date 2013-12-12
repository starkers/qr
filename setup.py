from setuptools import setup

setup(name='qr',
      version='1.0',
      description='qr generator',
      author='Tom Taylor',
      author_email='tom@tommyt.co.uk',
      url='qr-k3rnl.rhcloud.com',
	install_requires=[
	    'Flask==0.7.2',
	    'MarkupSafe',
	    'qrcode',
	    'pillow',
	]
     )
