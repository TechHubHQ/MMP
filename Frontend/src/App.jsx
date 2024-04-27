/* eslint-disable no-unused-vars */
import React, { useEffect, useState } from 'react';
import ApiHandler from './Lib/APIHandler';
import Header from './Components/Header';
import Footer from './Components/Footer';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    ApiHandler.get('/api/v1/test')
      .then(response => {
        console.log("Api Response", response.data);
        setMessage(response.data.message);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <>
      <Header />
      <div>
        <span>{message}</span>
      </div>
      <Footer />
    </>
  );
}

export default App
