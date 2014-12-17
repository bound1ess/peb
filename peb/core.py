from os.path import isfile, exists, dirname, abspath
from os import mkdir

def is_phpcpp_installed():

	files = ["/usr/include/phpcpp.h", "/usr/lib/libphpcpp.a", "/usr/lib/libphpcpp.so"]

	for file in files:
		if not isfile(file):
			return False

	return True

def create_extension_dir(ext_name):

	path = "%s/%s/" % (dirname(abspath(__file__)), ext_name)

	if not exists(path):
		mkdir(path)
		return True
	else:	
		return False
