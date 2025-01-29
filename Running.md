
# How to Run the Python Simple Blockchain

This guide will walk you through how to run the Python Simple Blockchain project on your local machine.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- Pip (Python package manager): [Install pip](https://pip.pypa.io/en/stable/installation/)

## Setting Up the Project

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/JakobAshfield/Python_Simple_Blockchain.git
   cd Python_Simple_Blockchain
   ```

2. Install the required dependencies using `pip`:

   If you don't have `pip` installed, install it first and then run the following:

   ```bash
   pip install -r requirements.txt
   ```

   This will install any dependencies that the project requires.

## Running the Application

To run the blockchain app, use the following command:

```bash
python app.py --http:4500
```

### Explanation:
- `app.py`: The Python script that runs the application.
- `--http:4500`: Specifies the port number (4500 in this case). You can replace `4500` with any port number of your choice (e.g., `--http:5000`).

Once the app starts, you should see logs in the terminal, and the application will be accessible at `http://localhost:4500` (or the port you've set).

## Adding Another Node

To add another node to the blockchain, simply run another instance of `app.py` with a different port number and/or address:

```bash
python app.py --http:5000
```

This will start another instance of the blockchain node.

## Testing the Endpoints

You can interact with the blockchain via the following endpoints using tools like **curl** or **Postman**:

### Example with `Postman`

1. **Mine a new block**
![Screenshot 2025-01-29 at 12 37 32 PM](https://github.com/user-attachments/assets/fad24c3f-745d-4ef3-a93b-5ac51eabd18e)

2. **Mine a new block on a different node**
![Screenshot 2025-01-29 at 12 37 53 PM](https://github.com/user-attachments/assets/22867513-d472-4f0a-b508-7b37efb56782)

3. **Get the blockchain data**
![Screenshot 2025-01-29 at 12 38 03 PM](https://github.com/user-attachments/assets/c4c15ebe-b756-484e-b6ae-ff0421e7488d)

4. **Register a new node**
![Screenshot 2025-01-29 at 12 38 26 PM](https://github.com/user-attachments/assets/2e6b7aae-c802-4504-b8f4-84783c2671cc)

You may need to add a new header like the one below (all Post requests):
![Screenshot 2025-01-29 at 12 38 15 PM](https://github.com/user-attachments/assets/55cb904b-b998-4d29-a466-29f48cc8c744)

5. **Resolve the block chain**
![Screenshot 2025-01-29 at 12 38 39 PM](https://github.com/user-attachments/assets/c948d9cf-5760-4c83-be9f-077f7e670c53)

6. **Add a new transaction**
![Screenshot 2025-01-29 at 12 41 34 PM](https://github.com/user-attachments/assets/a80a3610-9be2-4b7f-9ba7-99d9a4125078)


### Example with `curl`:

1. **Get the blockchain data**:

   ```bash
   curl http://localhost:4500/Blockchain
   ```

2. **Mine a new block**:

   ```bash
   curl -X POST http://localhost:4500/mine
   ```

3. **Add a new transaction**:

   ```bash
   curl -X POST http://localhost:4500/transactions/new -d '{"sender": "A", "recipient": "B", "amount": 5}'
   ```

Make sure to replace the address and port number if you're interacting with another node in the network (e.g., `http://localhost:5000`).

## Troubleshooting

If you run into any issues or need additional help, please refer to the Issues section of this repository or contact the repository owner.
