from os.path import isfile, exists, dirname, abspath, join
from os import mkdir, getcwd, listdir, rename
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
		copyfile(join(path, file), "%s/%s/%s" % (getcwd(), to, file))

def change_ini_file(ext):
	ext_dir = "%s/%s/" % (getcwd(), ext)
	ini_file = ext_dir + ext + ".ini"
	makefile = ext_dir + "Makefile"
	main = ext_dir + "main.cpp"

	rename(ext_dir + "extension.ini", ini_file)

	with open(ini_file, "r") as file:
		contents = file.read()
		with open(ini_file, "w") as file:
			file.write(contents.replace("extension.so", ext + ".so"))
	
	with open(makefile, "r") as file:
		contents = file.read()
		with open(makefile, "w") as file:
			file.write(contents.replace("NAME = extension", "NAME = " + ext))
	
	with open(main, "r") as file:
		contents = file.read()
		with open(main, "w") as file:
			file.write(contents.replace("yourextension", ext))
