import React, { useEffect, useState } from "react";
import { backendURL } from "./utils/urls";

const App = () => {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch(backendURL + "/members")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);

  return <div>App</div>;
};

export default App;
