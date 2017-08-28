try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'File Hash',
    'author': 'Jonathan Bowen',
    'url': 'https://github.com/jbowen102/file_hash'
    'download_url': '',
    'author_email': 'jjbowen19@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': [],
    'scripts': [],
    'name': 'file_hash'
}

setup(**config)
