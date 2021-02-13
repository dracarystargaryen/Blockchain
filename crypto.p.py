import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5



"""This calls the client class using private strings"""
class Client:
    def _init_(self):
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self.signer = PKCSV1_v1_5.new(self._private_key)
    @property
    def identity(self):
        return
binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

Dinesh = Client()
print(Jane.identity)


"""This is now creating Transaction class"""
def _init_(self, sender, recipient, value):
    self.sender = sender
    self.recipient = recipient
    self.value = value
    self.time = datetime.datetime.now();


def to_dict(self):
    if self.sender == "Genesis":
        identity - "Genesis"
    else:
        identity - self.sender.identity
    
        return collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time
    })

def sign_transaction(self):
    private_key = self.sender._private_key
    signer = PKCS1_v1_5.new(private_key)
    h = SHA.new(str(self.to_dict()).encode('utf8'))
    return binascii.hexlify(signer.sign(h)).decode('ascii')

"""Testing the code"""
t = Transaction(
    Jane,
    Stan.identity,
    5.0
)

signature = t.sign_transaction()
print (signature)

"""Display Transaction"""
def display_transaction(transaction):
    #for transaction in transactions:
    dict = transaction.to_dict()
    print("sender: " + dict['sender'])
    print('-----')
    print("recipient: " + dict['recipient'])
    print('-----')
    print("value: " + str(dict['value']))
    print('----')
    print("time: " + str(dict['time']))
    print('-----')

transaction = []

Jane = Client()
Stan = Client()
Robert = Client()
Bob = Client()

t1.sign_transaction()
transactions.append(t1)

t2 = Transaction(
    Jane,
    Robert.identity,
    6.0
)

t2.sign_transaction()
transactions.append(t2)
t3 = Transaction(
    Stan,
    Jane.identity,
    2.0
)

t3.sign_transaction()
transactions.append(t3)
t4 = Transaction(
    Robert,
    Stan.identity,
    5.0
)

t4.sign_transaction()
transactions.append(t4)
t5 = Transaction(
    Bob,
    Jane.identity,
    7.0
)

t5.sign_transaction()
transactions.append(t5)
t6 = Transaction(
    Jane,
    Stan.identity,
    4.0
)

for transaction in transactions:
    display_transaction (transaction)
    print('----------------')

self.verified_transactions = []

self.previous_block_hash = " "
self.Nonce = ""

class Block:
    def _init_(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""

last_block_hash = ""

"""Creating Genesis Block"""

Jane = Client()

t0 = Transaction (
    "Genesis",
    Jane.identity,
    500.0
)

block0 = Block()

block0.previous_block_hash = None
Nonce = None

block0.verified_transactions.append (t0)

digest = hash(block0)
last_block_hash = digest

TPCoins = []

def dump_blockchain(self):
    print ("Number of blocks in the chain: " + str(len (self)))
for x in range (len(TPCoins)):
    block_temp = TPCoins[x]
    print ("block #" + str(x))
    for transaction in block_temp.verified_transactions:
        display_transaction (transaction)
        print ('-----------')
    print ('==================================')

"""Adding Blocks"""
TPCoins.append(block0)

dump_blockchain(TPCoins)


"""Creating Miners"""

def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(message, difficulty=1):
    assert difficulty >= 1
    prefix = '1' * difficulty 
    for i in range(1000):
        digest = sha256(str(hash(message)) + str(i))
        if digest.startswith(prefix):
            print("after " + str(i) + " iterations found nonce: " + digest)
        return digest


"""Adding more blocks""""
block = Block()
for i in range(3):
    temp_transaction = transactions[last_transaction_index]
    # validate transaction
    # if valid
    block.verified_transactions.append (temp_transaction)

block.previous_block_hash = last_block_hash
block.Nonce = mine (block, 2)
digest = hash (block)
TPCoins.append (block)
last_block_hash = digest

#Adding more miner's blocks
block = Block()
for i in range(3):
    temp_transaction = transaction[last_transaction_index]
    #display_transaction (temp_transaction)
    #validate miner transaction
    #if validated
    block.verified_transactions_transactions.append (temp_transaction)
    last_transaction_index _ += 1

block.previous_block_hash = last_block_hash
block.Nonce = mine (block, 2)
digest = hash (block)

TPCoins.append (block)
last_block_hash = digest

dump_blockchain(TPCoins)