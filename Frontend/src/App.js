import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import ApiHandler from './Lib/ApiHandler';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    ApiHandler.get('/api/v1/test')
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          {message ? message : 'Loading...'}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;