// Run only after the page content is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("phishForm");
  
    if (form) {
      form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent real form submission
  
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
  
        alert("🚨 This is a phishing simulation. Never enter real credentials!");
  
        console.log("[SIMULATION] Entered username:", username);
        console.log("[SIMULATION] Entered password:", password);
      });
    } else {
      console.error("Form with id='phishForm' not found.");
    }
  });
  