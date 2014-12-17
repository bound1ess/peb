from os.path import isfile, exists, dirname, abspath, join
from os import mkdir, getcwd, listdir
from shutil import copyfile

def is_phpcpp_installed():

	files = ["/usr/include/phpcpp.h", "/usr/lib/libphpcpp.a", "/usr/lib/libphpcpp.so"]

	for file in files:
		if not isfile(file):
			return False

	return True

def create_extension_dir(ext_name):

	path = "%s/%s/" % (getcwd(), ext_name)

	if not exists(path):
		mkdir(path)
		return True
	else:	
		return False

def copy_template_files(to):
	
	path = "%s/../ext/" % dirname(abspath(__file__))

	files = [file for file in listdir(path) if isfile(join(path, file))]

	for file in files:
		copyfile(join(path, file), to)
