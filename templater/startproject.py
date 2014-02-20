import sys
import re
import glob
from os import makedirs, removedirs, chdir
from base import Page, Scratch

''' Script to make template and pages from arguments. 
	Usage: 		startproject.py <projectname> 
				startproject.py <projectname> -add [<pagename> | <pagename> ... ]


'''	

class Project(object):

	

	def __init__(self, page_arguments):
		self.page_arguments = page_arguments
		self.page_file = open(self.default_template, encoding='utf-8')




	default_template = "template.html"

'''
python startproject.py mysite
looks for template.html, sitestyle.css, script.js in the same folder,
if not there, says doesn't have these files. Make them, then run 
manage.py template update
'''

"""
Script ideas

>>> startprobject.py pageone pagetwo pagethree

pages_list = sys.argv(1:)
for page in pages_list:
	dictionary_of_pages



write_to_file(dictionary_of_pages)





"""

		

if __name__ == '__main__':

	project = Project(sys.argv[1:])
	project.build()