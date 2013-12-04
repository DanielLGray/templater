
# Make a class... 
import os
import getpass
import glob
	
def browsefiles():
	# line that reads the files in the folder, returns as a list
	# get this from the Dive into Python intro
	# line that takes each of the files, divides up into individual <ol> tags
	current_work_dir = os.getcwd
#!! hard code directory paths now, have as argument later...
	templates_dir = os.path.join(os.path.expanduser('~'), 'Documents', 'python', 'django-nmr', 'nmrserver', 'templates')
	# changes the current working directory to the one that has the NMR files... for the moment this is the templates files
#!! change this to location of user files... 
	os.chdir(templates_dir)
	new_working_directory = os.getcwd

# hard-code extension now, have as argument later...
	# returns list of all *.html files as strings
	file_and_ext = glob.glob('*.*')
	# splits list of files into tuples of filename and extension, takes the first of every tuple, the filename
	# returns a list of file names
	filenames = [os.path.splitext(i)[0] for i in file_and_ext]
	absolute_path_for_NMR_files = [(templates_dir, files) for files in file_and_ext]


class template_files():
	pass
	# there is a python "file type" that might be good to use this as a wrapper around...
	

	print absolute_path_for_NMR_files

browsefiles()