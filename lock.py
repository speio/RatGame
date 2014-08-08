#riddle for password based lock on door
#text the longest word in the english language is ostensibly opposite but infinitely dissimilar
#to the entry command
import time, helpers, sys, termios, fcntl, struct, signal
from random import randint


#gets size of window used as upper bound to range of randint
def getTerminalSize():
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

        ### Use get(key[, default]) instead of a try/catch
        #try:
        #    cr = (env['LINES'], env['COLUMNS'])
        #except:
        #    cr = (25, 80)
    return int(cr[1]), int(cr[0]) 
    
   
def unlock_lock(food):

	print """
 ______________________________________
|00000000000000000000000000000000000000|
|0|                                  |0| 
|0|                                  |0|                                  
|0|     Pass:___________________     |0|
|0|                ---------         |0|
|0|          Hint:|type HELP|        |0|
|0|                ---------         |0|
|00000000000000000000000000000000000000|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""






	if food == 'peanut':
		print "You run fast, and are pretty far ahead of the beast"
		print "That should give you enough time to remember the passowrd"
		repeats = 10
	else:
		repeats = 5
	
	start_repeat = repeats
	terminal_size = getTerminalSize()			
	round = 1
	output = 'bella 1'
	while repeats != 0:
		
		
		if round == 2:
			print "Attempts until beast chomps your face: %i" % repeats
			print ""
				
		print "Input password, type HELP for hint, or type EXIT to quit.\n "
				
		attempt = raw_input("> ")
				
		key_unlock = ''
		password = key_unlock*0
		legitimate_password = password
		official_password = legitimate_password
		actual_password = official_password
		real_password = actual_password
		true_password = real_password
	
		if attempt == true_password:
			output = 'unlocked'
			break
		elif attempt == 'HELP' or attempt == 'help' and round == 1:
			print "It's the only password a rat would ever remember"
		elif attempt == 'HELP' or attempt == 'help' and round != 1:	
			print "The longest word in the english language is ostensibly opposite"
			print "Boop"
			time.sleep(1)
			print "Nope"
			time.sleep(2)
		else:
			delay = 5*(start_repeat - repeats)*len(attempt.split())	
			
			for i in xrange(delay):
				spacing = randint(1,terminal_size[0])
				time.sleep(1)
				boop = ' '*spacing + 'boop' 
				print boop
			
				if i == delay:
					print "WRONG"
					
			round = round + 1	
			repeats = repeats - 1
		
		if repeats <= 2:
			helpers.stall(food)
			#need to write function in helpers that will serve for a stalling bella 
			#game that offers feeding with food obtained from package, or calling landlord
			# or calling out her name. Options could be "Feed..." "Call landlord" "Throw voice"
			#requiring that player knows the landlords number, has the peanut butter, or knows 'bella'
			
			print "The beast is nearing"
			print "You need  to think of a way to stall her."
			print "What should you do?"		
		
	return(output)
	
