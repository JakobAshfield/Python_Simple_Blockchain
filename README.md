# Blockchain API

This project implements a simple blockchain-based application with Flask for managing transactions and mining new blocks. It provides an API for performing operations such as creating transactions, mining blocks, viewing the blockchain, and resolving conflicts between nodes in a network.

## Features
- **Mine a Block**: Allow the creation of new blocks via proof of work.
- **Create Transactions**: Submit a transaction for sending cryptocurrency between users.
- **View Blockchain**: Retrieve the current state of the blockchain.
- **Register Nodes**: Add other nodes to the network to participate in consensus.
- **Resolve Conflicts**: Use the consensus algorithm to resolve blockchain conflicts by adopting the longest valid chain.

## Requirements
- Python 3.x
- Flask
- Requests

You can install the required dependencies by using `pip`:

```
pip install -r requirements.txt
```

## Installation

1. Clone the repository:
    ```bash
    git clone "<repository_url>
    ```

2. Navigate into the project directory:
    ```bash
    cd "<project_directory>
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## API Endpoints

### `/mine` (GET)
Mines a new block, rewards the miner with 1 coin, and returns the new block.

**Response:**
```json
{
    "message": "New block Forged",
    "index": "<block_index >",
    "transactions": "<list_of_transactions >",
    "proof": "<proof_of_work >",
    "previous_hash": "<previous_block_hash>"
}
```

### `/transactions/new` (POST)
Creates a new transaction. The request body must contain `sender`, `recipient`, and `amount`.

**Request Example:**
```json
{
    "sender": "<sender_address>",
    "recipient": "<recipient_address>",
    "amount": "<transaction_amount>"
}
```

**Response:**
```json
{
    "message": "Transaction will be added to Block \"<block_index>\""
}
```

### `/chain` (GET)
Returns the full blockchain along with its length.

**Response:**
```json
{
    "chain": "<list_of_blocks >",
    "length": "<blockchain_length>"
}
```

### `/nodes/register` (POST)
Registers new nodes to the blockchain network. The request body should contain a list of node addresses.

**Request Example:**
```json
{
    "nodes": ["http://<node1_address>", "http://<node2_address>"]
}
```

**Response:**
```json
{
    "message": "New nodes have been added",
    "total_nodes": "<list_of_all_nodes>"
}
```

### `/nodes/resolve` (GET)
Checks the network for longer valid chains and replaces the local chain with the longest one if necessary.

**Response:**
```json
{
    "message": "Our chain was replaced",
    "new_chain": "<new_chain_data>"
}
```

## Running the Application

To run the Flask app locally:

1. Open a terminal and navigate to the project directory.
2. Run the following command to start the server:
    ```bash
    python app.py
    ```

3. By default, the app will run on port `4500`. You can change the port by specifying a different value:
    ```bash
    python app.py --port 5000
    ```
<!--
## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.
-->

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
