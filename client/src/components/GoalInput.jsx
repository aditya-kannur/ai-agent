import React, { useState } from "react";
import axios from "axios";

const GoalInput = () => {
  const [goals, setGoals] = useState("");
  const [plans, setPlans] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleInputChange = (e) => {
    setGoals(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    try {
      const response = await axios.post("http://127.0.0.1:8000/generate-plan", {
        goals: goals.split(",").map((goal) => goal.trim()),
      });
      setPlans(response.data.plans);
    } catch (err) {
      setError("Error fetching data");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>AI Goal Planner</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={goals}
          onChange={handleInputChange}
          placeholder="Enter your goals (comma-separated)"
          rows="4"
          style={{ width: "100%" }}
        />
        <br />
        <button type="submit" disabled={loading}>
          {loading ? "Loading..." : "Generate Plan"}
        </button>
      </form>

      {error && <div style={{ color: "red" }}>{error}</div>}

      {plans.length > 0 && (
        <div>
          <h2>Generated Plans:</h2>
          <ul>
            {plans.map((plan, index) => (
              <li key={index}>
                <strong>Goal {index + 1}:</strong>
                <pre>{plan}</pre>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default GoalInput;
