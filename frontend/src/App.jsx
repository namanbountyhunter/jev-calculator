import { useState } from "react";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const calculate = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/calculate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: query,
        }),
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      setResult({
        success: false,
        error: "Could not connect to the backend.",
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="calculator-card">
        <h1>Jev Calculator</h1>

        <p className="subtitle">
          Calculate anything using natural language
        </p>

        <div className="input-container">
          <input
            type="text"
            placeholder="Try: What is 15% of 200?"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                calculate();
              }
            }}
          />

          <button onClick={calculate} disabled={loading}>
            {loading ? "Calculating..." : "Calculate"}
          </button>
        </div>

        {result && (
          <div className="result">
            {result.success ? (
              <>
                <div className="result-value">
                  {result.result}
                </div>

                <div className="details">
                  <p>
                    <strong>Query:</strong> {result.query}
                  </p>

                  <p>
                    <strong>Operation:</strong> {result.operation}
                  </p>

                  <p>
                    <strong>Decision source:</strong>{" "}
                    {result.decision_source}
                  </p>
                </div>
              </>
            ) : (
              <p className="error">{result.error}</p>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;