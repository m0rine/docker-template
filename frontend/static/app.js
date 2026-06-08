const API_URL = "/api";

const btn = document.getElementById("ipBtn");

btn.addEventListener("click", getIP);

async function getIP() {
  const box = document.getElementById("ipBox");
  const value = document.getElementById("ipValue");

  box.style.display = "block";
  value.textContent = "Loading...";

  try {
    const res = await fetch(`${API_URL}/ip`);
    const data = await res.json();

    value.textContent = data.ip;
  } catch (err) {
    console.error(err);
    value.textContent = "Error fetching IP";
  }
}
