import random
import names
#may have to do "pip install names"

candidates = []

"""
	Takes candidates from user to set up poll until the user enters 0.
	Valid candidates are added to an array for future use.
"""
def set_candidates():
	global candidates
	while(True):
		candidate = input("Enter a candidate (Enter 0 to quit): ")
		
		if candidate == "0":
			if len(candidates) < 2:
				#Since there can be no poll without more than one option, 
				#user must enter more than one candidate.
				print("Must have more than 1 candidate")
			else: 
				break
		
		#Also checks to see if the user accidently entered nothing.
		if candidate != "":
			candidates.append(candidate)

"""
	Creates a list of votes with a valid ID and some votes without valid IDs
"""
def make_votes():
	valid_ids = open("valid ids.txt", "w")
	voter_reg = open("voter registry.txt", "w")
	ID = 0
	IDs = []
	name = ""
	vote = 0	
	i = 0
	j = 0

	num_voters = int(input("How many voters? "))

	#Create voters with valid IDs
	while(i < num_voters):
		#Create a unique ID by checking against array of used IDs
		ID = '{:0>8}'.format(random.randrange(1, 99999999))
		while ID in IDs:
			ID = '{:0>8}'.format(random.randrange(1, 99999999))
		IDs.append(ID)
	
		#Add ID to list of valid IDs
		valid_ids.write(str(ID) + "\n")

		#Create name and vote from available candidates
		name = names.get_full_name()
		vote = candidates[random.randrange(0, len(candidates))]
		
		#Add voter to the registry		
		voter_reg.write(str(ID) + ", " + name + ", " + vote + "\n")	
		i+=1

	#Add extra voters without valid IDs
	while(j < num_voters/10):
		#Create a unique ID by checking against array of used IDs
		ID = '{:0>8}'.format(random.randrange(1, 99999999))
		while ID in IDs:
			ID = '{:0>8}'.format(random.randrange(1, 99999999))
		IDs.append(ID)

		#Create name and vote from available candidates
		name = names.get_full_name()
		vote = candidates[random.randrange(0, len(candidates))]
		
		#Add voter to the registry		
		voter_reg.write(str(ID) + ", " + name + ", " + vote + "\n")		
		j+=1

	valid_ids.close()
	voter_reg.close()

"""
	Manually add a new voter
"""
def add_voter():
	valid_ids = open("valid ids.txt", "a")
	voter_reg = open("voter registry.txt", "a")
	ID = 0
	IDs = []

	name = input("Please enter the voters name: ")
	
	#Create a unique ID by checking against array of used IDs
	ID = '{:0>8}'.format(random.randrange(1, 99999999))
	while ID in IDs:
		ID = '{:0>8}'.format(random.randrange(1, 99999999))
	IDs.append(ID)

	voter_reg.write(str(ID) + ", " + name + "\n")

	valid_ids.write(str(ID) + "\n")

	valid_ids.close()
	voter_reg.close()
	

"""
	Validate voter with given id
"""
def validate_id(given_id):
	sline = ""
	valid = False
	voter_reg = open("voter registry.txt", "r")

	for line in voter_reg:
		sline = line.split(", ")
		if sline[0] == given_id:
			print("Welcome " + sline[1])
			valid = True
	
	voter_reg.close()
	return valid

"""
	Validate voter with given name
"""	
def validate_name(given_name):
	sline = ""
	voter_reg = open("voter registry.txt", "r")

	for line in voter_reg:
		sline = line.split(", ")
		if sline[1] == given_name:
			print("Welcome " + sline[1])
			return sline[0]

	voter_reg.close()



# Following code is for testing purposes
"""
while(True):
	choice = int(input("What would you like to run? (enter 0 to quit)\n"+
		"[1] set_candidates\n"+
		"[2] make_votes\n"+
		"[3] add_voter\n"+
		"[4] validate_id\n"+
		"[5] validate_name\n\n"))

	if choice == 0: break
	if choice == 1: set_candidates()
	if choice == 2: make_votes()
	if choice == 3: add_voter()
	if choice == 4:
		validate_id(input("Enter an id: "))
	if choice == 5:
		validate_name(input("Enter a name: "))
"""