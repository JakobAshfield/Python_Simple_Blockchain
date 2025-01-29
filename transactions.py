class TransactionManager:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def new_transaction(self, sender, recipient, amount):
        return self.blockchain.new_transaction(sender, recipient, amount)
