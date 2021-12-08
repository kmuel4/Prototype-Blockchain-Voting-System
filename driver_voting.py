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
# #Create new votes for pending_votes
# v1 = blockchain.new_vote("Person2", "Indipendant")
# #create new block of pending votes, encryption 67890
# blockchain.new_block(v1)

# v2 = blockchain.new_vote("Person3", "Democrat")
# #create new block
# blockchain.new_block(v2)

# # v3 = blockchain.new_vote("Person3", "Democrat")
# # v4 = blockchain.new_vote("Person4", "Republican")
# # v5 = blockchain.new_vote("Person5", "Indipendant")

# #print the new blocks
# print("\nBlock 2:\n", blockchain.chain[1])
# print("\nBlock 3:\n", blockchain.chain[2])

'''
auto generated blockchain test
'''
stdin = 1
while(stdin == 1):
    stdin = input("[1] to vote\n[0] to quit\n")
    
    v = input("\nVoter ID: ")
    c = input("\nCandidate: ")
    v1 = blockchain.new_vote(v, c)
    blockchain.new_block(v1)
    

    
    
    