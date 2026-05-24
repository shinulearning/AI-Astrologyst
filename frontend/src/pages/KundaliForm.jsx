import React, { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

export default function KundaliForm() {
  const [form, setForm] = useState({
    name: '',
    gender: 'Male',
    dob: '',
    tob: '',
    pob: '',
    country: '',
    marital_status: '',
    profession: '',
    education: ''
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  function update(e) {
    const { name, value } = e.target
    setForm(f => ({ ...f, [name]: value }))
  }

  async function handleSubmit(e) {
    e.preventDefault()
    setLoading(true)
    setError('')
    try {
      const resp = await axios.post('/api/report', form)
      navigate('/report', { state: { report: resp.data } })
    } catch (err) {
      console.error('API error', err)
      if (err.response) {
        // Server responded with a status code outside 2xx
        setError(`Request failed with status ${err.response.status}: ${JSON.stringify(err.response.data)}`)
      } else {
        // Network or other error
        setError(err.message || 'Unable to generate the report. Please make sure the backend is running.')
      }
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="card form-card">
      <div className="form-header">
        <span className="eyebrow">Celestial Insights</span>
        <h2>Generate your personalized kundali report</h2>
        <p className="form-note">Enter your birth details and receive a beautiful, intuitive astrology summary.</p>
      </div>

      {error && <div className="alert">{error}</div>}

      <form onSubmit={handleSubmit} className="form">
        <div className="form-grid">
          <label>
            Name
            <input name="name" value={form.name} onChange={update} required placeholder="Your full name" />
          </label>
          <label>
            Gender
            <select name="gender" value={form.gender} onChange={update}>
              <option>Male</option>
              <option>Female</option>
              <option>Other</option>
            </select>
          </label>
          <label>
            Date of Birth
            <input name="dob" type="date" value={form.dob} onChange={update} required />
          </label>
          <label>
            Time of Birth
            <input name="tob" type="time" value={form.tob} onChange={update} required />
          </label>
          <label>
            Place of Birth
            <input name="pob" value={form.pob} onChange={update} required placeholder="City or town" />
          </label>
          <label>
            Country
            <input name="country" value={form.country} onChange={update} placeholder="Country" />
          </label>
          <label>
            Marital Status
            <input name="marital_status" value={form.marital_status} onChange={update} placeholder="Single, married, etc." />
          </label>
          <label>
            Profession
            <input name="profession" value={form.profession} onChange={update} placeholder="Your profession" />
          </label>
          <label>
            Education
            <input name="education" value={form.education} onChange={update} placeholder="Highest qualification" />
          </label>
        </div>

        <div className="actions">
          <button type="submit" disabled={loading}>{loading ? 'Generating...' : 'Generate Report'}</button>
        </div>
      </form>
    </div>
  )
}