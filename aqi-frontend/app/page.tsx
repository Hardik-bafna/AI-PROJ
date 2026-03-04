"use client"

import { useState } from "react"

export default function Home() {

  const [city, setCity] = useState("")
  const [data, setData] = useState<any>(null)

  const getAQI = async () => {

    if (!city) return

    const res = await fetch(`http://127.0.0.1:5000/aqi?city=${city}`)
    const result = await res.json()

    setData(result)
  }

  return (
    <main className="flex items-center justify-center min-h-screen">

      <div className="bg-zinc-900 p-10 rounded-2xl shadow-2xl w-[380px] text-center">

        <h1 className="text-3xl font-bold mb-6">
          AQI Checker
        </h1>

        <input
          className="w-full p-3 rounded-lg bg-black border border-zinc-700 focus:outline-none focus:border-white"
          placeholder="Enter city"
          value={city}
          onChange={(e)=>setCity(e.target.value)}
        />

        <button
          onClick={getAQI}
          className="mt-4 w-full bg-white text-black py-2 rounded-lg font-semibold hover:bg-zinc-200 transition"
        >
          Check AQI
        </button>

        {data && (
          <div className="mt-6 bg-black rounded-lg p-4 border border-zinc-700">

            <h2 className="text-xl font-semibold">{data.city}</h2>

            <p className="mt-2 text-lg">
              AQI: <span className="font-bold">{data.AQI}</span>
            </p>

            <p className="text-zinc-400">
              {data.Status}
            </p>

          </div>
        )}

      </div>

    </main>
  )
}
