function load_data() {
    fetch("/data")
      .then((response) => response.json())
      .then((data) => {
  
        
        
      })
      .catch((error) => console.error("Error:", error));
  }