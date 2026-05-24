import React, { useEffect } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'

export default function Report() {
  const location = useLocation()
  const navigate = useNavigate()
  const report = location.state?.report

  useEffect(() => {
    if (!report) {
      navigate('/')
    }
  }, [report, navigate])

  if (!report) {
    return null
  }

  return (
    <div className="card form-card">
      <div className="form-header">
        <span className="eyebrow">Your Cosmic Summary</span>
        <h2>Your personalized astrology report</h2>
        <p className="form-note">This report is generated from your birth information and designed to help you understand your present energy.</p>
      </div>

      <p>{report.summary}</p>
      <section className="report-grid">
        <div className="report-card">
          <h3>Birth Details</h3>
          <p>Name: {report.name}</p>
          <p>Gender: {report.gender}</p>
          <p>Date of Birth: {report.dob}</p>
          <p>Time of Birth: {report.tob}</p>
          <p>Place of Birth: {report.pob}</p>
          <p>Country: {report.country}</p>
        </div>

        <div className="report-card">
          <h3>Personal Profile</h3>
          <p>Age: {report.age}</p>
          <p>Profession: {report.profession}</p>
          <p>Education: {report.education}</p>
          <p>Marital Status: {report.marital_status}</p>
        </div>

        <div className="report-card">
          <h3>Analysis</h3>
          <ul className="report-list">
            {report.analysis.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>

        <div className="report-card">
          <h3>Recommendations</h3>
          <ul className="report-list">
            {report.recommendations.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>
      </section>

      <div className="actions">
        <button type="button" onClick={() => navigate('/')}>Back to Form</button>
      </div>
    </div>
  )
}