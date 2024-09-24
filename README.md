# finance data processing project

## Requirements
Make sure you have python and Node js installed on your system:
- [Python version 3.9.13](https://www.python.org/downloads/release/python-3913/) 
- [Node version 20](https://nodejs.org/en/download/)


## Project Setup

- Clone the repository in a local folder
    ```sh
    git clone https://github.com/OnlineNets/finance-data-processing.git 
    ```
- Open terminal and verify python version
  ```sh
    python --version
    ```
- Verify if node and npm are installed
  ```sh
    node --version
    npm -version
    ```
## Setup Backend
- Nvaigate to cloned project directory
  ```sh
    cd finance-data-processing
    ```
- Create a python virtual environment for backend
  ```sh
    python -m venv myvenv
    ```
- Activate the virtual environment
  ```sh
  # For winodws
    myvenv\Scripts\activate
  # For linux
    source myvenv/bin/activate
    ```
- Install python libraries
  ```sh
   cd backend
   pip install -r requirements.txt
   python -m pip install -U channels["daphne"]
   pip install redis channels_redis
    ```
  - Start Django server
    ```sh
    python manage.py runserver
      ```
  - Django backend server will start on http://localhost:8000/
  - Start Websocket
    ```sh
    python crypto_data.py
      ```

## Setup Frontend
- Open a new terminal and navigate to frontend directory
  ```sh
   cd smwa-project/frontend
    ```
- Install frontend libraries using npm
  ```sh
   npm install
    ```
- Start Node server
  ```sh
   npm start
    ```
- Once node is started you can access the application on http://localhost:3000/
