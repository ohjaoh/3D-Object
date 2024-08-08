import { Canvas } from "@react-three/fiber";
// import Scene from "../components/Scene";
import Lights from "../components/Lights";
import { lazy, Suspense } from "react";
import CustomLoader from "./CustomLoader"; // CustomLoader 컴포넌트 임포트

// Saspense React 18에서 나온 기술
// API나 GrapQL 등에서 사용 비동기에 자주하는 듯
// R3F에서 3D작업을 할 때 Saspense가 굉장히 자주 사용됨
// useLoader를 이용해서 모델을 불러오기 때문에 Saspense를 사용함

function Sphere() {
  return (
    <mesh>
      <sphereGeometry args={[1]} />
      <meshBasicMaterial color="white" />
    </mesh>
  );
}
const Scene = lazy(() => {
  return new Promise((resolve) => {
    setTimeout(() => resolve(import('../components/Scene')), 2000);
  });
});

function Home() {
  return (
    <>
      <Canvas camera={{ position: [0, 0, 5], fov: 45 }}>
        <color attach="background" args={["rgb(67, 127, 240)"]} />
        <Suspense fallback={<CustomLoader />}>
          <Lights />
          <Scene />
        </Suspense>
      </Canvas>
    </>
  );
}

export default Home;