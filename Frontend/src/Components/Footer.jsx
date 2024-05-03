function Footer() {
    return (
      <footer className="footer p-10 bg-base-200 text-base-content">
        <nav>
          <h6 className="footer-title">Services</h6>
          <a className="link link-hover">Wedding Photography</a>
          <a className="link link-hover">Portrait Photography</a>
          <a className="link link-hover">Event Photography</a>
        </nav>
        <nav>
          <h6 className="footer-title">About</h6>
          <a className="link link-hover">Our Story</a>
          <a className="link link-hover">Meet the Team</a>
          <a className="link link-hover">Testimonials</a>
        </nav>
        <nav>
          <h6 className="footer-title">Resources</h6>
          <a className="link link-hover">Photography Tips</a>
          <a className="link link-hover">Pricing Guide</a>
          <a className="link link-hover">FAQs</a>
          <a className="link link-hover">Contact Us</a>
        </nav>
        <form>
          <h6 className="footer-title">Stay Updated</h6>
          <fieldset className="form-control w-80">
            <label className="label">
              <span className="label-text">Enter your email address</span>
            </label>
            <div className="join">
              <input
                type="text"
                placeholder="email@example.com"
                className="input input-bordered join-item"
              />
              <button className="btn btn-primary join-item">Subscribe</button>
            </div>
          </fieldset>
        </form>
      </footer>
    );
  }
  
  export default Footer;