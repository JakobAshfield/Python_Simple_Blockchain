from flask import Flask, jsonify, request
from uuid import uuid4
from blockchain import Blockchain
from node import NodeManager
from transactions import TransactionManager

app = Flask(__name__)
node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()
node_manager = NodeManager(blockchain)
transaction_manager = TransactionManager(blockchain)

@app.route('/mine', methods=['GET'])
def mine():
    """
    Mines a new block and adds it to the blockchain.

    This function retrieves the last block, calculates the proof of work, 
    creates a new transaction (rewarding the miner), and creates a new block 
    with the proof and previous block hash. The newly mined block is then 
    returned in the response.

    Returns:
    Response: A JSON response with the details of the newly mined block.
    """
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    transaction_manager.new_transaction(sender="0", recipient=node_identifier, amount=1)
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }

    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    Creates a new transaction and adds it to the blockchain.

    This function accepts transaction details (sender, recipient, amount) 
    through a POST request. It then validates the required values and 
    creates a new transaction. The transaction is added to the list 
    of current transactions and will be included in the next block.

    Returns:
    Response: A JSON response with a message indicating the transaction 
    will be added to the next block.
    """
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400
    index = transaction_manager.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """
    Returns the full blockchain.

    This function provides the entire chain of blocks in the blockchain, 
    including the length of the chain.

    Returns:
    Response: A JSON response containing the blockchain and its length.
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    """
    Registers new nodes to the blockchain network.

    This function allows other nodes to register themselves with the blockchain 
    network. The request must contain a list of node addresses. Each address 
    is parsed and added to the set of registered nodes.

    Returns:
    Response: A JSON response confirming the nodes were added successfully.
    """
    values = request.get_json()
    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400
    for node in nodes:
        node_manager.register_node(node)
    response = {'message': 'New nodes have been added', 'total_nodes': list(blockchain.nodes)}
    return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    """
    Resolves conflicts in the blockchain network.

    This function is responsible for checking the registered nodes for any 
    longer valid chains. If a longer chain is found, the current chain is 
    replaced with the new chain. This helps maintain consensus in the network.

    Returns:
    Response: A JSON response indicating whether the chain was replaced 
    or is already authoritative.
    """
    replaced = node_manager.resolve_conflicts()
    if replaced:
        response = {'message': 'Our chain was replaced', 'new_chain': blockchain.chain}
    else:
        response = {'message': 'Our chain is authoritative', 'chain': blockchain.chain}
    return jsonify(response), 200

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--port', default=4500, type=int, help="Port to listen on")
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port)
