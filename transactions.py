class TransactionManager:
    """
    A class to manage transactions within the blockchain.

    This class is responsible for adding new transactions to the blockchain by delegating
    the responsibility to the blockchain object.

    Attributes:
    blockchain (Blockchain): The blockchain object that this transaction manager interacts with.
    """

    def __init__(self, blockchain):
        """
        Initializes the TransactionManager with the given blockchain.

        Args:
        blockchain (Blockchain): The blockchain to be managed by this transaction manager.
        """
        self.blockchain = blockchain

    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the blockchain.

        This method delegates the creation of a new transaction to the blockchain's 
        `new_transaction` method.

        Args:
        sender (str): The address of the sender of the transaction.
        recipient (str): The address of the recipient of the transaction.
        amount (float): The amount being transferred in the transaction.

        Returns:
        int: The index of the block that will contain the new transaction.
        """
        return self.blockchain.new_transaction(sender, recipient, amount)
