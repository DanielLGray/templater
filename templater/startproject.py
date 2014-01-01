import sys
import re
import glob
from os import makedirs, removedirs, chdir
from base import Page, Scratch

''' Script to make template and pages from arguments. '''	

class Project(object):

	default_template = "template.html"

	def __init__(self, page_arguments):
		self.page_arguments = page_arguments
		self.page_file = open(self.default_template, encoding='utf-8')



'''
python startproject.py mysite
looks for template.html, sitestyle.css, script.js in the same folder,
if not there, says doesn't have these files. Make them, then run 
manage.py template update
'''

'''
python manage.py makepages home blog 
python manage.py makepages news
python manage.py update from news
'''

		

if __name__ == '__main__':

	project = Project(sys.argv[1:])
	project.build()