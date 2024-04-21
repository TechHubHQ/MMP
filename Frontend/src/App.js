import { Camera, User } from 'react-feather';
import React, { useEffect, useState } from 'react';
import ApiHandler from './Lib/ApiHandler';
import Header from './Components/Header';
import Footer from './Components/Footer';
import "./Assets/Styles/GlowEffect.css"
import heroImage from './Assets/Images/hero-image.jpg';


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
    <div className="App bg-gray-900 text-white">
      <Header />
      <main>
        <section className="hero py-20">
          <div className="container mx-auto px-4">
            <div className="hero-content flex flex-col md:flex-row items-center justify-between">
              <div className="md:w-1/2">
                <h1 className="text-4xl font-bold mb-4">Capture Life's Moments</h1>
                <p className="text-lg mb-8">Moments Made Photography specializes in capturing the beauty of life's precious moments.</p>
                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Book a Session</button>
              </div>
              <div className="md:w-1/2">
                <img src={heroImage} alt="Hero" className="rounded-lg shadow-lg glow-effect" />
              </div>
            </div>
          </div>
        </section>
        <section className="services py-20">
          <div className="container mx-auto px-4">
            <h2 className="text-3xl font-bold mb-8 text-center">Our Services</h2>
            <div className="service-cards grid grid-cols-1 md:grid-cols-3 gap-8">
              <div className="service-card bg-gray-800 rounded-lg shadow-lg p-6 hover:bg-gray-700 transition-colors duration-300 glow-effect">
                <Camera className="w-16 h-16 mb-4 text-blue-500" />
                <h3 className="text-xl font-bold mb-2">Wedding Photography</h3>
                <p className="text-gray-300">Capture the love and joy of your special day with our professional wedding photography services.</p>
              </div>
              {/* Add more service cards here */}
            </div>
          </div>
        </section>
        <section className="testimonials py-20">
          <div className="container mx-auto px-4">
            <h2 className="text-3xl font-bold mb-8 text-center">What Our Clients Say</h2>
            <div className="testimonial-cards grid grid-cols-1 md:grid-cols-3 gap-8">
              <div className="testimonial-card bg-gray-800 rounded-lg shadow-lg p-6 hover:bg-gray-700 transition-colors duration-300 glow-effect">
                <User className="w-16 h-16 rounded-full mb-4 mx-auto text-blue-500" />
                <p className="text-gray-300 mb-4">"The team at Moments Made Photography did an excellent job capturing the essence of our special day. We are thrilled with the beautiful photos!"</p>
                <h4 className="text-lg font-bold text-center">John and Jane Doe</h4>
              </div>
              {/* Add more testimonial cards here */}
            </div>
          </div>
        </section>
        <section className="message py-20">
          <div className="toast">
            <div className="alert alert-info">
              <span>{message || 'Loading...'}</span>
            </div>
          </div>          
        </section>
      </main>
      <Footer />
    </div>
  );
}

export default App;