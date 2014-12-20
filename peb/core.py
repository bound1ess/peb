from os.path import isfile, exists, dirname, abspath
from os import mkdir

def phpcpp_is_installed():
	return isfile("/usr/include/phpcpp.h") \
	and isfile("/usr/lib/libphpcpp.a") \
	and isfile("/usr/lib/libphpcpp.so")

def create_extension_dir(dir):
	path = "%s/%s/" % (dirname(abspath(__file__)), dir)
	if exists(path):
		return False
	else:	
		mkdir(path)
		return True
