import React from 'react'
import { Routes, Route, Link } from 'react-router-dom'
import KundaliForm from './pages/KundaliForm'
import Report from './pages/Report'

export default function App() {
  return (
    <div className="app">
      <header className="topbar">
        <div className="brand">
          <img className="brand-logo" src="/shinu-logo.svg" alt="ShinuAiLabs Logo" />
          <div>
            <h1>ShinuAiLabs AI Astrologyst</h1>
            <p className="tagline">Your personalized celestial insights and karmic guidance.</p>
          </div>
        </div>
        <nav>
          <Link to="/">Home</Link>
        </nav>
      </header>

      <main className="main-content">
        <Routes>
          <Route path="/" element={<KundaliForm />} />
          <Route path="/report" element={<Report />} />
        </Routes>
      </main>
    </div>
  )
}