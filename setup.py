try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description' : 'My Project',
	'author' : 'Daniel Gray',
	'url' : 'https://github.com/DanielLGray',
	'download url' : 'https://github.com/DanielLGray/templater',
	'author_email' : 'dgray60@gmail.com',
	'version' : '0.1',
	'install_requires' : 'nose',
	'packages' : ['templater'],
	'scripts' : [],
	'name' : 'templater',
}

setup(**config)
