#!/usr/bin/env python3
PEB_VERSION = "0.0.0"

from os.path import isfile
from cement.core import foundation, controller

def phpcpp_is_installed():
	return isfile("/usr/include/phpcpp.h") \
	and isfile("/usr/lib/libphpcpp.a") \
	and isfile("/usr/lib/libphpcpp.so")

class PebBaseController(controller.CementBaseController):
	class Meta:
		label = "base"
		description = "PHP Extension Builder"	

	@controller.expose(hide = True)
	def default(self):
		print("PHP Extension Builder (version %s)" % PEB_VERSION)

	@controller.expose(help = "Check if PHP-CPP library is installed.")
	def check_install(self):
		if phpcpp_is_installed():
			print("PHP-CPP is correctly installed.")
		else:
			print("PHP-CPP is not installed on your machine.")

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
