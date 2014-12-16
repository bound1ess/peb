#!/usr/bin/env python3
PEB_VERSION = "0.0.0"

from os.path import isfile, exists, dirname, abspath
from os import mkdir
from cement.core import foundation, controller

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

class PebBaseController(controller.CementBaseController):
	class Meta:
		label = "base"
		description = "PHP Extension Builder"	
		arguments = [
			(['--name'], dict(action = 'store', dest = 'name', help = 'Extension name.'))
		]

	@controller.expose(hide = True)
	def default(self):
		print("PHP Extension Builder (version %s)" % PEB_VERSION)

	@controller.expose(help = "Check if PHP-CPP library is installed.")
	def check_install(self):
		if phpcpp_is_installed():
			print("PHP-CPP is correctly installed.")
		else:
			print("PHP-CPP is not installed on your machine.")

	@controller.expose(help = "Create new PHP-CPP project.")
	def create(self):
		if create_extension_dir(self.app.pargs.name):
			print("Directory successfully created.")
		else:
			print("Directory already exists.")

class Peb(foundation.CementApp):
	class Meta:
		label = "PEB"
		base_controller = PebBaseController

app = Peb()

try:
	app.setup()
	app.run()
finally:
	app.close()
