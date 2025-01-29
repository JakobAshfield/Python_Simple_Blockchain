import requests
from urllib.parse import urlparse
from blockchain import Blockchain

class NodeManager:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def register_node(self, address):
        parsed_url = urlparse(address)
        self.blockchain.nodes.add(parsed_url.netloc)

    def resolve_conflicts(self):
        neighbours = self.blockchain.nodes
        print(f"Registered nodes: {neighbours}")
        new_chain = None
        max_length = len(self.blockchain.chain)

        for node in neighbours:
            response = requests.get(f'http://{node}/chain')
            print(f"Checking chain from node {node}")

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                print(f"Received chain from node {node} with length {length}")

                if length > max_length and self.blockchain.valid_chain(chain):
                    max_length = length
                    new_chain = chain
                    print("Found longer valid chain, updating...")

        if new_chain:
            self.blockchain.chain = new_chain
            print("Chain updated with the longer one")
            return True

        print("No valid chain found to replace")
        return False