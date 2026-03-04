fetch("http://127.0.0.1:5000/aqi")
.then(response => response.json())
.then(data => {

document.getElementById("aqi").innerText = data.AQI
document.getElementById("status").innerText = data.Status

})