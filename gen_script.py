#!usr/bin/python3

import json

class GenerateBinding:
	cppfilename=""
	modulename=""
	linelist=[]
	jsondata=None


	def __init__(self, jsonfilename):

		# helper function for generating cppfilename from jsonfilename (with path)
		def gen_cppfilename(jsonfilename):
			jsonfilename=jsonfilename.split('.')[0]
			jsonfilename="/".join(jsonfilename.split('/')[1:])
			return "gen/"+jsonfilename+".cpp"

		# create empty file
		self.cppfilename=gen_cppfilename(jsonfilename=jsonfilename)
		open(self.cppfilename).close()

		# module name extracted from jsonfilename
		self.modulename=jsonfilename.split('/')[1]

		# add pybind11 info to linelist
		self.linelist.append("#include <pybind11/pybind11.h>")
		self.linelist.append("using namespace py = pybind11;")

		# load json data
		with open(jsonfilename) as f:
			self.jsondata = json.load(f)



	def write_to_file(self):
		"""
		write to file from linelist
		"""

		# add proper formatting or call a clang-format
		with open(self.cppfilename, 'w') as f:
			for line in self.linelist:
				f.writelines(line+'\n')



	def call_order(self):
		self.write_to_file()
		

x=GenerateBinding(jsonfilename="json/2d/keypoint.json")
x.call_order()
# for file in parsed_header_list:
# 	with open(file) as f:
# 		data = json.load(f)

	# for blocks in data:
	# 	if(blocks['type']=='include'):
	# 		print(blocks['file'])
