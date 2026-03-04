"use client"

import { useState } from "react"

export default function Home() {

  const [city, setCity] = useState("")
  const [data, setData] = useState<any>(null)

  const getAQI = async () => {

    const res = await fetch(`http://127.0.0.1:5000/aqi?city=${city}`)
    const result = await res.json()

    setData(result)
  }

  return (
    <main style={{padding:"40px", fontFamily:"sans-serif"}}>

      <h1>AQI Checker</h1>

      <input
        placeholder="Enter city"
        value={city}
        onChange={(e)=>setCity(e.target.value)}
      />

      <button onClick={getAQI}>
        Check AQI
      </button>

      {data && (
        <div style={{marginTop:"20px"}}>
          <h2>{data.city}</h2>
          <p>AQI: {data.aqi}</p>
          <p>Status: {data.status}</p>
        </div>
      )}

    </main>
  )
}
