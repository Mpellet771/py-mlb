from logging import getLogger, Handler

__version__ = '1.0'

class NullHandler(Handler):
	def emit(self, record):
		pass

logger = getLogger(__name__)
logger.addHandler(NullHandler())
