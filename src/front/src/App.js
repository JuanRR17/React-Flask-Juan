import React, { useEffect, useState } from "react";
import { backendURL } from "./utils/urls";

const App = () => {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch(backendURL + "/members")
      // fetch("/members")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);

  return (
    <div>
      {typeof data.members === "undefined" ? (
        <p>Loading...</p>
      ) : (
        data.members.map((member, i) => <p key={i}>{member}</p>)
      )}
    </div>
  );
};

export default App;
