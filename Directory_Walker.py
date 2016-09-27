## Cartwright, Stephen D
## 8/6/16 - 9/27/16

import os
import JSON_Builder

class Directory_Walker():


	def __init__(self):
		self.wd = os.getcwd()
		self.maxfiles = 3
		self.files = []
		self.directories = []
	
	def main(self, s):
		count = 0
		#cwd = os.getcwd()
		cwd = s
		ld = os.listdir(cwd)
	
	
		for a in ld:
			o = os.path.join(cwd, a)
			self.walk(o)
		
		for b in self.directories:
			self.walk(b)

				
		
		#self.printer(self.directories)
		self.printer(self.files)

		jb = JSON_Builder.JSON_Builder()
		jb.main(self.files)

	def walk(self, path_name):
		
		if os.path.isdir(path_name):
			cwd = path_name
			ld = os.listdir(cwd)
			
			for a in range (0, len(ld)):
				o = os.path.join(cwd, ld[a])
				bool = os.path.isfile(o)
				
				if bool:
					self.files.append(os.path.basename(str(o)))
			
				elif o not in self.directories:
					self.directories.append(o)
	
		elif os.path.isfile(path_name):
			self.files.append(os.path.basename(str(path_name)))

		else:
			print ("error:" + path_name)

	def printer(self, arr):
		for ele in arr:
			ele = str(ele)
#			print ele

			
		
exe = Directory_Walker()
print "--- Directory_Walker Printer ---"
print "Input directory"
#s = raw_input("> ")
s = "/Users/ranger/Desktop/books/"


exe.main(s)
print "Printer Status: Finished."
#exe.main(os.getcwd())		

'''

while count < size:
o = os.path.join(cwd) + ld[count]
bool = os.path.isfile(o)
if bool:
self.files.append(o)

else:
self.directories.append(o)

count = count + 1

'''


