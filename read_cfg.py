import ConfigParser
import argparse
import shutil
import os
import subprocess

class ReadFile():
	def __init__(self):
		self.configFilePath = ''
		self.layout = ''
		self.destinationFilePath = ''
		self.sourcefile = ''
		self.destinationfile = ''

	def argument_parser(self):
		argparser = argparse.ArgumentParser()
		argparser.add_argument("-d","--destinationfilepath",required=True,help="Path of destination file")
		argparser.add_argument("-c","--configfilepath",required=True,help="Path of config file")
		argparser.add_argument("-t","--layouttype",required=True,help="Type of layout")
		args = vars(argparser.parse_args())
		self.destinationFilePath = args['destinationfilepath']
		self.configFilePath = args['configfilepath']
		self.layout= args['layouttype']
		print(self.destinationFilePath)
		print(self.configFilePath)
		print(self.layout)

	def read_file(self):
		configParser = ConfigParser.RawConfigParser()
		configParser.read(self.configFilePath)
		#print(self.configFilePath)
		self.sourcefile = configParser.get('my-config','source')
		self.destinationfile= configParser.get('my-config','destination')
		print(configParser.get('my-config','source'))
		print(configParser.get('my-config','destination'))
		print(configParser.get('my-config','layout_type'))

	def copy_file(self):
		#shutil.copy(self.sourcefile, self.destinationfile )
		process = subprocess.Popen(['cp',self.sourcefile, self.destinationfile], stdout=subprocess.PIPE)
		output = process.stdout.readline()
		rc = process.communicate()[0]
		rc = process.returncode
		print("OUTPUT OF process code")
		print(rc)
		


#argument_parser()
#read_file()
obj=ReadFile()
print("OUTPUT OF ARGUMENT_PARSER!!!")
obj.argument_parser()
print("OUTPUT OF READ_FILE!!!")
obj.read_file()
print("COPY_FILE function call!!!")
obj.copy_file()

'''
configParser = ConfigParser.RawConfigParser()
argparser = argparse.ArgumentParser()
argparser.add_argument("-d","--destinationfilepath",required=True,help="Path of destination file")
argparser.add_argument("-c","--configfilepath",required=True,help="Path of config file")
argparser.add_argument("-t","--layouttype",required=True,help="Type of layout")
args = vars(argparser.parse_args())
destinationFilePath= args['destinationfilepath']
configFilePath = args['configfilepath']
layout= args['layouttype']
print(destinationFilePath)
print(configFilePath)
print(layout)
f=open(configFilePath,'r')
data=f.readlines()
#print(data)
f.close()
configParser.read(configFilePath)
#self.path = configParser.get('my-config','source')
print(configParser.get('my-config','source'))
print(configParser.get('my-config','destination'))
print(configParser.get('my-config','layout_type'))
'''
