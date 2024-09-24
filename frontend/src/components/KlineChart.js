import React, { useEffect, useState } from 'react';
import "../App.css";
import axios from 'axios';
import { init, registerIndicator } from 'klinecharts'

async function getDatas() {
  return await axios.get('http://127.0.0.1:8000/cryptoprices/')
    .then(response => response.data)
}

const fruits = [
  '🍏', '🍎', '🍐', '🍊', '🍋', '🍌',
  '🍉', '🍇', '🍓', '🍈', '🍒', '🍑',
  '🍍', '🥥', '🥝', '🥭', '🥑', '🍏'
];

registerIndicator({
  name: 'Custom',
  figures: [{ key: 'emoji' }],
  calc: (kLineDataList) => {
    return kLineDataList.map(kLineData => ({
      emoji: kLineData.close,
      text: fruits[Math.floor(Math.random() * fruits.length)]
    }));
  },
  draw: ({ ctx, barSpace, visibleRange, indicator, xAxis, yAxis }) => {
    const { from, to } = visibleRange;

    ctx.font = `${barSpace.gapBar}px Helvetica Neue`;
    ctx.textAlign = 'center';
    const result = indicator.result;
    for (let i = from; i < to; i++) {
      const data = result[i];
      const x = xAxis.convertToPixel(i);
      const y = yAxis.convertToPixel(data.emoji);
      ctx.fillText(data.text, x, y);
    }
    return false;
  }
});


const KlineChart = () => {
  const [datas, setDatas] = useState([]);

  useEffect(() => {
    let mounted = true;
    let len;
    getDatas()
      .then(data => {
        if(mounted) {
          setDatas(data)
        }
      })
    return () => mounted = false;
  }, []);
 
  useEffect(() => {
    const chart = init('k-line-chart');
    chart.createIndicator('MACD');
    chart.createIndicator('RSI');
    chart.applyNewData(datas);

    return () => {
      chart.destroy();
    };
  }, [datas]);

  const setMainIndicator = (name) => {
    const chart = init('k-line-chart'); // Re-initialize to get the chart instance
    chart.createIndicator(name, true, { id: 'candle_pane' });
  };

  const setSubIndicator = (name) => {
    const chart = init('k-line-chart'); // Re-initialize to get the chart instance
    chart.createIndicator(name);
  };

  const socket = new WebSocket('ws://127.0.0.1:8000/crypto/');

  // Handle connection open
  socket.onopen = () => {
      socket.send(JSON.stringify({ 'message': 'Hello!' }));
      console.log('WebSocket connection established');
  };

  // Handle incoming messages
  socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      const period = new Date(data.data.timestamp/1000);
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
      <div id="container" className="row side-row">
        <div id="k-line-chart" style={{ height: '630px' }}></div>
      </div>
    </div>
  );
};

export default KlineChart;