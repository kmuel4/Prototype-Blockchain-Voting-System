# -*- coding: utf-8 -*-
"""
Driver for blockchain_voting.py

Created on Wed Dec  1 12:38:13 2021

@author: kurtm
"""

import poll
import time
#import FacialRecognition
from blockchain_voting import Blockchain
blockchain = Blockchain()


'''manual testing of blockchain contents'''
# print("\nThis is the chain with only the genesis block, block 0:\n ", blockchain.chain)

# #Create new votes for pending_votes
# v1 = blockchain.new_vote("Person1", "Independant")
# print("\nThis is an example of a vote:  Person1, Independant")
# #create new block of pending votes, encrypt using itself
# print("\nAfter casting a vote, it is stored in pending_votes:\n", blockchain.pending_votes)
# blockchain.new_block(blockchain.chain[0])
# #print the new blocks
# print("\nAfter creating the new block, everything in pending_votes is added to the chain\n", blockchain.chain[1])

# v2 = blockchain.new_vote("Person3", "Independant")
# blockchain.new_block(v1)

# print("\nThe contents of Block 2 with three simulated votes:\n", blockchain.chain[2])

stdin = input("\nVoting initiated. Press any key to begin facial identification:   ")
print(">------------------------------------------------------------------<\n")
#lines 38-41 for demonstration purposes
print("Angle your head left...")
time.sleep(2)
print("Angle your head right...")
time.sleep(2)


'''voter_name is where we impliment faical recognition, it recognizes the user and finds the name as a string'''
# voter_name = (return from facial recognition)

'''poll.validate_name then finds out if the scanned name is in the registry and returns a boolean into valid_name'''
# valid_name = poll.validate_name(voter_name)
# if(valid_name == false):
#     print("\nFace not recognized. Your booth has been flagged.")

print("\nApproved.")

print("\n>------------------------------------------------------------------<")
time.sleep(1)
voter_id = input("Enter your voter ID:  ")
print("Validating...")
time.sleep(2)

#poll.validate_id checks to make sure the voter ID inputted is in the voter registry
#and prints the associated name
valid_id = poll.validate_id(voter_id)
print("\n>------------------------------------------------------------------<")
#if the inputted ID is in the voter registry, continue to voting
'''need to add in a check if voter_id and voter_name are on the same line'''
if(valid_id == True ):
    time.sleep(1)
    candidate = input("Please cast your vote: ")
    v5 = blockchain.new_vote(voter_id, candidate)
    #submit the blocks
    blockchain.new_block(proof=50)
    print("Vote submitted.")
else:
    print("\nInvalid voter ID. Your booth has been flagged.")
print("\n>------------------------------------------------------------------<")
    
'''more testing'''
#print("This is the block we submitted:\t", blockchain.chain[1])
# print("\nWhen the polling booth is closed, a new block is created to store all votes in pending_votes.\n", blockchain.pending_votes)
# print("\nAs you can see, pending_votes is now an empty array")









    
    
    