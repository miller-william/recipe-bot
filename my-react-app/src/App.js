import React from 'react';
import './App.css';
import Chatbot from './Chatbot'; // Import your Chatbot component

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Recipe Bot</h1>
        <Chatbot /> {/* Include the Chatbot component */}
      </header>
    </div>
  );
}

export default App;
