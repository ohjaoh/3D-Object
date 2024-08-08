import { useLoader } from "@react-three/fiber";
import { useMemo } from "react";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";

const Weather = (props) => {
  const { position, weather } = props;
  const glb = useLoader(GLTFLoader, "/models/weather.glb");
  console.log(glb.nodes);

  // api에서 오는 데이터와 모델에 맞는 것이 없다면 기본으로 구름을 한다는 코드임
  // let weatherModel;
  // if(glb.nodes[weather]){
  //     weatherModel = glb.nodes[weather].clone();
  // }else{
  //     weatherModel = glb.nodes.cloud.clone();
  // }

  const weatherModel = useMemo(() => {
    const cloneModel =glb.nodes[weather] || glb.nodes.cloud
    return cloneModel.clone();
  }, [weather]);

  return (
    <mesh position={position}>
      <primitive object={weatherModel} />
    </mesh>
  );
};

export default Weather;
