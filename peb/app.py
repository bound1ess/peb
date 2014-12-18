from cement.core import foundation, controller
from peb.utility import get_peb_version
import peb.core as peb

class PebBaseController(controller.CementBaseController):
	class Meta:
		label = "base"
		description = "PHP Extension Builder"
		arguments = [
			(["--name"], dict(action = "store", dest = "name", help = "Extension name."))
		]

	@controller.expose(hide = True)
	def default(self):
		print("PHP Extension Builder (version %s)" % get_peb_version())

	@controller.expose(help = "Check if PHP-CPP library is installed.")
	def check_install(self):
		if peb.is_phpcpp_installed():
			print("PHP-CPP is correctly installed.")
			return True
		else:
			print("PHP-CPP is not installed on your machine.")
			return False

	@controller.expose(help = "Create new PHP-CPP project.")
	def create(self):
		if not self.check_install():
			print("Interrupting...")
			return False

		name = self.app.pargs.name

		if peb.create_extension_dir(name):
			print("Directory \"%s\" successfully created." % name)
		else:
			print("Directory \"%s\" already exists." % name)

		print("Copying template files to \"%s\"..." % name)
		peb.copy_template_files(name)

		print("Applying small changes...")
		peb.change_ini_file(name)

		print("All done, you are all set!")

	# add a command to build and install (deploy) extension ("deploy")
	# it will execute "make", "make install", "php5enmod" and stuff
	
class Peb(foundation.CementApp):
	class Meta:
		label = "PEB"
		base_controller = PebBaseController
