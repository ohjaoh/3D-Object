import { Html, useProgress } from "@react-three/drei";
import './CustomLoader.css';

function CustomLoader() {
  const { progress } = useProgress();
  return (
    <Html center>
      <div className="loader-container">
        <div className="spinner" />
        <p className="loading-text">Loading {progress.toFixed(2)}%</p>
      </div>
    </Html>
  );
}

export default CustomLoader;
