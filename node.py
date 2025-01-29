import requests
from urllib.parse import urlparse
from blockchain import Blockchain

class NodeManager:
    """
    A class to manage the nodes in the blockchain network.

    This class is responsible for registering new nodes, resolving conflicts between nodes by
    comparing and updating the blockchain, and ensuring that the network operates with the longest
    valid blockchain.

    Attributes:
    blockchain (Blockchain): The blockchain object that this NodeManager is responsible for managing.
    """

    def __init__(self, blockchain):
        """
        Initializes the NodeManager with the given blockchain.

        Args:
        blockchain (Blockchain): The blockchain to be managed by this node manager.
        """
        self.blockchain = blockchain

    def register_node(self, address):
        """
        Registers a new node to the blockchain network.

        This method parses the provided address and adds the node's network location (host:port) to the list of
        registered nodes in the blockchain.

        Args:
        address (str): The address of the node to be registered, in the format 'http://<host>:<port>'.
        """
        parsed_url = urlparse(address)
        self.blockchain.nodes.add(parsed_url.netloc)

    def resolve_conflicts(self):
        """
        Resolves conflicts in the blockchain network by checking for the longest valid chain among the registered nodes.

        This method compares the local blockchain to those from other nodes in the network, and if it finds a longer
        valid chain, it replaces the local chain with the longer one. This helps achieve consensus across the network
        when multiple chains exist.

        Returns:
        bool: True if the chain was updated with a longer valid one, False otherwise.
        """
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
