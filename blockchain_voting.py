# -*- coding: utf-8 -*-
"""
Creates a prototype blockchain that stores voting data

Created on Wed Dec  1 12:32:17 2021

@author: kurtm
"""

import hashlib
import json
from time import time

class Blockchain(object):
    '''
    Initialize variables for the blockchain
    
    @param self         object
    
    @return none
    '''
    def __init__(self):
        #This will hold blocks of votes
        self.chain = []
        #this will hold votes that are to be validated before being added to the chain
        self.pending_votes = []
        #genesis block
        self.new_block(previous_hash="This is the hash data for our genesis block", proof=100)

    '''
    Create a new block of info using a JSON object, reset the pending_votes array and append the block to the chain
    
    @var index          blocks location in the chain
    @var timestamp      exact time in which the block was made
    @var votes          votes that are in pending_votes
    @var proof          validation of votes
    @var previous_hash  takes the hash from the previous block
    
    @return             returns the new block
    '''
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'votes': self.pending_votes,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_votes = []
        self.chain.append(block)
        return block

    '''
    Find the most recent block in the chain
    
    @param self     object
    
    @return         none
    '''
    @property
    def last_block(self):
        return self.chain[-1]

    '''
    Add a vote with voter ID and candidate information to the list of pending votes
    
    @param self         object
    @param voter        voter's ID
    @param candidate    candidate voted for
    
    @return             returns the block for the new vote  
    '''
    def new_vote(self, voter, candidate):
        vote = {
            'voter': voter,
            'candidate': candidate
        }
        #add vote to the pending pool
        self.pending_votes.append(vote)
        return self.last_block['index'] + 1

    '''
    Recieve one block, turn it into a string, turn that into unicode for hashing and then hash with SHA256 encryption
    and then translate the unicode into a hexidecimal string
    
    @param self     object
    @param block    block to be hashed
    
    @return         returns the hashed block
    '''
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

    '''
    Validate the pending votes by checking that the Voter is in the voter_registry, if it is in the registry then remove it.
    if it is not in the registry flag the vote
    
    @param
    
    @return
    '''
    #def validate():
        
    