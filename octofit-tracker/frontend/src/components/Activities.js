import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActivities = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
      console.log('Activities API endpoint:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Activities fetched data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results || data;
        setActivities(Array.isArray(activitiesData) ? activitiesData : []);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching activities:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchActivities();
  }, []);

  if (loading) return (
    <div className="container mt-4">
      <div className="loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-4">
      <div className="alert alert-danger" role="alert">
        <h4 className="alert-heading">Error!</h4>
        <p>{error}</p>
      </div>
    </div>
  );

  return (
    <div className="container mt-4">
      <div className="page-header">
        <h2>🏃 Activities Log</h2>
        <p className="mb-0">Track all fitness activities and workouts</p>
      </div>
      <div className="table-container">
        <div className="d-flex justify-content-between align-items-center mb-3">
          <h5 className="mb-0">Recent Activities</h5>
          <span className="badge bg-primary">{activities.length} Total</span>
        </div>
        <div className="table-responsive">
          <table className="table table-hover">
          <thead>
            <tr>
              <th>ID</th>
              <th>User</th>
              <th>Activity Type</th>
              <th>Duration (min)</th>
              <th>Distance (km)</th>
              <th>Calories</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            {activities.length === 0 ? (
              <tr>
                <td colSpan="7" className="text-center">No activities found</td>
              </tr>
            ) : (
              activities.map((activity) => (
                <tr key={activity.id}>
                  <td><span className="badge bg-secondary">{activity.id}</span></td>
                  <td><strong>{activity.user}</strong></td>
                  <td><span className="badge bg-info">{activity.activity_type}</span></td>
                  <td>{activity.duration} min</td>
                  <td>{activity.distance} km</td>
                  <td><span className="badge bg-success">{activity.calories_burned} cal</span></td>
                  <td>{new Date(activity.date).toLocaleDateString()}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
        </div>
      </div>
    </div>
  );
}

export default Activities;
