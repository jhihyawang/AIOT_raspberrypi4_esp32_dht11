document.addEventListener('DOMContentLoaded', () => {
    // 设置日期时间输入框的最大值为当前时间
    const now = new Date();
    const currentDateTime = new Date(now.getTime() - now.getTimezoneOffset() * 60000).toISOString().slice(0, 16);
    document.getElementById('startDateTime').setAttribute('max', currentDateTime);
    document.getElementById('endDateTime').setAttribute('max', currentDateTime);    

    const chart = Highcharts.chart('dataChart', {
        chart: {
            type: 'line'
        },
        title: {
            text: 'Specified Time Sensor Data'
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

    document.getElementById('fetchDataBtn').addEventListener('click', () => {
        const startDateTime = document.getElementById('startDateTime').value;
        const endDateTime = document.getElementById('endDateTime').value;

        if (!startDateTime || !endDateTime) {
            alert('Please select both start and end date times.');
            return;
        }

        const selectedStartTime = new Date(startDateTime).getTime();
        const selectedEndTime = new Date(endDateTime).getTime();
        const currentTimestamp = new Date().getTime();

        if (selectedStartTime > currentTimestamp || selectedEndTime > currentTimestamp) {
            alert('Selected date time cannot be greater than current time.');
            return;
        }

        if (selectedEndTime < selectedStartTime) {
            alert('End time cannot be before start time.');
            return;
        }

        fetch(`/get_data?start_time=${startDateTime}:00&end_time=${endDateTime}:00`)
            .then(response => response.json())
            .then(data => {
                const categories = data.map(entry => entry.timestamp);

                const temperatureData = data.map(entry => entry.temperature);
                const humidityData = data.map(entry => entry.humidity);

                chart.xAxis[0].setCategories(categories);
                chart.series[0].setData(temperatureData);
                chart.series[1].setData(humidityData);
            })
            .catch(error => console.error('Error fetching data:', error));
    });
});
