import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../api'

export default function Users() {
  const [users, setUsers] = useState([])
  const [error, setError] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    api.get('/users')
      .then((res) => setUsers(res.data))
      .catch((err) => {
        if (err.response?.status === 401) {
          localStorage.removeItem('token')
          navigate('/login')
        } else {
          setError('Failed to fetch users')
        }
      })
  }, [])

  const handleLogout = () => {
    localStorage.removeItem('token')
    navigate('/login')
  }

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <h2>Users</h2>
        <button onClick={handleLogout} style={styles.logout}>Logout</button>
      </div>
      {error && <p style={styles.error}>{error}</p>}
      <table style={styles.table}>
        <thead>
          <tr>
            <th>User ID</th>
            <th>Email</th>
            <th>Status</th>
            <th>Created At</th>
          </tr>
        </thead>
        <tbody>
          {users.map((u) => (
            <tr key={u.user_id}>
              <td>{u.user_id}</td>
              <td>{u.email}</td>
              <td>{u.status}</td>
              <td>{u.created_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

const styles = {
  container: { padding: '24px' },
  header: { display: 'flex', justifyContent: 'space-between', alignItems: 'center' },
  logout: { padding: '8px 16px', cursor: 'pointer' },
  error: { color: 'red' },
  table: { width: '100%', borderCollapse: 'collapse', marginTop: '16px' },
}
