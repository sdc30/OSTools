## Cartwright, Stephen D
## 8/6/16 


import os

class OSTools():


	def __init__(self):
		self.wd = os.getcwd()
		self.maxfiles = 3
	
	def main(self, str):
		count = 0
		#cwd = os.getcwd()
		cwd = str
		ld = os.listdir(cwd)
		size = len(ld)
		files = []
		
		while count < size:
			o = os.path.join(cwd) + ld[count]
			bool = os.path.isfile(o)
			if bool:
				print o
				files.append(o)
				
			
			count = count + 1
		
		if len(files) > self.maxfiles:
			print "File Contents Printer"
			print "Printer Status: Failed (size > 20) == %d." % count
			exit(1)
			
		count = 0
		
		while count < len(files):
	
			f = open(files[count])
			r = f.read()
			print(r)
			
			
		
exe = OSTools()
print "--- File Contents Printer ---"
print "Input directory or file:"
str = raw_input("> ")

exe.main(str)		
print "File Contents Printer"
print "Printer Status: Finished."
#exe.main(os.getcwd())		

