import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              <img src="/octofitapp-small.png" alt="OctoFit Logo" className="navbar-logo" />
              OctoFit Tracker
            </Link>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/users">
                    Users
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">
                    Activities
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">
                    Teams
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">
                    Leaderboard
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">
                    Workouts
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route
            path="/"
            element={
              <div className="container mt-4">
                <div className="hero-section text-center">
                  <h1 className="hero-title">🏋️ Welcome to OctoFit Tracker!</h1>
                  <p className="hero-subtitle">
                    Track your fitness activities, compete with your team, and achieve your goals.
                  </p>
                  <hr className="my-4" style={{ borderColor: 'rgba(255,255,255,0.3)' }} />
                  <p className="lead">Select a section from the navigation menu to get started.</p>
                </div>
                
                <div className="row mt-4">
                  <div className="col-md-4 mb-3">
                    <div className="card text-center">
                      <div className="card-body">
                        <h3>👤</h3>
                        <h5 className="card-title">Users</h5>
                        <p className="card-text">Manage user profiles and track member information.</p>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-4 mb-3">
                    <div className="card text-center">
                      <div className="card-body">
                        <h3>🏃</h3>
                        <h5 className="card-title">Activities</h5>
                        <p className="card-text">Log and view all fitness activities and workouts.</p>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-4 mb-3">
                    <div className="card text-center">
                      <div className="card-body">
                        <h3>👥</h3>
                        <h5 className="card-title">Teams</h5>
                        <p className="card-text">Create and manage fitness teams for competition.</p>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-6 mb-3">
                    <div className="card text-center">
                      <div className="card-body">
                        <h3>🏆</h3>
                        <h5 className="card-title">Leaderboard</h5>
                        <p className="card-text">View rankings and compete with other users.</p>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-6 mb-3">
                    <div className="card text-center">
                      <div className="card-body">
                        <h3>💪</h3>
                        <h5 className="card-title">Workouts</h5>
                        <p className="card-text">Get personalized workout suggestions and plans.</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            }
          />
          <Route path="/users" element={<Users />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
