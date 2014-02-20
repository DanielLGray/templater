import os 
import re
import glob


''' Can create pages. '''	


class Page(object):
	''' Has a name and html attributes. Use Page.dictionary to access the html, css and js names and contents.''' 
	def __init__(self, name):
		self.name 	= name 
		self.html_filename = self.name + '.html'

	def __str__(self):
	 	return('<%s.html Page object>' % self.name)


def filename_builder(some_filename, extension):
	''' Checks to see if the correct extension is added, and if no extension is present, the
	specified one will be added. If an incorrect extension is found, raises ValueError. '''
	(a_potential_name, ext) = os.path.splitext(some_filename)
	if ext == extension:
		return some_filename
	elif ext == '':
		return a_potential_name + extension
	else:
		raise ValueError("This extension is not supported: %s", ext)

def build_page_with_css_and_js(page_object, css_filename='stylesheet.css', js_filename='script.js'):
	''' Supply a stylesheet and script with '.css' and '.js' extension (or not, and '.css' or '.js' will be added) '''
	css_and_js_attrs = ('css_filename', css_filename, '.css'), ('js_filename', js_filename, '.js')
	for key, value, extension in css_and_js_attrs:
		setattr(page_object, key, filename_builder(value, extension))

def try_and_make_dir(dir_name):
	try:
		os.makedirs(dir_name, 644)		
		return True
	except FileExistsError:
		return False

''' 
script idea:
if try_and_make_dir(dir_name):
	write_html_css_js(stuff)
'''
# Here begins the work in progress
# also open templater_tests.py and startproject.py
def add_content_to_new_page(page_object, filename):
	file_types = ['.html', '.js', '.css']
	if filename has extension file_type
		setattr(page_object, file_type, filename)
	



# template = Page('template')

# 		try:
# 			with open(name, 'r') as f:
# 				self.html = f.read()
# 			if re.match(css_name, self.html):
# 				with open(css_template_name, 'r') as f:
# 					self.css = f.read()
# 			self.css_files = re.findall(r'[\w]+\.css')
	
# 			assert len(css_files) <= 3, "Too many css files: only a site-wide style and individual stylesheet allowed."
# 			assert css_template_name in css_files, "Specified sylesheet {0} is not in the css_files {1} found in the template_html".format(css_template_name, css_files)

# 		except IOError:
# 			self.html = None
		

def page_writer(page):
	''' Takes a page object, and uses the associated dictionary to write pages. '''
	
	for key_name, value_content in page.dictionary.items():
		with open(key_name, 'a') as f:
			f.write(value_content)

def dir_write_and_open(page):
	try:
		os.makedirs(page.name, 0644)
		os.chdir(page.name)
		return None		
	except Exception:
		print("Could not change into newly created directory!")
		return None

def write_project_page(page):	
	dir_write_and_open(page)
	page_writer(page)
	os.chdir('..')
	return None

class Scratch(object):
	''' 
	Takes a template and makes the page objects that are specified in the nav links.	
	The template is a unique file that is loaded from the current working directory.
	Page objects have 'name', 'html', 'css', and 'js' atrributes.
	'''

	def __init__(self, project_name, ): 
		self.cache = []
		self.cache_index = 0
		self.project_name = project_name
		self.template = Template(project_name)

	''' Can string formatters grab the name of a variable rather than the variable contents?'''
	
	def make_project_directory(self):
		dir_write_and_open(page)
		for page in pages:
			write_project_page(page)

	def pages_generator(self):
		'''
		takes a template page and template css, and then writes the pages that are on the template. Looks for 
		a 'sitestyle.css' in the template file.
		'''
		
		nav_tag_pattern = r'<nav>([\W\w\S\s]+)</nav>'
		nav_links = re.findall(nav_tag_pattern, self.name)
		# re.findall returns a list

		pattern = r'<li><a href="[\W]*([\w]+)'
		links = re.findall(pattern, nav_links[0])

		for i in links:
			re.sub(r'="sitestyle.css', r'="../sitestyle.css', self.template_html)
			if len(css_files) == 2:
				# two files, a site-wide stylesheet and an individual stylesheet.

				# add in the other css files for individual pages
				re.sub(
					r'<{0}"/>'.format(css_template_name), 
					r'<{0}"/><link type="text/css" rel="stylesheet" href="./{1}.css"/>'.format(css_template_name, page.html),
					template_html
					)
			# Clean this up!!
			new_page = Page(i, template, js)
	
			self.cache.append(new_page)
			self.cache_index += 1
			# Makes and changes into 
			write_project_page(new_page)
		return self.cache





