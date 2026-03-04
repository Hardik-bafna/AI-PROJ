"use client"

import { useEffect, useState } from "react"

export default function Home() {

  const [aqiData, setAqiData] = useState<any>(null)

  useEffect(() => {

    fetch("http://127.0.0.1:5000/aqi?city=${city}")
      .then(res => res.json())
      .then(data => setAqiData(data))

  }, [])


  function getColor(status:string){

    switch(status){
      case "Good": return "text-green-600"
      case "Satisfactory": return "text-yellow-500"
      case "Moderate": return "text-orange-500"
      case "Poor": return "text-red-500"
      case "Very Poor": return "text-purple-600"
      case "Severe": return "text-red-800"
      default: return "text-gray-500"
    }

  }


  if(!aqiData){
    return(
      <div className="flex items-center justify-center h-screen text-2xl">
        Loading AQI Data...
      </div>
    )
  }

  return(

    <div className="h-screen flex items-center justify-center bg-gradient-to-r from-blue-500 to-purple-700">

      <div className="bg-white shadow-2xl rounded-2xl p-10 w-[420px] text-center">

        <h1 className="text-3xl font-bold mb-6">
          🌍 Air Quality Monitor
        </h1>

        <div className="text-lg">
          PM2.5
        </div>

        <div className="text-4xl font-bold mb-5">
          {aqiData.PM25}
        </div>

        <div className="text-lg">
          AQI
        </div>

        <div className="text-5xl font-bold mb-5">
          {aqiData.AQI}
        </div>

        <div className={`text-2xl font-bold ${getColor(aqiData.Status)}`}>
          {aqiData.Status}
        </div>

      </div>

    </div>

  )
}