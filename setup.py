try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'File Hash',
    'author': 'Jonathan Bowen',
    'url': 'https://github.com/jbowen102/file_hash',
    'download_url': 'https://github.com/jbowen102/file_hash',
    'author_email': 'ew15dro6k216@opayq.net',
    'version': '',
    'install_requires': [''],
    'packages': [],
    'scripts': [],
    'name': 'file_hash'
}

setup(**config)
