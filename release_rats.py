#releases the rats
import os
from os.path import expanduser
from random import randint

def release():
	home = expanduser("~")
	dirs = []
	the_rat = """

        _        _    
       (\\.-""-.//)  
        /        \    /)
        \o      o/   ((
        /\      /\    ))
       /==\ () /==\  //
      |    `UU`    |//
      |            |/
    .-'\          /'-.
   (((` ) |----| ( `)))
       (((`    `)))
"""
	counter = 0
	print_list = range(0,10000, 75)
	for dirname, dirnames, filenames in os.walk(home):
		# finding all directories
		for subdirname in dirnames:
			dirs.append(os.path.join(dirname, subdirname))
			counter = counter + 1
			if counter in print_list:
				print("**scurry scurry**")

	for i in range(50):
		pre_path = dirs[randint(0, len(dirs))] #choosing dir
		path = pre_path + '/'
		#print("path is \n %s") % path
		completeName = os.path.join(path, "rat.txt") #naming file
		try:
			file = ''
			file = open(completeName, 'w')
		except IOError:
			pass
		
		if len(file) != 0 :
			file.write(the_rat) #writing
			file.close()
		else:
			pass
			
release()	