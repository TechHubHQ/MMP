import Header from '../Components/Header';
import Footer from '../Components/Footer';

function LandingPage() {
  return (
    <div className="relative">
      <Header />
      <main>
        {/* Hero Section */}
        <div className="hero min-h-screen bg-base-200 glow">
          <div className="hero-content text-center">
            <div className="max-w-md">
              <h1 className="text-5xl font-bold">Capture Timeless Moments</h1>
              <p className="py-6">
                Elevate your special occasions with our professional photography services.
              </p>
              <button className="btn btn-primary">Book Now</button>
            </div>
          </div>
        </div>
        {/* Services Section */}
        <div className="bg-base-100 py-12">
          <div className="container mx-auto px-4">
            <h2 className="text-3xl font-bold mb-8 text-center">Our Services</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              <div className="card bg-base-100 shadow-xl glow-card">
                <figure>
                  <img src="../../src/assets/Images/wedding-photography.jpg" alt="Wedding Photography" />
                </figure>
                <div className="card-body">
                  <h2 className="card-title">Wedding Photography</h2>
                  <p>
                    Capture the love and joy of your special day with our expert wedding photographers.
                  </p>
                </div>
              </div>
              <div className="card bg-base-100 shadow-xl glow-card">
                <figure>
                  <img src="../../src/assets/Images/portrait-photography.jpg" alt="Portrait Photography" />
                </figure>
                <div className="card-body">
                  <h2 className="card-title">Portrait Photography</h2>
                  <p>
                    Showcase your personality and style with our professional portrait photography services.
                  </p>
                </div>
              </div>
              <div className="card bg-base-100 shadow-xl glow-card">
                <figure>
                  <img src="../../src/assets/Images/event-photography.jpg" alt="Event Photography" />
                </figure>
                <div className="card-body">
                  <h2 className="card-title">Event Photography</h2>
                  <p>
                    Preserve the memories of your corporate events, parties, and celebrations with our expert event photographers.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}

export default LandingPage;