from os import makedirs, removedirs, chdir
# for class page_engine directory_builder to make directories
# and then for tests() to delete them!



"""
Imagined user procedure:
make project directory, with template in first directory

"""


class page(object):
	def __init__(self, name, html_content, css_content):
		self.name = name 
		self.html_content = html_content
		self.css_content = css_content


class page_engine(object):
	''' An class that can create a website and all of its pages '''

	def __init__(self, pages):
		self.pages = pages
		self.name = pages.name
		self.html_content = pages.html_content
	
	def generator(self):
		''' Takes a homepage object and makes the pages that are specified in the nav links '''
		pass


	def writer(self):
		''' Takes a page object, creates a directory with page.name,
		a webpage with the page.name, and saves page.html_content '''

		makedirs(self.name)
		chdir(self.name)
		with open(self.name + '.html', 'w') as f:
			f.write(self.html_content)
		with open(self.name + '.css', 'w') as f:
			f.write(self.css_content)

''' Testing will now commence '''


def tests():
	index = page('index', sample_webpage)
	print index
	a_project = page_engine(index)
	print a_project
	a_project.writer()

def undotests():
	pages = ['index', 'blog', 'housemusic']
	for page in pages:
		removedirs(page)	



	

class modify_engine(object):
	pass 

class index(object):
	pass

class blog(object):
	pass

class article(object):
	pass
