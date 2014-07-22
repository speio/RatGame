import time
import helpers_helpers
import dead
#At point in game where user deciding whether or not to eat contents of box which they
#found out contains peanut butter and oreos.
#want to know if they want to eat peanut butter or oreos, not eat any
# eat just the peanut butter, eat just the oreos, or eat both. 

def intersect_check(input):
	
##Lists for checking against
	O = ["eat", "it", "them"]
	a = ["peanut", "peanut butter"]
	b = ["oreo", "oreos"]
	c = ["peanut", "peanut butter", "oreos", "oreo"]
	d = ["don't", "do not", "not", "no"] # negatives 
	e = ["or", "nor"] # joining
	f = ["box"]
	z = ["not not", "don't not", "not don't"]


##Checking intersections
	o_o = list((set(O)) & set(input.split()))
	a_a = list((set(a)) & set(input.split()))
	b_b = list((set(b)) & set(input.split()))
	c_c = list((set(c)) & set(input.split()))
	d_d = list((set(d)) & set(input.split()))
	e_e = list(set(e) & set(input.split()))
	f_f = list(set(f) & set(input.split()))

	span = 2
	words = input.split(" ")
	every_2 = [" ".join(words[i:i+span]) 
	for i in range(0, len(words), span)]
	z_z = list(set(z) & set(every_2))
	
	#if eating box
	if len(f_f) == 1 and len(o_o) >= 1 and (len(c_c) + len(b_b)) == 0:
		return "box"
	
	
	
	#if double negative
	if len(z_z) >= 1 :
		#print "..."
		#time.sleep(1)
		#print "don't be a dick"
		return "double_negative"

	#If no specifics about which to eat are given
	elif len(o_o) >= 1 and (len(d_d) + len(c_c)) == 0:
		#print "Eat what? The box? Let's not talk like apes"
		return "unspecific"
		
	#If neither food is to be eaten
	elif len(o_o) >= 1 and len(d_d) >= 1 and len(b_b + c_c) == 0 and len(z_z) == 0:
		#print "I guess you're not eating either?"
		return "neither"			
		
	#Trying to figure out what to do if both oreo and peanut included in input		
	elif len(c_c) > len(b_b) and len(c_c) > len(a_a): #if 
		#error check> print "included peanut and oreo in input"
	
		#list of negatives not empty but two weren't used and no joining words used
		#implying input is using both items but wants opposite actions attached to each
		if len(d_d) != 0 and len(d_d) < 2 and len(e_e) == 0:
			#error check> print "eating only one of them"
			input_list = list(input.split())
			
			#finding the index of the negative
			index = 0
			found = "no"
			while found != "yes":
				
				if input_list[index] in d:
					#error check> print "found index of negative"
					i_negative = index
					found = "yes"
					 
				else:
					found = "no"
					index = index + 1
					
			#finding index of peanut 
			index = 0
			found = "no"
			while found != "yes":
				
				if input_list[index] in a:
					#error check> print "found index of peanut"
					i_peanut = index
					
					#getting distance between peanut and negative
					dist_peanut = i_peanut - i_negative
					found = "yes"
					 
				else:
					found = "no"
					index = index + 1
					
			#finding index of oreos
			index = 0
			found = "no"
			while found != "yes":
				
				if input_list[index] in b:
					#erro check> print "found index of oreos"
					i_oreos = index
					
					#getting distance between oreos and negative
					dist_oreos = i_oreos - i_negative
					found = "yes"
					 
				else:
					found = "no"	
					index = index + 1
			
			#negative before object assumption
			if i_negative < i_peanut and i_negative < i_oreos:
				
				if dist_peanut > dist_oreos:
					return "peanut butter"
									
				else:
					return "oreos"	
					
			
			#negative after object assumption
			else:
				if dist_peanut > dist_oreos:
					return "oreos"
				else:
					return "peanut butter"	
				

	
		elif len(d_d) == 1 and len(e_e) != 0:
			#print "Not eating either"
			return "neither"
	
		#This probably won't be reached unless trying to input something confusing
		elif len(d_d) >= 2:
		#	print "That's a confusing way to say you are not eating either of them"
			return "confused neither"
		else:
		#	print "eating both"
			return "both"
	
	#Eating just the penut butter (no mention oreos)
	elif len(o_o) >= 1 and len(a_a) >= 1 and len(b_b) == 0:
		return "peanut butter"
		
	#eating just the oreos (no mention of peanut butter)	
	elif len(o_o) >= 1 and len(b_b) >= 1 and len(a_a) == 0:
		return "oreos"
					
	else:
		#print "Not sure what that means, give it another go"
		return "bad input"

##Landlord
def landlord():	
	print "\"I'm pretty sure I said (y/n) meaning choose \"yes\" \"no\" by typing y or n \""
	#.sleep(2)
	print "..."
	#.sleep(0.5)
	print "\"but now we are here, so I'll tell you about myself.\""
	#.sleep(0.8)
	print "\"but first tell me this\""
	#.sleep(0.9)
	
	#beginning riddel  
	answer = "none"
	while answer == "none":
		response = str(raw_input("\"How's a how to tell a who that it's the one to do a thing?\" \n >"))
		
		if len(list(set(["ask", "Ask"]) &  set(response.split()))) != 0:
			answer = "ask"
			print "\"Dang, that was too easy.\""
			time.sleep(0.9)
			print "\"I'm your damn landlord\""
			time.sleep(0.7)
			print " \"Please try and be here next time you get a packages. \""
			time.sleep(0.7)
			print " \" But again, just call me if you need anything. \" "			
			time.sleep(1)
			while True:
				print "Do you need my number?"
				number = raw_input("(y/n) \n > ")
				if number == 'n':
					print "Okay good."
					print "See you later, take care of Bella." #Both knowing Bella's name
					#and getting the landlords number in this tangent can allow escape from last room
					#but player must remember them, no saved items or variables are applied, 
					time.sleep(2)
					break
				elif number == 'y':				
					# open a public URL
					url = "http://youtu.be/Rk0iT7egdd4"
					webbrowser.open_new(url)
					break
				else:
					print " \" %s \" \n idk what that means. " % number
			output = ("Ratzo",2)
			return(output)
		
		else:
			print "Try reading it again."



def repeat(f, n, sleep):
	x = 0
	while x != (n):
		print "%s" % f
		time.sleep(sleep)
		x = x + 1

##Tangents possible after having the package##	
def openpackage(yesno): ##Automatically enters the YES open package if no input%%%%%%%%

	if yesno == "no":
		
		while True: 
			second_yesno = raw_input("Should you hold on to the package still? \n (y/n) > ")
			
			if second_yesno == 'y':
				print "Okay, sounds good"
				time.sleep(1)
				print "Maybe you can hurl it at a monster or something and run for your life, Ha!"
				break
			
			elif second_yesno == 'n':
				print "You throw the package back onto the bed."
				#.sleep(2)
				print "HOLY SHIT"
				#.sleep(2)
				print "YOU KNOCKED OVER THE CANDLE"
				#.sleep(1)
				dead.dead("fire")
			else:
				print "%s \n wuz diz mean?" % second_yesno	
		#Possible to return from this function: "unopened" package, 
		return("unopened")
			
	

	elif yesno == "yes":
		#from helpers_helpers import yes_open
		#This just comes back here without setting any variables after making them guess
		#what is in the box, there are no tangents or deaths from this function
		helpers_helpers.yes_open()
		
		result = ("default","default", "default")
		round = 1
		while result[2]!= 'continue':
			print "What should you do with the delicious peanut butter and scrumptious oreos?"
			eat = raw_input("> ")
			eat = intersect_check(input)
			result = eating(eat)
			
		if result[0] == "dead":
			dead.dead(result[1])
		else:
			return(result)	
		
		
		#deciphering input on what to "do" with the food items 
		#from helpers import yes_open


