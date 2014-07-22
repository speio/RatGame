#At point in game where user deciding whether or not to eat contents of box which they
#found out contains peanut butter and oreos.
#want to know if they want to eat peanut butter or oreos, not eat any
# eat just the peanut butter, eat just the oreos, or eat both. 

def intersect_check(input):
	
##Lists for checking against
	O = ["eat", "it"]
	a = ["peanut", "peanut butter"]
	b = ["oreo", "oreos"]
	c = ["peanut", "peanut butter", "oreos", "oreo"]
	d = ["don't", "do not", "not", "no"] # negatives 
	e = ["or", "nor"] # joining
	z = ["not not", "don't not", "not don't"]

	decision = "none"

##Checking intersections
	o_o = list((set(O)) & set(input.split()))
	a_a = list((set(a)) & set(input.split()))
	b_b = list((set(b)) & set(input.split()))
	c_c = list((set(c)) & set(input.split()))
	d_d = list((set(d)) & set(input.split()))
	e_e = list(set(e) & set(input.split()))
	z_z = list(set(z) & set(input.split()))
	
##Using combinations of intersections to discern meaning
#	while decision == "none":
		#print "O %s" % o_o
		#print "a %s" % a_a
		#print "b %s" % b_b
		#print "c %s" % c_c
		#print "d %s" % d_d
		#print "e %s" % e_e 
#		input = str(raw_input("(internal)input response to check \n > "))
	
	##Checking intersections	
#		o_o = list((set(O)) & set(input.split()))
#		a_a = list((set(a)) & set(input.split()))
#		b_b = list((set(b)) & set(input.split()))
#		c_c = list((set(c)) & set(input.split()))
#		d_d = list((set(d)) & set(input.split()))
#		e_e = list(set(e) & set(input.split()))

	
	span = 2
	words = input.split(" ")
	every_2 = [" ".join(words[i:i+span]) 
	for i in range(0, len(words), span)]
	z_z = list(set(z) & set(every_2))
	
	#if double negative
	if len(z_z) >= 1 :
		#print "..."
		#time.sleep(1)
		#print "don't be a dick"
		decision = "double_negative"
		#print decision

	#If no specifics about which to eat are given
	elif len(o_o) >= 1 and len(d_d) == 0 and len(c_c) == 0:
		#print "Eat what? The box? Let's not talk like apes"
		decision = "unspecific"
		#print decision
		
	#If neither food is to be eaten
	elif len(o_o) >= 1 and len(d_d) >= 1 and len(b_b + c_c) == 0 and len(z_z) == 0:
		#print "I guess you're not eating either?"
		decision = "neither"			
		
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
					decision = "just peanut butter"
									
				else:
					decision = "oreos"	
					
			
			#negative after object assumption
			else:
				if dist_peanut > dist_oreos:
					decision = "just oreos"
				else:
					decision = "just peanut butter"	
				

	
		elif len(d_d) == 1 and len(e_e) != 0:
			#print "Not eating either"
			decision = "neither"
	
		#This probably won't be reached unless trying to input something confusing
		elif len(d_d) >= 2:
		#	print "That's a confusing way to say you are not eating either of them"
			decision = "confused neither"
		else:
		#	print "eating both"
			decision = "both"
	
	#Eating just the penut butter (no mention oreos)
	elif len(o_o) >= 1 and len(a_a) >= 1 and len(b_b) == 0:
		decision = "only peanut butter"
		
	#eating just the oreos (no mention of peanut butter)	
	elif len(o_o) >= 1 and len(b_b) >= 1 and len(a_a) == 0:
		decision = "only oreos"
					
	else:
		#print "Not sure what that means, give it another go"
		decision = "bad input"

	print decision
#user_input = str(raw_input("input response to check \n > "))
#intersect_check(user_input)			
