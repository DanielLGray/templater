from os import makedirs, removedirs, chdir
import re
import glob


''' Can create pages from a template, if run as stand-alone. 
OLD BACKUP VERSION OF BASE.PY

'''	
# each import line does the following:	
# for class page_engine directory_builder to make directories and then for tests() to delete them!
# for matching paterns
# for looking in directories to get the template.html


class Page(object):
	''' Has a name, html, css, and js attributes ''' 
	def __init__(self, name, html, css='css', js='js'):
		self.name = name 
		self.html = html
		self.css = css
		self.js = js

	# def __repr__(self):
	# 	return dict( self.name + .html, self)




class Make(object):
	''' Creates a directory, writes files, from a Page object that has attributes name, html, css, and js. '''

	def __init__(self, name):
		self.name = name 
	

	def page_writer(self, page):
		''' Takes a page object, creates a parent directory
		with index.html and children. '''
		with open(page.name + '.html', 'w') as f:
			f.write(page.html)
		try:
			with open(page.name + '.css', 'w') as f:
				f.write(page.css)
		except Exception, e:
			print "Could not make %s css file!" % page.name
		try:
			with open(page.name + '.js', 'w') as f:
				f.write(page.js)
		except Exception, e:
			print "Could not make %s js file!" % page.name
		return None


	def dir_write_and_open(self, page):
		try:
			makedirs(page.name)
			chdir(page.name)
			return True		
		except Exception, e:
			print "Could not change into newly created directory!"
			return None

	def write_project_page(self, page):	
		dir_write_and_open(page)
		page_writer(page)
		chdir('..')
		return None

# Work in progress
	def writer_validation():
		''' Makes sure the right files were made '''
		file_and_ext = glob.glob('*.html')
		current_work_dir = os.getcwd	


class Scratch(PageEngine):
	''' 
	Takes a template and makes the page objects that are specified in the nav links.	
	The template is a unique file that is loaded from the current working directory.
	Page objects have 'name', 'html', 'css', and 'js' atrributes.
	'''

	def __init__(self): 
		self.cache = []
		self.filenames = glob.glob('template.html')
		try:
			for filename in self.filenames:
				with open(filename, 'r') as f:
					self.template = f.read()
			return self.template
		except AttributeError:
			print 'There does not seem to be a "template.html" in this directory'
			return None


	def pages_generator(self, template=self.template):
		# fix this so it recognizes the <nav> tag and then goes to make pages
		pattern = r'<li><a href="[\W]*([\w]+)'
		links = re.findall(pattern, self.template)
		pages = {}
		for i in links:
			new_page = Page(i, template)
			self.cache.append(new_page)
			# Makes and changes into 
			self.write_project_page(new_page)


class update_engine(object):
	pass 


def generate_pages():
	# projectName = raw_input('Project Name:')	
	projectName = 'SampleProject'
	a_project = Scratch(projectName)
	a_project.pages_generator()


if __name__ == '__main__':
	generate_pages()