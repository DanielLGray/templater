import re

sample_webpage = """
<!DOCTYPE html>

<html>
	<head>

		<title></title>
		<meta http-equiv="Content-Type" content="text/html;charset=utf-8">			
		<link type="text/css" rel="stylesheet" href="sitestyle.css"/>
		<link type="text/css" rel="stylesheet" href="news.css"/>
		<script type='text/javascript' src='http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js'></script>
		<script type="text/javascript" src="jquery4.js"></script>  		

	
	</head>
	
	<body>
		

	    <header>	
		 	<h1>The X Research Group</h1>
			<nav>
			    <ul>
			      <li><a href="./Home.html">Home</a></li>
			      <li><a href="./Teaching.html">Teaching</a></li>
			      <li><a href="./Research.html">Research</a></li>
			      <li><a href="./Publications.html">Publications</a></li>
			      <li><a href="./ProfBio.html">Prof. Bio</a></li>
			      <li><a href="./Group.html">Group</a></li>
			      <li><a href="./News.html">News</a></li>
			    </ul>
			</nav>
		</header>

	</body>

</html>
"""




def build_match_and_apply_functions(pattern, search, replace):
	''' Builds other match and apply functions dynamically '''
	def matches_rule(word):
		return re.search(pattern, word)
	def apply_rule(word):
		return re.sub(search, replace, word)
	return (matches_rule, apply_rule)



def read(link):
	''' Readout each line in a webpage, make a copy of the lines, then replace the references to other webpages'''
	for 


navEntry = '<li><a href="./Home.html">Home</a></li>'



	
