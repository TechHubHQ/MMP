module.exports = {
    // ... other webpack configuration ...
    resolve: {
      fallback: {
        "url": false,
        "assert": false
      }
    }
  }