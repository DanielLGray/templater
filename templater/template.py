from os import makedirs, removedirs, chdir
import re
import glob


''' Can create pages from a template, if run as stand-alone. '''	
# each import line does the following:	
# for class page_engine directory_builder to make directories and then for tests() to delete them!
# for matching paterns
# for looking in directories to get the template.html


class page(object):
	''' Has a name, html, and css ''' 
	def __init__(self, name, html, css='css'):
		self.name = name 
		self.html = html
		self.css = css


class page_engine(object):
	''' Creates a website and all of its pages. The template is a unique file that is loaded from the current working directory'''

	def __init__(self, name):
		self.name = name 

	def detect_template(self): 
		try:
			filenames = glob.glob('template.html')
		except Exception, e:
			print 'There does not seem to be a "template.html" in this directory'
		for filename in filenames:
			with open(filename, 'r') as f:
				self.template = f.read()
		return self.template
	
	def generator(self, template):
		''' Takes a homepage object and makes the page objects that are specified in the nav links '''
		pattern = r'<li><a href="[\W]*([\w]+)'
		links = re.findall(pattern, template)
		pages = {}
		for i in links:
			pages[i + '.html'] = page(i, template)
		return pages	

	def writer(self, pages):
		''' Takes a dictionary of page objects, creates a parent directory
		with index.html and children. '''
		
		# Makes a parent directory for project, writes template as index.html
		makedirs(self.name)
		chdir(self.name)
		with open(self.name + '.html', 'w') as f:
			f.write(self.template)
		for (htmlname,pageObj) in pages.iteritems():
			makedirs(pageObj.name)
			chdir(pageObj.name)
			with open(pageObj.name + '.html', 'w') as f:
				f.write(pageObj.html)
			with open(pageObj.name + '.css', 'w') as f:
				f.write(pageObj.css)
			chdir('..')
		return None

# Work in progress
	def writer_validation():
		''' Makes sure the right files were made '''
		file_and_ext = glob.glob('*.html')
		current_work_dir = os.getcwd	


class update_engine(object):
	pass 


if __name__ == '__main__':
	projectName = raw_input('Project Name:')	
	a_project = page_engine(projectName)
	a_template = a_project.detect_template()
	some_pages = a_project.generator(a_template)
	write_some_pages = a_project.writer(some_pages)