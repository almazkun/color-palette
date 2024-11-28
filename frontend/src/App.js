import React, { useState, useEffect, useCallback } from "react";
import "./App.css";

const baseApiUrl = process.env.REACT_APP_API_URL || "http://localhost:8000";

const COLOR_SPACES = {
  RGB: "rgb",
  HSL: "hsl",
  HEX: "hex"
};

const formatColor = (color) => {
  switch(color.color_space) {
    case COLOR_SPACES.RGB:
      return `rgb(${color.r}, ${color.g}, ${color.b})`;
    case COLOR_SPACES.HSL:
      return `hsl(${color.h}, ${color.s}%, ${color.l}%)`;
    case COLOR_SPACES.HEX:
      return `${color.hex}`;
    default:
      return "";
  }
};

const ColorLines = ({ colors }) => (
  <div className="lines-container">
    {colors.map((color, index) => (
      <div
        key={index}
        className="line"
        style={{ backgroundColor: formatColor(color) }}
      />
    ))}
  </div>
);

const useColorFetcher = () => {
  const [colors, setColors] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchColors = useCallback(async () => {
    setIsLoading(true);
    setError(null);
    
    try {
      const apiUrl = baseApiUrl + `/api/v1/swatches/`;
      const response = await fetch(apiUrl);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();

      setColors(data.swatches);
    } catch (error) {
      console.error("Error fetching colors:", error);
      setError(error);
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchColors();
  }, [fetchColors]);

  return { 
    colors, 
    fetchColors, 
    isLoading, 
    error 
  };
};

const App = () => {
  const { 
    colors,
    fetchColors, 
    isLoading, 
    error 
  } = useColorFetcher();

  return (
    <div className="App">
      {error && (
        <div className="error-message">
          Failed to load colors: {error.message}
        </div>
      )}

      {isLoading ? (
        <div className="loading">
          <ColorLines colors={colors} />
          <div className="overlay-loading">Loading...</div>
        </div>
      ) : (
        <>
          <ColorLines colors={colors} />
          <button 
            onClick={fetchColors} 
            className="regenerate-button"
            disabled={isLoading}
          >
            {isLoading ? 'Regenerating...' : 'Regenerate'}
          </button>
        </>
      )}
    </div>
  );
};

export default App;