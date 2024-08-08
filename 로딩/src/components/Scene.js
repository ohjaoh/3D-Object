import { useEffect, useState } from "react";
import Earth from "./Earth";
import Weather from "./Weather";
import { getCityWeather, getCurrentWeather } from "../utils/weatherApi";
import { cities } from "../utils/cities";
const api = process.env.REACT_APP_API_KEY;
const Scene = () => {
  const [content, setContent] = useState();
  // useEffect(() => {
  //   // getCurrentWeather(44.34, 10.99, process.env.REACT_APP_API_KEY);
  //   console.log(getCityWeather('Seoul', api));
  // },[]);

  const getCitiesWeather = () => {
    const promies = cities.map((city) => {
      return getCityWeather(city, api);
    });

    Promise.all(promies)
      .then((weatherDataArray) => {
        setContent(weatherDataArray);
      })
      .catch((error) => {
        console.error("error", error);
      });
  };

  useEffect(() => {
    // getCurrentWeather(44.34, 10.99, process.env.REACT_APP_API_KEY);
    getCitiesWeather();
  }, []);

  useEffect(() => {
    console.log("도시들 데이터", content);
  }, [content]);

  return (
    <>
      <Earth position={[0, -2, 0]} />
      {/* content가 존재하면, content 배열을 순회하며 Weather 컴포넌트를 렌더링 */}
      {content?.map((el, i) => {
        return (
          <Weather
            key={i + "Model Key"}
            position={[-1 + i * 0.5, 0, 0]}
            weather={el.weatherData.weather[0].main.toLowerCase()}
          />
        );
      })}
    </>
  );
};

export default Scene;
