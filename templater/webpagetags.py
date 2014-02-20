
# necessary types 
class doctype(object):
	def __init__(self, tag):
		self.tag = 'doctype html'

class head(object):
	def __init__(self, tag):
		self.tag = 'head'

class meta(object):
	def __init__(self, tag):
		self.tag = 'meta'

class link(object):
	def __init__(self, tag, attributes):
		self.tag = 'link'
		self.attributes = ''

class title(object):
	def __init__(self, tag):
		self.tag = 'title'
	
class html(object):
	def __init__(self, tag, attributes):
		self.tag = 'html'
		self.attributes = ['lang="en"']

class body(object):
	def __init__(self, tag):
		self.tag = 'body'
	
class nav(object):
	def __init__(self, tag):
		self.tag = 'nav'

class section(object):
	def __init__(self, tag):
		self.tag = 'section'

class article(object):
	def __init__(self, tag):
		self.tag = 'article'
	
class ul(object):
	def __init__(self, tag):
		self.tag = 'ul'

class li(object):
	def __init__(self, tag):
		self.tag = 'li'

class img(object):
	def __init__(self, tag):
		self.tag = 'img'

class a(object):
	def __init__(self, tag, attributes):
		self.tag = 'a'
		self.attributes = ['href=']

class audio(object):
	def __init__(self, tag):
		self.tag = 'audio'

class video(object):
	def __init__(self, tag):
		self.tag = 'video'

class source(object):
	def __init__(self, attributes):
		self.attributes = ['src=']



class tag_engine(object):
	"""Takes tag names and produces the right <, /, > syntax."""
		
	# dictionary of tag types and their corresponding syntaxes

	def __init__(self, name):
		self.name = name

	def tag_open(self, tag):
		self.tag = tag
		tag_open = '<' + self.tag
		return tag_open
		
	def tag_close(self, tag, attributes):
		self.tag = tag
		self.attributes = attributes
		tag_close = self.tag + attributes + '>'
		tag_close = '</' + self.tag + '>'
		return tag_close

	def tag_open_and_close(self, tag, attributes):
		self.tag = tag
		self.attributes = attributes 
		tag_open_close = '<' + self.tag + attributes + '/>'
		return tag_open_close



class page_builder(object):
	''' Collects tags and attributes, and puts together a cohesive webpage '''
	def __init__(self):
		pass
		
	def header(self, tags):
		pass
		# takes a dictionary of tags and attributes, 
		# and turns it into html.
		# produces the most up-to-date jquery libraries		 
		'''		 = tag_engine.tag_open()
		# necessary types :
		doctype 
		html
		head
		meta
		link
		title
		'''
		# reads a set of instructions (i.e. header options, page names)
		# with ability to add pages afterwards.
		# takes arguments, makes webpages and CSS templates
	
	def body():
		pass
	# open file
	# write
