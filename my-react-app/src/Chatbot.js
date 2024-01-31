import React, { useState } from 'react';
import './Chatbot.css'; // Import your CSS file

const renderMessage = (msg, index) => {
    if (msg.sender === 'chatbot') {
        // Split the message by newline and render each line, followed by a <br> tag
        return (
            <div key={index} className={`message ${msg.sender}`}>
                {msg.text.split('\n').map((line, lineIndex) => (
                    <React.Fragment key={lineIndex}>
                        {line}<br />
                    </React.Fragment>
                ))}
            </div>
        );
    } else {
        // Render user messages normally
        return (
            <div key={index} className={`message ${msg.sender}`}>
                {msg.text}
            </div>
        );
    }
};

const Chatbot = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');

    const sendMessage = async () => {
        if(input) {
            const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000'; // Fallback to localhost if not set

            try {
                // Send the message to the Flask backend
                const response = await fetch(`${apiUrl}/message`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ message: input })
                });
    
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
    
                const data = await response.json();
                // Update the chat with the chatbot's response
                setMessages(currentMessages => [...currentMessages, { text: input, sender: 'user' }, { text: data.reply, sender: 'chatbot' }]);
    
            } catch (error) {
                console.error('Fetch error:', error);
                // Optionally, handle the error in the UI as well
            }
    
            // Clear the input field
            setInput('');
        }
    };
    
    

    return (
        
        <div className="chatbot-container">
        <div className="messages">
            {messages.map((msg, index) => renderMessage(msg, index))}
        </div>
        <input 
            type="text" 
            value={input} 
            onChange={(e) => setInput(e.target.value)} 
            onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
        />
        <button onClick={sendMessage}>Send</button>
    </div>
    );
};

export default Chatbot;
