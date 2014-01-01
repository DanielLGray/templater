from nose.tools import *
import unittest
import glob
from templater import base, startproject
from os import makedirs, removedirs, chdir, getcwd

# def setup():
# 	print 'SETUP!'

# def teardown():
# 	print 'TEAR DOWN!'

# def test_basic():
# 	print 'I RAN!'

'''
Well, what do I want to assert to be true?
The goals of this program are to set up a project from the template files.
Generate pages from the command line, and update those pages from the command line.
'''


class PageValues(unittest.TestCase):

	def setUp(self):
		self.pagename = 'mypage'
		self.pagehtml = '<html><h1>Hello World!</h1></html>'
		self.pagecss = 'h1 {\n\tcolor: green\n}'
		self.pagejs = None
		self.attr_values = [self.pagename, self.pagehtml, self.pagecss, self.pagejs]
		self.exts = ['.html', '.css', '.js']


	# def test_make_page_object(self):
	# 	"""
	# 	A samplepage made with Page(name, html, css) should have Page.name, Page.html, Page.css
	# 	"""

	# 	samplepage = base.Page(self.pagename, self.pagehtml, self.pagecss, self.pagejs)
	# 	sample_page_attrs = [samplepage.name, samplepage.html, samplepage.css, samplepage.js]

	# 	self.assertIsInstance(samplepage, base.Page)

	# 	for x in zip(self.attr_values, sample_page_attrs):
	# 		# with self.subTest():
	# 		self.assertEqual(x[0], x[1])
			
	# def test_page_writer(self):
	# 	"""
	# 	When you make a page object and write the html, css, and js, they should exist!
	# 	"""
	# 	samplepage = base.Page(self.pagename, self.pagehtml, self.pagecss, self.pagejs)

	# 	sample_page_attrs = [samplepage.name, samplepage.html, samplepage.css, samplepage.js]
	# 	abbrev_attr_values = [self.pagehtml, self.pagecss, self.pagejs]

	# 	base.page_writer(samplepage)

	# 	for x in zip(abbrev_attr_values, self.exts):
	# 		if x[0] is not None:
	# 			self.assertEqual(glob.glob(self.pagename + x[1]), [self.pagename + x[1]])
		
	# 	# Now, need a way to remove these files.


	# def test_write_project_page(self):

	# 	samplepage = base.Page(self.pagename, self.pagehtml, self.pagecss, self.pagejs)
		
	# 	base.write_project_page(samplepage)
		
	# 	assert samplepage.name in glob.glob('*')
	# 	chdir(samplepage.name)
	# 	self.test_page_writer()
	# 	chdir('..')

		# And a way to remove the dir 'mypage' and files in that dir

	def test_scratch(self):
		
		scratch_project = base.Scratch('myproject')
		self.assertRaises(IOError, scratch_project.pages_generator('template_fake.html'))
		scratch_project.pages_generator('template.html')
		directories = ['Home', 'OtherHome', 'OtherOtherHome']


		
		for directory in directories:
			assert directory in glob.glob('*')
			chdir(directory)
			for extension in self.exts:
				self.assertEqual(glob.glob(directory), [directory + extension])
			chdir('..')	



	# def test_generate_pages(self):
	# 	pass