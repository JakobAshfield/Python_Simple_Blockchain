import hashlib
import json

def valid_proof(last_proof, proof):
    """
    Validates the proof of work for the blockchain.

    This function checks if the hash of the concatenation of the last proof and the current proof
    starts with four leading zeros, which is the required condition for the proof of work.

    Args:
    last_proof (int): The proof of the previous block.
    proof (int): The proof being validated.

    Returns:
    bool: True if the proof is valid, False otherwise.
    """
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"

def hash(block):
    """
    Generates the hash of a given block.

    This function converts the block to a JSON string, sorts the keys, encodes it, and then
    computes the SHA-256 hash of the string.

    Args:
    block (dict): The block to be hashed.

    Returns:
    str: The SHA-256 hash of the block.
    """
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()
