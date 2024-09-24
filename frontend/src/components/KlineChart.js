import React, { useEffect, useState } from 'react';
import "../App.css";
import axios from 'axios';
import Chart from './Chart';

async function getStudents() {
  return await axios.get('http://127.0.0.1:8000/cryptoprices/')
    .then(response => response.data)
}

const KlineChart = () => {
  const [datas, setDatas] = useState([]);

  useEffect(() => {
    let mounted = true;
    let len;
    getStudents()
      .then(data => {
        if(mounted) {
          setDatas(data)
        }
      })
    return () => mounted = false;
  }, []);
 
  const socket = new WebSocket('ws://127.0.0.1:8000/crypto/');

  // Handle connection open
  socket.onopen = () => {
      socket.send(JSON.stringify({ 'message': 'Hello!' }));
      console.log('WebSocket connection established');
  };

  // Handle incoming messages
  socket.onmessage = (event) => {
      let latestId = 0;
      const data = JSON.parse(event.data);
      const period = new Date(data.data.timestamp);
      setDatas(prevPrices => [
        ...prevPrices, 
        {
          ...data.data,
          period,
        }
      ]); // Update the state with new data
  };

  // Handle errors
  socket.onerror = (event) => {
      console.error('WebSocket error observed:', event);
  };

  // Handle connection close
  socket.onclose = (event) => {
      console.log('WebSocket connection closed:', event);
  };

  return(
   <div className="container-fluid side-container">
    <Chart
      chartValues = {datas}
    />
  </div>
  );
};

export default KlineChart;