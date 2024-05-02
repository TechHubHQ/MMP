import Header from '../Components/Header';
import Footer from '../Components/Footer';
import '../assets/Styles/glow-effect.css';

function LandingPage() {
  return (
    <div className="relative">
      <Header />
      <main>
        {/* Hero Section */}
        <div className="hero min-h-screen bg-base-200 glow">
          <div className="hero-content text-center">
            <div className="max-w-md">
              <h1 className="text-5xl font-bold">Capture Life&#39;s Moments</h1>
              <p className="py-6">
                Welcome to our photography app where you can explore, share, and connect with talented photographers worldwide.
              </p>
              <button className="btn btn-primary">Get Started</button>
            </div>
          </div>
        </div>
        {/* Features Section */}
        <div className="bg-base-100 py-12">
          <div className="container mx-auto px-4">
            <h2 className="text-3xl font-bold mb-8 text-center">Features</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              <div className="card bg-base-100 shadow-xl glow-card">
                <figure>
                  <img src="../../src/assets/Images/create-album.jpg" alt="Album" />
                </figure>
                <div className="card-body">
                  <h2 className="card-title">Create Albums</h2>
                  <p>
                    Organize your photos into beautiful albums and share them with your friends and family.
                  </p>
                </div>
              </div>
              <div className="card bg-base-100 shadow-xl glow-card">
                <figure>
                  <img src="../../src/assets/Images/explore-discover.jpg" alt="Explore" />
                </figure>
                <div className="card-body">
                  <h2 className="card-title">Explore and Discover</h2>
                  <p>
                    Explore amazing photos from talented photographers around the world and get inspired.
                  </p>
                </div>
              </div>
              <div className="card bg-base-100 shadow-xl glow-card">
                <figure>
                  <img src="../../src/assets/Images/community.jpg" alt="Community" />
                </figure>
                <div className="card-body">
                  <h2 className="card-title">Join the Community</h2>
                  <p>
                    Connect with like-minded photographers, share your work, and get feedback from the community.
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