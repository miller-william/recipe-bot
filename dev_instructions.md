## Running the Flask Backend

On macOS or Linux, run:
```bash
. venv/bin/activate
python app.py
```

Your Flask application will typically start on http://localhost:5000 unless you've configured a different port.

## Running the React Frontend
Open a New Terminal: This should be separate from the one running the Flask app.

Navigate to Your React App Directory: This is the directory where your React app was created, typically containing files like package.json.

Run the following command:
```
export NODE_OPTIONS=--openssl-legacy-provider
npm start
```

This will start the React development server, usually accessible at http://localhost:3000. Your default web browser should automatically open this URL.