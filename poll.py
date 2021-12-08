import random
import names

candidates = []
candidate = ""


#Take candidates to set up poll
def set_candidates():
	while(True):
		candidate = input("Enter a candidate (Enter 0 to quit): ")
		
		if candidate == "0":
			if len(candidates) < 2:
				print("Must have more than 1 candidate")
			else: 
				break
		
		if candidate != "":
			candidates.append(candidate)

#make a list of valid ids
def set_ids():
	valid_ids = open("valid ids.txt", "w")
	ID = 0
	IDs = []
	i = 0

	while i < 49999999:
		ID = '{:0>8}'.format(random.randrange(1, 99999999))
		while ID in IDs:
			ID = '{:0>8}'.format(random.randrange(1, 99999999))
		valid_ids.write(str(ID) + "\n")
		i+=1

	valid_ids.close	

#Make voters and vote
def set_voters():
	voter_reg = open("voter registry.txt", "w")
	ID = 0
	IDs = []
	name = ""
	vote = 0	
	i = 0

	num_voters = int(input("How many voters?: "))

	while(i < num_voters):
		ID = '{:0>8}'.format(random.randrange(1, 99999999))
		while ID in IDs:
			ID = '{:0>8}'.format(random.randrange(1, 99999999))
		IDs.append(ID)

		name = names.get_full_name()
		vote = candidates[random.randrange(0, len(candidates))]
				
		voter_reg.write(str(ID) + ", " + name + ", " + vote + "\n")	
		i+=1

	voter_reg.close()


choice = int(input("What would you like to run?\n\n[1] set_candidates\n[2] set_ids\n[3] set_voters\n"))

if choice == 1: set_candidates()
if choice == 2: set_ids()
if choice == 3: set_voters()