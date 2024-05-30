document.addEventListener('DOMContentLoaded', () => {
    const MAX_ENTRIES = 8;
    const UPDATE_INTERVAL_MS = 5000;
    
    // 設置起始時間
    const startDate = new Date(new Date().toLocaleString("en-US", {timeZone: "Asia/Taipei"}));
    startDate.setHours(startDate.getHours() + 8);
    const formattedStartDate = startDate.toISOString().slice(0, 19).replace('T', ' ');

    // 初始化 Highcharts
    const chart = Highcharts.chart('dataChart', {
        chart: {
            type: 'line'
        },
        title: {
            text: 'Real Time Sensor Data'
        },
        xAxis: {
            categories: []
        },
        yAxis: {
            title: {
                text: 'Values'
            }
        },
        series: [{
            name: 'Temperature',
            data: []
        }, {
            name: 'Humidity',
            data: []
        }]
    });

    // 獲取資料並更新圖表
    const fetchDataAndUpdateChart = () => {
        const currentDate = new Date(new Date().toLocaleString("en-US", {timeZone: "Asia/Taipei"}));
        const endDate = new Date(currentDate.getTime() + (UPDATE_INTERVAL_MS * 2));
        endDate.setHours(endDate.getHours() + 8);
        const formattedEndDate = endDate.toISOString().slice(0, 19).replace('T', ' ');

        console.log(`/get_data?start_time=${formattedStartDate}&end_time=${formattedEndDate}`);

        fetch(`/get_data?start_time=${formattedStartDate}&end_time=${formattedEndDate}`)
            .then(response => response.json())
            .then(data => {
                const latestEntries = data.slice(-MAX_ENTRIES);

                console.log("Latest Entries: ", latestEntries);
                // 更新圖表資料
                const categories = latestEntries.map(entry => entry.timestamp);
                const temperatureData = latestEntries.map(entry => entry.temperature);
                const humidityData = latestEntries.map(entry => entry.humidity);

                chart.xAxis[0].setCategories(categories);
                chart.series[0].setData(temperatureData);
                chart.series[1].setData(humidityData);
            })
            .catch(error => console.error('Error fetching data:', error));
    };

    fetchDataAndUpdateChart();
    setInterval(fetchDataAndUpdateChart, UPDATE_INTERVAL_MS + 10);

    document.getElementById('fetchAutoDataBtn').addEventListener('click', fetchDataAndUpdateChart);
});
