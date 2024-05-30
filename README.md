# HW6 rasberry pi & 溫濕度感測器

**資管三 4110029009 王致雅**

以下以序列圖說明本實驗之溫濕度數據的收集、存儲和呈現過程

![截圖 2024-05-31 凌晨2.00.53.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-05-31_%25E5%2587%258C%25E6%2599%25A82.00.53.png)

以下是各個參與者的角色：

- **ESP32:** ESP32，負責收集溫濕度數據並通過 HTTP POST 請求將其發送到 app.py 伺服器。
- **app.py 伺服器**: 應用程序伺服器，接收來自 ESP32 的數據並將其存儲在資料庫 sensor_data.db 中。同時，它還提供了兩個網頁界面，即時數據頁面（realtime.html）和選擇時間範圍的數據頁面（specifictime.html）。
- **sensor_data.db**: 資料庫，用於存儲溫濕度數據。
- **realtime.html 和 specifictime.html**: 兩個前端頁面，用於呈現即時數據和特定時間範圍的數據。它們分別向 app.py 伺服器發送 HTTP GET 請求以獲取數據。
- **realtime.js 和 specifictime.js**: 兩個前端 JavaScript 腳本，用於處理從 app.py 伺服器獲取的數據並在網頁界面上呈現。

# 以下為本實驗之步驟

## **step1 樹莓派刷機**

### 下載PI的開機映像檔案

選擇macOS版本 [https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/)   

![Untitled](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/Untitled.png)

### 開啟執行檔

![截圖 2024-05-07 凌晨1.45.12.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-05-07_%25E5%2587%258C%25E6%2599%25A81.45.12.png)

![截圖 2024-05-07 凌晨1.44.59.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-05-07_%25E5%2587%258C%25E6%2599%25A81.44.59.png)

1.選擇rasberry Pi 機型                        

![截圖 2024-04-30 上午10.48.57.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-04-30_%25E4%25B8%258A%25E5%258D%258810.48.57.png)

2.選擇操作系統

![截圖 2024-04-30 上午10.49.19.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-04-30_%25E4%25B8%258A%25E5%258D%258810.49.19.png)

3.選擇儲存卡

![截圖 2024-05-07 凌晨1.47.21.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-05-07_%25E5%2587%258C%25E6%2599%25A81.47.21.png)

### 開始寫入開機映像檔案 至 SD卡

![截圖 2024-05-07 凌晨1.48.35.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-05-07_%25E5%2587%258C%25E6%2599%25A81.48.35.png)

![截圖 2024-05-07 凌晨1.50.06.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-05-07_%25E5%2587%258C%25E6%2599%25A81.50.06.png)

![截圖 2024-05-07 凌晨1.50.19.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-05-07_%25E5%2587%258C%25E6%2599%25A81.50.19.png)

燒錄中

![截圖 2024-05-07 凌晨1.49.40.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-05-07_%25E5%2587%258C%25E6%2599%25A81.49.40.png)

燒錄完成

![截圖 2024-05-07 凌晨2.31.17.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-05-07_%25E5%2587%258C%25E6%2599%25A82.31.17.png)

## **step2 樹莓派安裝 arduino ide**

將sd卡插入樹莓派並接上電源、螢幕、滑鼠以及設定網路連線

![Untitled](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/12f3e259-e537-4542-9620-c94f8ea16b41.png)

![Untitled](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/Untitled.jpeg)

下載所需之環境

**安裝Arduino IDE**

**Board manger：**ESP32manger

[https://dl.espressif.com/dl/package_esp32_index.json](https://dl.espressif.com/dl/package_esp32_index.json)

**Library:** 

Adafruit_Unified_Sensor

ArduinoJson

DHT_sensor_library

HttpClient

![20240507_03h42m58s_grim.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/3d99ad5a-e5c6-4b7c-90ad-c4a35db9d182.png)

## **step3 ESP32傳輸溫濕度** 評分項（一）

接線 || S —— D2 || VCC —— 3V3 || GND —— GND ||

board選擇：ESP32 Dev Module

![Untitled](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/Untitled%201.jpeg)

(1) 連接wifi

![20240530_16h26m56s_grim.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/20240530_16h26m56s_grim.png)

(2) 連接dht11 接收溫濕度

![20240530_16h32m49s_grim.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/20240530_16h32m49s_grim.png)

(3) 包裝成json，並以http送出，將透過url：”http://192.168.50.36:5000/post_data”傳送資料

![20240530_16h43m07s_grim.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/20240530_16h43m07s_grim.png)

- **樹莓派、ESP32端（Arduino）**
    
    ```cpp
    #include <WiFi.h>
    #include <DHT.h>   //引用DHT.h程式庫
    #include <ArduinoJson.h>
    #include <HTTPClient.h>
    
    const char* ssid = "Y615";
    const char* password = "nchumis123";
    
    #define DHTPIN 2    // Digital pin connected to the DHT sensor
    #define DHTTYPE DHT11   // Type of the DHT sensor
    
    DHT dht(DHTPIN, DHTTYPE);//dht(接腳,感測元件類型DHT11)
    #define SERVER_URL "http://192.168.50.36:5000/post_data"
    
    void setup() {
        Serial.begin(9600);
    
        Serial.println("Connecting to WiFi...");
        WiFi.begin(ssid, password);
    
        while (WiFi.status() != WL_CONNECTED) {
            delay(500);
            Serial.print(".");
        }
    
        Serial.println("");
        Serial.println("WiFi connected");
        Serial.print("IP address: ");
        Serial.println(WiFi.localIP());
    }
    
    void loop() {
      // Read temperature and humidity from DHT11 sensor
      float humidity = dht.readHumidity();
      float temperature = dht.readTemperature();
      
      // Check if any reads failed and exit early (to try again).
      if (isnan(humidity) || isnan(temperature)) {
        Serial.println("Failed to read from DHT sensor!");
        return;
      }
      
      // Print values to Serial Monitor
      Serial.print("Humidity: ");
      Serial.print(humidity);
      Serial.println("%");
      Serial.print("Temperature: ");
      Serial.print(temperature);
      Serial.println("°C");
      Serial.println("=======================================");
      
      // Create JSON object
      DynamicJsonDocument jsonDoc(200);
      jsonDoc["temperature"] = temperature;
      jsonDoc["humidity"] = humidity;
    
      // Serialize JSON object to string
      String jsonString;
      serializeJson(jsonDoc, jsonString);
    
      // Send data to the server via HTTP POST
      if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
    
        http.begin(SERVER_URL);
        http.addHeader("Content-Type", "application/json");
    
        int httpResponseCode = http.POST(jsonString);
    
        if (httpResponseCode > 0) {
          String response = http.getString();
          Serial.println("HTTP Response code: " + String(httpResponseCode));
          Serial.println("Response from server: " + response);
        } else {
          Serial.println("Error on sending POST: " + String(httpResponseCode));
          Serial.println(http.errorToString(httpResponseCode));
        }
    
        http.end();  // Free resources
      } else {
        Serial.println("Error in WiFi connection");
      }
    
      delay(2000); // Delay before next reading
    }
    ```
    
- **資料庫建立**
    
    ```python
    
    import sqlite3
    
    DB_NAME = "sensor_data.db"
    
    def init_database(db_name):
        """
        初始化資料庫，如果資料表不存在則創建它。
        
        Args:
            db_name (str): 資料庫檔案名稱。
        """
        try:
            with sqlite3.connect(db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_data
                                  (temperature REAL, humidity REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
                conn.commit()
            print("Database initialized successfully.")
        except Exception as e:
            print(f"Error initializing database: {str(e)}")
    ```
    
- **服務器端（Python Flask）**
    
    ```python
    from flask import Flask, request, jsonify
    from datetime import datetime
    
    app = Flask(__name__)
    
    DB_NAME = "sensor_data.db"
    
    @app.route('/post_data', methods=['POST'])
    def receive_data():
        try:
            content = request.json
    
            temperature = content["temperature"]
            humidity = content["humidity"]
    
            # Call function to insert sensor data into the database
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            timestamp = datetime.now().replace(microsecond=0)
    
            cursor.execute(
                """INSERT INTO sensor_data (temperature, humidity, timestamp) VALUES (?, ?, ?)""",
                (temperature, humidity, timestamp),
            )
    
            conn.commit()
            conn.close()
            print("(insert_sensor_data) Sensor data inserted successfully.")
    
            print(f"Received data: temperature={temperature}, humidity={humidity}")
            return jsonify({"success": True})
    
        except Exception as e:
            print(f"Error receiving data: {str(e)}")
            return jsonify({"success": False, "error": str(e)})
    
    if __name__ == "__main__":
    		init_database(DB_NAME)
        app.run(host="0.0.0.0", port=5000, debug=True)
    ```
    

![截圖 2024-05-29 晚上11.45.58.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-05-29_%25E6%2599%259A%25E4%25B8%258A11.45.58.png)

![Untitled](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/aafbd807-1d3a-44ae-b1c0-cc05373b92a3.png)

## **step4 FLASK網頁設計**

### 評分項（二）使用Flask製作前端頁面（Frontend&UI）

- 即時資料
    
    **我**：建立一個 JavaScript 腳本和一個 HTML 模板，用於使用 Highcharts 庫可視化即時感測器資料，並每五秒更新一次數據
    
    **chatgpt**：
    
    以下是用於使用 Highcharts 库可视化实时传感器数据的 JavaScript 脚本和 HTML 模板：
    
    ```jsx
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
    ```
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Data Visualization</title>
        <!-- Add Highcharts library -->
        <script src="https://code.highcharts.com/highcharts.js"></script>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <!-- header.html -->
        {% include 'header.html' %}
    
        <div class="container">
            <h1>it will update every 2 sec</h1>
            <button id="fetchAutoDataBtn" style="background-color: #484891; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; margin-top: 20px;">If it does not update automatically, Click Me</button>
            </div>           
            <div class="chart-container">
                <div id="dataChart"></div>
            </div>
        </div>
    
        <!-- footer.html -->
        {% include 'footer.html' %}
    
        <script src="/static/realtime.js"></script>
    </body>
    </html>
    ```
    
- 指定區間資料
    
    **我**：建立一個 JavaScript 腳本和一個 HTML 模板，用於使用 Highcharts 庫可視化指定時間範圍內的感測器資料、end time也不能在start time之前、時間也不能超過當前時間
    
    **chatgpt**：以下是用於可视化指定时间范围内传感器数据的 JavaScript 脚本和 HTML 模板：
    
    ```jsx
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
    ```
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Data Visualization</title>
        <!-- Add Highcharts library -->
        <script src="https://code.highcharts.com/highcharts.js"></script>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <!-- header.html -->
        {% include 'header.html' %}
    
        <div class="container">
            <div class="datetime-inputs" style="font-family: Arial, sans-serif; display: flex; align-items: center;">
                <div class="input-container">
                    <label for="startDateTime">Start Date And Time:</label>
                    <input type="datetime-local" id="startDateTime" name="startDateTime">
                </div>
                <div class="input-container">
                    <label for="endDateTime" style="display: block; margin-bottom: 5px;">End Date And Time:</label>
                    <input type="datetime-local" id="endDateTime" name="endDateTime">
                </div>
            </div>        
            <button id="fetchDataBtn" style="background-color: #484891; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; margin-top: 20px;">Fetch Data</button>
            </div>           
            <div class="chart-container">
                <div id="dataChart"></div>
            </div>
        </div>
    
        <!-- footer.html -->
        {% include 'footer.html' %}
    
        <script src="/static/specifiedtime.js"></script>
    </body>
    </html>
    
    ```
    
- 主頁面
    
    **我**：index.html該如何設計
    
    **chatgpt**：
    
    對於 **`index.html`**，你可以設計一個簡單的介面，用於顯示應用程序的概要信息、連結到其他部分，以及可能的話提供一些操作。以下是一個基本的範例：
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <!-- header.html -->
        {% include 'header.html' %}
    
        <div class="container">
            <h1>Welcome to Sensor Data Visualization</h1>
            <p>This application visualizes real-time sensor data and data within a specified time range.</p>
            <div class="links">
                <a class="button" href="/visualize-realtime">Visualize Real-time Data</a>
                <a class="button" href="/visualize-specifiedtime">Visualize Specified Time Data</a>
            </div>
        </div>
    
        <!-- footer.html -->
        {% include 'footer.html' %}
    </body>
    </html>
    ```
    
    這個 **`index.html`** 包括一個歡迎消息，提供了兩個連結到不同部分的按鈕，這些部分將顯示即時數據和指定時間範圍內的數據。你可以根據你的需求自定義此模板。
    

### 評分項（三）使用Flask製作後端API設計（Backend）

- 操作資料庫
    
    **我：**
    
    生成一個用於操作 SQLite 資料庫的程式碼。需要一個用來初始化資料庫的函式，以及用來從資料庫中擷取資料的函式
    
    **chatgpt：**
    
    以下是用於操作 SQLite 資料庫的程式碼：
    
    ```python
    import sqlite3
    from datetime import datetime
    
    DB_NAME = "sensor_data.db"
    
    def init_database(db_name):
        """
        初始化資料庫，如果資料表不存在則創建它。
        
        Args:
            db_name (str): 資料庫檔案名稱。
        """
        try:
            with sqlite3.connect(db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_data
                                  (temperature REAL, humidity REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
                conn.commit()
            print("Database initialized successfully.")
        except Exception as e:
            print(f"Error initializing database: {str(e)}")
    
    def fetch_data(start_time, end_time, db_name):
        """
        從資料庫中擷取指定時間範圍內的溫濕度資料。
        
        Args:
            start_time (str): 查詢開始時間，格式為 'YYYY-MM-DD HH:MM:SS'。
            end_time (str): 查詢結束時間，格式為 'YYYY-MM-DD HH:MM:SS'。
            db_name (str): 資料庫檔案名稱。
        
        Returns:
            list: 包含查詢結果的元組列表，每個元組包含溫度、濕度和時間戳記。
        """
        try:
            with sqlite3.connect(db_name) as conn:
                cursor = conn.cursor()
                query = "SELECT temperature, humidity, timestamp FROM sensor_data WHERE timestamp BETWEEN ? AND ?"
                print(f"Executing query: {query} with start_time: {start_time}, end_time: {end_time}")
                cursor.execute(query, (start_time, end_time))
                rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(f"Error retrieving data: {str(e)}")
            return None
    
    ```
    
    這個程式碼包含了初始化資料庫的函式 **`init_database`**，以及從資料庫中擷取資料的函式 **`fetch_data`** 。
    
- app.py 獲取即時資料、區間資料
    
    **我**：建立一個 Flask 應用程式。app應該有一個路由“/get_data”，該路由根據指定時間範圍內從名為「sensor_data.db」的 SQLite 資料庫的時間傳回溫度、濕度和時間戳記。
    
    **chatgpt**：
    
    這個程式碼創建了一個 Flask 應用程式，其中定義了一個路由 '/get_data'。當有人訪問該路由時，我們從請求的查詢字串中獲取了 **`start_time`** 和 **`end_time`**，然後使用這些時間參數調用 **`fetch_data`** 函式來擷取指定時間範圍內的溫濕度資料。最後，我們將資料以 JSON 格式返回到用戶端。
    
    ```python
    from flask import Flask, jsonify, request
    from db_method import fetch_data
    
    app = Flask(__name__)
    
    @app.route('/get_data')
    def get_data():
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')
        if not start_time or not end_time:
            return jsonify({"error": "Both start_time and end_time parameters are required"}), 400
        
        data = fetch_data(start_time, end_time, DB_NAME)
        if data:
            formatted_data = []
            for entry in data:
                temperature, humidity, timestamp = entry
                formatted_data.append({"temperature": temperature, "humidity": humidity, "timestamp": timestamp})
            return jsonify(formatted_data)
        else:
            return jsonify({"error": "Failed to retrieve data from database"}), 500
    
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
    ```
    

### **介面展示 使用highchart視覺化資料**

### 評分項（四）

**介面（一）呈現即時數據，5秒更新一次**

1. 顯示當前日期時間
2. 顯示每筆即時溫濕度資料之數值、日期時間

![截圖 2024-05-31 凌晨2.11.08.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-05-31_%25E5%2587%258C%25E6%2599%25A82.11.08.png)

### 評分項（五）

**介面（二）觀看過去某個時間區段資料**

防呆：開始和結束的時間僅能選取當下之前，並且當選取之結束時間早於開始時間會跳出警告

![截圖 2024-05-31 凌晨1.09.06.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-05-31_%25E5%2587%258C%25E6%2599%25A81.09.06.png)

結束時間早於開始時間會跳出警告

![截圖 2024-05-31 凌晨1.11.31.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-05-31_%25E5%2587%258C%25E6%2599%25A81.11.31.png)

成功選擇範圍之輸出圖表

![截圖 2024-05-31 凌晨1.12.36.png](HW6%20rasberry%20pi%20&%20%E6%BA%AB%E6%BF%95%E5%BA%A6%E6%84%9F%E6%B8%AC%E5%99%A8%207da8a2a3a7be42ccbcef17c2ff8bd76f/%25E6%2588%25AA%25E5%259C%2596_2024-05-31_%25E5%2587%258C%25E6%2599%25A81.12.36.png)

螢幕錄影：[https://youtu.be/orSADZQNSOg](https://youtu.be/orSADZQNSOg)

[https://youtu.be/orSADZQNSOg](https://youtu.be/orSADZQNSOg)