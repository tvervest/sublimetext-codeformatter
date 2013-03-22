# @author 		Avtandil Kikabidze
# @copyright 		Copyright (c) 2008-2013, Avtandil Kikabidze (akalongman@gmail.com)
# @link 			http://long.ge
# @license 		GNU General Public License version 2 or later;


try:
	# Python 3
	from io import StringIO
	#from .AutoPEP8 import autopep8
	from .sublimeautopep8lib.autopep8 import autopep8


except (ValueError):
	# Python 2
	from StringIO import StringIO
	from PythonTidy.config import version, summary
	from PythonTidy import PythonTidy
	from PythonTidy import PythonTidyWrapper


class Beautifier:
	def __init__(self, formatter):
		self.formatter = formatter

	def beautify(self, text, options):
		stderr = ""
		stdout = ""


		stdout = autopep8.fix_string('x=       123\n')

		return stderr, stdout





		config = PythonTidyWrapper.Config()

		for key, val in options.iteritems():
			config.set_global(key, val)

		config.to_pythontidy_namespace()

		try:
			source = StringIO(text)
			output = StringIO()
			PythonTidy.tidy_up(source, output)
			stdout = output.getvalue()
		except Exception as e:
			stderr = str(e)

		if (not stderr and not stdout):
			stderr = "Formatting error!"

		return stdout, stderr
