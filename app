#!/usr/bin/env python3
from peb.app import Peb

app = Peb()

try:
	app.setup()
	app.run()
finally:
	app.close()
