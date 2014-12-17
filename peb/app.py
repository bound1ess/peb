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

		if peb.create_extension_dir(self.app.pargs.name):
			print("Directory \"%s\" successfully created." % self.app.pargs.name)
		else:
			print("Directory already exists.")

class Peb(foundation.CementApp):
	class Meta:
		label = "PEB"
		base_controller = PebBaseController
