#!/usr/bin/env python3
from cement.core import foundation

app = foundation.CementApp('PEB')

try:
	app.setup()
	app.run()
	app.log.info('Hello, world!')
finally:
	app.close()
