## Prerequisites
Before running the application locally, ensure you have the following prerequisites installed:

- Python
- Node.js and npm
- An OpenAI API key

## Getting started
### Cloning the repo
First, clone the repository to your local machine:

```bash
git clone https://github.com/miller-william/recipe-bot.git
cd recipe-bot
```

### Installing dependencies
#### For the Flask backend

Navigate to the Flask App directory:
Assuming the Flask app is in the root directory:

```bash
cd path/to/flask_app  # Adjust the path as necessary
```

Create a virtual environment (optional but recommended):

On macOS or Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

#### For the React frontend
Navigate to the React app directory:
Assuming the React app is in a subdirectory (e.g., my_react_app):

```bash
cd path/to/my_react_app  # Adjust the path as necessary
```

Install Node Modules:

```bash
npm install
```

This sets up both the Flask backend and the React frontend on your local machine, ready for running and further development.

## Environment setup
### Setting up environment variables
#### For the Flask backend

In the root directory of your Flask app (where app.py is located), create a file named `.env`.

Add Your OpenAI API Key:

```
OPENAI_API_KEY=your_openai_api_key
```
#### For the React frontend
Navigate to Your React app directory: This is where your React app is located, typically containing package.json.
In this directory, create a file named .env.

Set the Backend URL:
```
REACT_APP_API_URL=http://localhost:5000
```
Use the appropriate URL if your Flask app is running on a different port.

## Running the Flask backend

On macOS or Linux, run:
```bash
. venv/bin/activate
python app.py
```

Your Flask application will typically start on http://localhost:5000 unless you've configured a different port.

## Running the React frontend
Open a new terminal. This should be separate from the one running the Flask app.

Navigate to your React app directory. This is the directory where your React app was created, typically containing files like package.json.

Run the following command:
```
npm start
```

If you have SSL related errors, you may need to run the following first:
```
export NODE_OPTIONS=--openssl-legacy-provider 
```

This will start the React development server, usually accessible at http://localhost:3000. Your default web browser should automatically open this URL.
