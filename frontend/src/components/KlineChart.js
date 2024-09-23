import React, { useEffect, useState } from 'react';
import { init, dispose } from 'klinecharts'
import { Table } from 'react-bootstrap';
import "../App.css";
import axios from 'axios';

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

  useEffect(() => {
    const chart = init('chart')
          
    chart.applyNewData(datas)
    console.log(datas)     
    return () => {
      dispose('chart')
    }
  }, [])
 
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
      const now = new Date();
      console.log(datas);
      setDatas(prevPrices => [
        ...prevPrices, 
        {
          ...data.data,
          time: now.toUTCString(),
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
    <div id="chart" className="row side-row" style={{ width: 600, height: 600 }}/>
    <div className="row side-row" >
      <p id="before-table"></p>
      <Table striped bordered hover className="react-bootstrap-table" id="dataTable">
        <thead>
            <tr>
            <th>Name</th>
            <th>Open</th>
            <th>Close</th>
            <th>High</th>
            <th>Low</th>
            <th>Volume</th>
            <th>Timestamp</th>
            <th>Time</th>
            </tr>
        </thead>
        <tbody>
          {datas.map((data, key) =>
          <tr key={key}>
              <td>{data.crypto_name}</td>
              <td>{data.open}</td>
              <td>{data.close}</td>
              <td>{data.high}</td>
              <td>{data.low}</td>
              <td>{data.volume}</td>
              <td>{data.timestamp}</td>
              <td>{data.time}</td>
          </tr>)}
        </tbody>
      </Table>            
    </div>
  </div>
  );
};

export default KlineChart;