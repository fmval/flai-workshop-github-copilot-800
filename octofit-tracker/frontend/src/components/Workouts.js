import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
      console.log('Workouts API endpoint:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Workouts fetched data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
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
        <h2>💪 Workout Suggestions</h2>
        <p className="mb-0">Personalized workout plans and routines</p>
      </div>
      <div className="mb-3">
        <span className="badge bg-primary fs-6">{workouts.length} Workouts</span>
      </div>
      <div className="row">
        {workouts.length === 0 ? (
          <div className="col-12">
            <div className="alert alert-info">No workouts found</div>
          </div>
        ) : (
          workouts.map((workout) => {
            const difficultyColor = 
              workout.difficulty_level === 'Beginner' ? 'success' :
              workout.difficulty_level === 'Intermediate' ? 'warning' : 'danger';
            return (
              <div key={workout.id} className="col-md-6 col-lg-4 mb-4">
                <div className="card h-100">
                  <div className="card-header">
                    <h5 className="mb-0">{workout.name}</h5>
                  </div>
                  <div className="card-body d-flex flex-column">
                    <div className="mb-2">
                      <span className="badge bg-info">{workout.activity_type}</span>
                    </div>
                    <p className="card-text flex-grow-1">{workout.description}</p>
                    <div className="mt-auto">
                      <hr />
                      <div className="d-flex justify-content-between mb-2">
                        <span><strong>⏱️ Duration:</strong></span>
                        <span className="badge bg-primary">{workout.duration} min</span>
                      </div>
                      <div className="d-flex justify-content-between mb-2">
                        <span><strong>📊 Difficulty:</strong></span>
                        <span className={`badge bg-${difficultyColor}`}>{workout.difficulty_level}</span>
                      </div>
                      <div className="d-flex justify-content-between">
                        <span><strong>🔥 Calories:</strong></span>
                        <span className="badge bg-success">{workout.calories_estimate} cal</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            );
          })
        )}
      </div>
    </div>
  );
}

export default Workouts;
