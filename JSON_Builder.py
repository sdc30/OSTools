## Cartwright, Stephen D
## 8/6/16 - 9/25/16

import json


class JSON_Builder():


	def __init__(self):
		print "--- JSON Builder ---"
		print "Build start."


	def main(self, arr):
		
		container_name = "result"
		word = ""
		wrd = '\"' + word + '\"'
		
		print self.construct(container_name, "")

		print "JSON Builder"
		print "Builder finished."


	def construct(self, word, args):
		count = 0
		length = len(args)
		s = ""

		s += word + " : [\""

		while count < length:
			a = args[count]
			
			s += str(a)
			
			if count < length-1:
				s += ", "
			
			count = count + 1
	
		s += "\"]"

		return s


'''
	for a in arr:
	l = []
	l.append(a)
	print self.construct(wrd, l)
'''
