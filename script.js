async function getAQI() {

    const city = document.getElementById("cityInput").value;

    if (!city) {
        alert("Please enter a city");
        return;
    }

    document.getElementById("aqi").innerText = "...";
    document.getElementById("status").innerText = "Loading...";

    const response = await fetch(`http://127.0.0.1:5000/aqi?city=${city}`);
    const data = await response.json();

    if (data.error) {
        document.getElementById("aqi").innerText = "--";
        document.getElementById("status").innerText = data.error;
        return;
    }

    document.getElementById("aqi").innerText = data.AQI;
    document.getElementById("status").innerText = data.Status;
}