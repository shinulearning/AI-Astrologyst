import React, { useEffect, useRef } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { jsPDF } from 'jspdf'
import html2canvas from 'html2canvas'

const WEBSITE_URL = 'https://shinuailabs.ai'

export default function Report() {
  const location = useLocation()
  const navigate = useNavigate()
  const report = location.state?.report
  const reportRef = useRef(null)

  async function downloadPdf() {
    if (!reportRef.current) {
      return
    }

    const canvas = await html2canvas(reportRef.current, {
      scale: 2,
      backgroundColor: '#0b1220'
    })
    const imageData = canvas.toDataURL('image/png')
    const pdf = new jsPDF('p', 'pt', 'a4')
    const pageWidth = pdf.internal.pageSize.getWidth()
    const margin = 24
    const pdfWidth = pageWidth - margin * 2
    const pdfHeight = (canvas.height * pdfWidth) / canvas.width

    pdf.addImage(imageData, 'PNG', margin, margin, pdfWidth, pdfHeight)
    pdf.save(`${report.name || 'astrology-report'}.pdf`)
  }

  useEffect(() => {
    if (!report) {
      navigate('/')
    }
  }, [report, navigate])

  if (!report) {
    return null
  }

  return (
    <div className="card form-card" ref={reportRef}>
      <div className="report-header">
        <img className="report-logo" src="/shinu-logo.svg" alt="ShinuAiLabs Logo" />
        <div>
          <span className="eyebrow">ShinuAiLabs Astrology</span>
          <h2>Your personalized astrology report</h2>
          <p className="website-label">https://shinuailabs.ai</p>
        </div>
      </div>

      <p className="report-summary">{report.summary}</p>
      <div className="actions report-actions">
        <button type="button" className="download-btn" onClick={downloadPdf}>Download as PDF</button>
        <button type="button" onClick={() => navigate('/')}>Back to Form</button>
      </div>
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

      </section>

      <section className="report-sections">
        {report.sections.map((section, index) => (
          <div key={index} className="section-card">
            <h3>{section.title}</h3>
            {section.content.split('\n').map((line, idx) => (
              <p key={idx}>{line}</p>
            ))}
          </div>
        ))}
      </section>

      <div className="report-card">
        <h3>Recommendations</h3>
        <ul className="report-list">
          {report.recommendations.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>

      <div className="actions">
        <button type="button" onClick={() => navigate('/')}>Back to Form</button>
      </div>
    </div>
  )
}