# -*- coding: utf-8 -*-
"""
Driver for blockchain_voting.py

Created on Wed Dec  1 12:38:13 2021

@author: kurtm
"""

from blockchain_voting import Blockchain
blockchain = Blockchain()

'''
manual input for testing the blockchain
'''
print("This is the chain with only the genesis block, block 0:\n ", blockchain.chain)

#Create new votes for pending_votes
v1 = blockchain.new_vote("Person2", "Indipendant")
#create new block of pending votes, encrypt using itself
print("\nAfter casting a vote, pending_votes stores it:\n", blockchain.pending_votes)
blockchain.new_block(v1)
#print the new blocks
print("\nAfter creating the new block, it is added to the chain\n", blockchain.chain[1])

v2 = blockchain.new_vote("Person3", "Democrat")
v3 = blockchain.new_vote("Person4", "Republican")
v4 = blockchain.new_vote("Person5", "Indipendant")
blockchain.new_block(v1+v2+v3+v4)

print("\nThe contents of Block 2 with 3 votes:\n", blockchain.chain[2])

print("\nNow lets simulate the voting process.\n")

print("\nPlease look at the camera before proceeding...\n")

'''
this is where we will have the facial recognition function go. it should recognize the face before proceeding

@param  none

@return voter ID
'''
candidate = input("Please cast your vote: ")
v5 = blockchain.new_vote("12345", "candidate")

print("\nNext there is a function for closing the polling booth. This function takes all pending votes and adds them to the blockchain.")

#this is a temporary version of that function
blockchain.new_block(v5)

print("\nAs you can see, pending_votes is now empty: ", blockchain.pending_votes)









    
    
    