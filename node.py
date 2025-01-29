import requests
from urllib.parse import urlparse

class NodeManager:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def register_node(self, address):
        parsed_url = urlparse(address)
        self.blockchain.nodes.add(parsed_url.netloc)

    def resolve_conflicts(self):
        neighbours = self.blockchain.nodes
        new_chain = None
        max_length = len(self.blockchain.chain)

        for node in neighbours:
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.blockchain.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.blockchain.chain = new_chain
            return True
        return False
