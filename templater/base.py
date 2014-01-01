from os import makedirs, removedirs, chdir
import re
import glob


''' Can create pages from a template, if run as stand-alone. '''	
# each import line does the following:	
# for class page_engine directory_builder to make directories and then for tests() to delete them!
# for matching paterns
# for looking in directories to get the template.html


class Page(object):
	''' Has a name, html, css, and js attributes ''' 
	# make optional keyword arguments here
	def __init__(self, name, html=None, css=None, js=None):
		self.name 	= name 
		self.html 	= html
		self.css 	= css
		self.js 	= js
		self.html_name = self.name + '.html'
		self.css_name = self.name + '.css'
		self.js_name = self.name + '.js'
		self.names = [self.html_name, self.css_name, self.js_name]
		self.dictionary = { 
							self.html_name: self.html, 
							self.css_name: self.css, 
							self.js_name: self.js,
						}

	# def __str__(self):
	# 	return('<%s.html Page object>' % self.name)



template = Page('template')

		try:
			with open(name, 'r') as f:
				self.html = f.read()
			if re.match(css_name, self.html):
				with open(css_template_name, 'r') as f:
					self.css = f.read()
			self.css_files = re.findall(r'[\w]+\.css')
	
			assert len(css_files) <= 3, "Too many css files: only a site-wide style and individual stylesheet allowed."
			assert css_template_name in css_files, "Specified sylesheet {0} is not in the css_files {1} found in the template_html".format(css_template_name, css_files)

		except IOError:
			self.html = None
		

def page_writer(page):
	''' Takes a page object,  index.html and children. '''
	
	for key_name, value_content in page.dictionary.items():
		with open(key_name, 'a') as f:
			f.write(value_content)

def dir_write_and_open(page):
	try:
		makedirs(page.name, 0644)
		chdir(page.name)
		return None		
	except Exception:
		print("Could not change into newly created directory!")
		return None

def write_project_page(page):	
	dir_write_and_open(page)
	page_writer(page)
	chdir('..')
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







# def generate_pages():
# 	# projectName = raw_input('Project Name:')	
# 	projectName = 'SampleProject'
# 	a_project = Scratch(projectName)
# 	a_project.pages_generator()


# if __name__ == '__main__':
# 	generate_pages()