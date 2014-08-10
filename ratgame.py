import time, helpers, dead, webbrowser, lock, release_rats
start = time.time()
#The game of the Rat
print "     The \n Game of the \n     Rat"
raw_input("Press enter to continue")
print "Choose your character:"
time.sleep(1)



	
#Drawing character choices
print "Elfred Ratskill"


print "	 	   	          _..----.._      _"
print "	      			.\'  .--.    \"-.(0)_"
print "                  '-.__.-''''=:|   ,  _)_ \__  . c\\'-.."
print "	     			 '''------'---''---'-\""



time.sleep(.7)
print "Sir. Ratsalot"

print "	             (\,/)"
print "                     oo   '''//,        _"
print "                   ,/_;~,        \,    / '"
print "                    \"'  \    (    \    !"
print "                         ',|  \    |__.'"
print "                         '~  '~----''"


time.sleep(.7)
print "Ratzo"

print "                .---."
print "           (\./)     \.......- "
print "           >' '<  (__.'\"\"\"\" "
print "          \" ` \" \""

#taking character input
#and checking to see if character was typed correctly
character =""
while len(character) == 0:
	character = raw_input("Which character do you choose? \n > " )	

	if character in ["Ratzo" , "ratzo"]:
		print "Good choice %s is a great rat." % character
		break	
	elif character in ["Sir. Ratsalot" , "Elfred Ratskill", "sir. ratsalot", "elfred ratskill"]:
		print "%s is cool as fuck, but you should pick a different rat." % character
		character = ""
	else:
		character = ""
		print "You probably mistyped something, let's try entering the rat's name again"

print "Let's begin our adventure!"


print "You awake in a small ratbed with a candle precariously burning beside the bed."
print "The rest of the room is dark besides the sphere of light around you from the candle."
print "You probably fell asleep reading"
time.sleep(5.5)
print "Thank god you didn't burn the rathouse down."

rat = "Ratzo"
round = 1

#Haven't worked on other characters: 
while character == "Sir. Ratsalot":
	print "Hey Sir Ratsalot...nice to see you again."
#Haven't worked on other character: 
while character == "Elfred Ratskill":
	print "Hello Elfred"


##MEETING##
#function for presenting and giving the package, leads to same room but either with or without contents
#Also has loop including riddle to figure out who is giving the package

while rat == "Ratzo":
	if round == 1:
		print "...and suddenly a voice"
		time.sleep(2)
		print "\"Hi Ratzo...You recieved a package while you were out."
		print "Would you like the package now?\""
	elif round == 2:
		print "\"So do you want the package or not?\""
	else:
		print "How did you get here?"
		exit(1)
			
	package_ans = str(raw_input("(y/n) \n > "))

	x = len(set(package_ans.split()) &  set(["who", "are", "you"]))#splits user input into list of strings the
	#compares intersection of the two lists. if non-zero can enter landlord
	
	if package_ans == "y":
		print "A package slides out of the darkness towards your bed"
		time.sleep(2)
		print "'Here you go %s'" % character 
		print ""
		item = "yes"
		time.sleep(2)
		break
		

	elif package_ans == "n":
		print "Fine"
		time.sleep(2.7)
		print "jerk."
		print "The mysterious voice traveles off mumbling curses at you"
		time.sleep(3)
		item = "no"
		break
	
	elif x != 0 :
		landlord_output = helpers.landlord()
		rat = landlord_output[0]
		round = landlord_output[1]
		
	else:
		print "\" %s \"is not a proper answer" % package_ans
		round = 2


##BEDROOM##

print "You get up and step into the dark bedroom."
print ""

while True:
			
	if item == "yes":
		print "Package in hand, you look around the dark room for what to do next."
		print "You deliberate a bit on what to do with the package, what could it be?"
		time.sleep(5)
		print "You wonder if you should even open it..."
		open_package = raw_input("Open? (y/n)> ")
	
		if open_package == "n":
			op_result = helpers.openpackage("no")
			food = op_result
			break
	
		elif open_package == "y":
			op_result = helpers.openpackage("yes")
			food = op_result
			break
		
	
		else:
			print "I don't understand"
			

	elif item == "no":
		print "You got no package and no cares, you're basically a free spirit."
		time.sleep(1.9)
		print "No package weighing you down."
		time.sleep(1.7)
		print "No sweet ass items"
		time.sleep(1.5)
		print "No clue what the hell you're doing or who has been talking to you."
		print ""
		food = 'neither'
		
		break

	else:
		"else bedroom reached"

	

			

if food == "peanut":
	print "Belly full of Oreos"
	print "Pocket full of Peanut Butter"
	
	time.sleep(2)
	
elif food == "both":
	print "With a box full of oreos and peanut butter."
	time.sleep(2)
elif food == "neither":
	print "Claws clumped with crap, fur full of fuzz, snout soaked with snot."	
	print ""
	time.sleep(2)
elif 
else:
	print " else reached"


time.sleep(3)	
print "You step forth through the dark of the bedroom towards a rat doorway, lit from outside"
time.sleep(2.5)
print """
       _---_
   .-"``   ``"-.
  /            \\
 |              |
 |              |
 |              |
 |              |
 |              |
 |              |
 |              |
 |              |
 |______________|
 
"""
print "You step through it, a white haze turns to colours as your eyes adjust to the bright light."
time.sleep(4)
print "Suddenly a BEAST!"
time.sleep(0.5)
print """
 ,--.____                                     ____.--.
/  .'.'"``--...----------.___.----------...--''"`.`.  \\
| .'.'         .                       .         `.`. |
`. .'|     . ' - . _    `-----'    _ . - ' .     |`. .'
 `.' `|   .'   _     "-._     _.-"     _   `.   |' `.'
      |  |        " -.           .- "        |  |
       \|        ;;..  "|i. .i|"  ..;;        |/
       `|_      ,---.``.   ' '   .'',---.     _|'
          \   <'(_@_.'>.'--- '---`.<`_@_)`>  / 
           \ `. `~  .'  ,-------.  `.  ~'.' /  
           |=_"`=.'    `-.___.-' .  `.='"_=| 
           |  ==/          i   : ' :  \==  |
           | ==/      /\___|___/\      \== |
           | =Y      .' \"\"\"_\"\"\" `.      Y= |
           L ||      ;  .=="==.  ;      || J
            \ ;     .' '       ` `.     ; /
             `.     ;             ;     .'
               \;  ;'\           /`;  ;/
                 '-.'.'/.       ,\`.`-'
                        `-----'  
"""


time.sleep(2)
print "You freeze in your rattracks"
time.sleep(1)
print "NO TIME TO LOOK CAREFULLY"
print "WHAT SHOULD YOU DO?"
time.sleep(1)

while True:	
	print ""
	print "1) Run to the right, 'right turn on red' are words you always lived by."
	print "2) Run to the left, always a good default."
	print "3) Stand still, if you don't move she won't see you."
	
	#print "error check: variable 'food'= %s" % food
	
	a = raw_input("(Pick a number) \n > ")
	
	if a == '1' or a == 'run to the right':
		direction = 'right'
		break
		
	elif a == '2' or a == 'run to the left':
		direction = 'left'
		break
	elif a == '3' or a == 'stand still':
		dead.dead("bella 3")

	else:
		print "This is no time for typos or creativity!"
		time.sleep(1)


if direction == 'right':
	print "You scurry to the right"
	helpers.repeat('*scurry scurry*',4,0.5)
	
	if food == 'peanut':
		print "Wow you are fast, good thing you had those nutritious oreos."
		time.sleep(3)
		print "You rush towards the small ratdoor that you use every day to get to work"
		print "But oh no...you remember that your landlord installed a new lock..."
		time.sleep(5)
		
		result = lock.unlock_lock(food)
		if result == 'bella 1':
			dead.dead(result)
		else:
			print "You got the door open!"
			print "You scurry to work cus you late."
			print "The End!"
			print "**Releasing Rats**"
			end = time.time()
			rats = round((end - start)/60)
			release_rats.release(rats)
			
			
	
	elif food == 'both' or food == 'neither':
		print "You're femished"
		print "The beast is gaining on you."
		print "You have to hide"
		#enter hiding function
		
	
	


elif direction == 'left':
	print "You scurry left like no rat has ever scurried before"
	 
	helpers.repeat('*scurry scurry*',5,0.5)
	
	print "You scurry into a bucket of bacon juice"
	if food == 'peanut':
		print "You get back on your paws and take off with the speed of a rat that just ate oreros"
		helpers.repeat("*scurry*", 5, 0.33)
				
		print "But there's little hope, the beast is gaining on you"
		time.sleep(2)
		print "You reach the ratdoor that leads outside"
		time.sleep(2)
		print "But you remember the landlord installed a new lock."
		time.sleep(1.5)
		print "1) Try the password \n 2) Call the landlord 3) Face the beast"
		door_decision = raw_input("What should you do?\n > ")
		 
		if door_decision == '1':
			result = lock.unlock_lock(food)
			
			if result == 'bella1':
				dead.dead(result)
			else:
				
				print "You got the door open!"
				print "You scurry to work cus you late."
				print "The End!"
				print "**Releasing Rats**"
				time.sleep(2)
				end = time.time()
				rats = round((end - start)/60)
				release_rats.release(rats)
			
		elif door_decision == '2':
			print "no"
		elif door_decision == '3':
			dead.dead('bella1')
			
		else:
			dead.daed('bella3')
			
		#enter hiding function
	else:
		time.sleep(1.5)
		print "You're tired, covered in bacon juice"
		time.sleep(1.5)
		print "The beast is catching up to you..."
		
		helpers.repeat("*scurry*",10,0.4)
		time.sleep(2.0)
		dead.dead("bacon")