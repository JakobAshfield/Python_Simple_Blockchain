import hashlib
import json
from time import time
from utils import valid_proof, hash

class Blockchain(object):
    """
    A class to represent the Blockchain.

    The blockchain is a distributed ledger of transactions that are secured using cryptographic hash functions.
    It is structured as a chain of blocks, with each block containing a list of transactions and a reference to the previous block.
    This class manages the blockchain, including creating new blocks, adding transactions, and verifying the validity of the chain.

    Attributes:
    chain (list): List of blocks in the blockchain.
    current_transactions (list): List of current transactions to be added to the next block.
    nodes (set): Set of registered nodes in the network.
    """

    def __init__(self):
        """
        Initializes a new blockchain with a genesis block and no nodes.

        The genesis block is the first block in the chain, which is created with a predefined proof and previous hash.
        """
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Creates a new block in the blockchain.

        Args:
        proof (int): The proof of the new block.
        previous_hash (str, optional): The hash of the previous block. Defaults to None.

        Returns:
        dict: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or hash(self.chain[-1])
        }
        self.current_transactions = []  
        self.chain.append(block)  
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the list of current transactions.

        Args:
        sender (str): The sender's address.
        recipient (str): The recipient's address.
        amount (float): The amount to be transferred.

        Returns:
        int: The index of the block that will contain this transaction.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1  

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a block.

        Args:
        block (dict): The block to be hashed.

        Returns:
        str: The SHA-256 hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()  
        return hashlib.sha256(block_string).hexdigest()  

    @property
    def last_block(self):
        """
        Returns the last block in the chain.

        Returns:
        dict: The last block in the blockchain.
        """
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Calculates the proof of work for the next block.

        This method iterates through possible proofs until it finds one that satisfies the required condition 
        (a hash that meets the difficulty target).

        Args:
        last_proof (int): The proof from the previous block.

        Returns:
        int: The proof for the next block.
        """
        proof = 0
        
        while valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    def valid_chain(self, chain):
        """
        Validates a given blockchain to ensure it is properly linked and follows the consensus rules.

        Args:
        chain (list): The blockchain to be validated.

        Returns:
        bool: True if the chain is valid, False otherwise.
        """
        last_block = chain[0]  
        current_index = 1  

        while current_index < len(chain):
            block = chain[current_index]
            
            print(f'{last_block}')
            print(f'{block}')
            print("\n------------\n")
        
            if block['previous_hash'] != self.hash(last_block):
                return False

            if not valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block  
            current_index += 1
        
        return True  
