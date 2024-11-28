import React, { useState, useEffect, useCallback } from "react";
import "./App.css";

const baseApiUrl = process.env.REACT_APP_API_URL || "http://localhost:8000";

const COLOR_SPACES = {
  RGB: "rgb",
  HSL: "hsl"
};

const formatColor = (color, colorSpace) => {
  switch(colorSpace) {
    case COLOR_SPACES.RGB:
      return `rgb(${color.r}, ${color.g}, ${color.b})`;
    case COLOR_SPACES.HSL:
      return `hsl(${color.h}, ${color.s}%, ${color.l}%)`;
    default:
      return "";
  }
};

const ColorSpaceSelector = ({ 
  colorSpace, 
  onColorSpaceChange 
}) => (
  <div className="color-space-selector">
    <label htmlFor="color-space">Select Color Space:</label>
    <select
      id="color-space"
      value={colorSpace}
      onChange={(e) => onColorSpaceChange(e.target.value)}
    >
      {Object.values(COLOR_SPACES).map(space => (
        <option key={space} value={space}>
          {space.toUpperCase()}
        </option>
      ))}
    </select>
  </div>
);

const ColorLines = ({ colors, colorSpace }) => (
  <div className="lines-container">
    {colors.map((color, index) => (
      <div
        key={index}
        className="line"
        style={{ backgroundColor: formatColor(color, colorSpace) }}
      />
    ))}
  </div>
);


const useColorFetcher = (colorSpace) => {
  const [colors, setColors] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchColors = useCallback(async () => {
    setIsLoading(true);
    setError(null);
    
    try {
      const apiUrl = baseApiUrl + `/api/v1/swatches/${colorSpace}/`;
      console.log(apiUrl);
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
  }, [colorSpace]);

  useEffect(() => {
    fetchColors();
  }, [fetchColors]);

  return { colors, fetchColors, isLoading, error };
};

const App = () => {
  const [colorSpace, setColorSpace] = useState(COLOR_SPACES.RGB);
  const { colors, fetchColors, isLoading, error } = useColorFetcher(colorSpace);

  return (
    <div className="App">
      <ColorSpaceSelector 
        colorSpace={colorSpace} 
        onColorSpaceChange={setColorSpace} 
      />

      {error && (
        <div className="error-message">
          Failed to load colors: {error.message}
        </div>
      )}

      {isLoading ? (
        <div className="loading">Loading colors...</div>
      ) : (
        <>
          <ColorLines colors={colors} colorSpace={colorSpace} />
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