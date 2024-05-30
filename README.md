# HW6 rasberry pi & 溫濕度感測器

**資管三 4110029009 王致雅**

以下以序列圖說明本實驗之溫濕度數據的收集、存儲和呈現過程

<img width="812" alt="截圖 2024-05-31 凌晨2 59 59" src="https://github.com/jhihyawang/rasberrypi4_esp32_dht11/assets/157604262/2463bd01-e911-4d59-882f-0fa8462bdae8">

以下是各個參與者的角色：

- **ESP32:** ESP32，負責收集溫濕度數據並通過 HTTP POST 請求將其發送到 app.py 伺服器。
- **app.py 伺服器**: 應用程序伺服器，接收來自 ESP32 的數據並將其存儲在資料庫 sensor_data.db 中。同時，它還提供了兩個網頁界面，即時數據頁面（realtime.html）和選擇時間範圍的數據頁面（specifictime.html）。
- **sensor_data.db**: 資料庫，用於存儲溫濕度數據。
- **realtime.html 和 specifictime.html**: 兩個前端頁面，用於呈現即時數據和特定時間範圍的數據。它們分別向 app.py 伺服器發送 HTTP GET 請求以獲取數據。
- **realtime.js 和 specifictime.js**: 兩個前端 JavaScript 腳本，用於處理從 app.py 伺服器獲取的數據並在網頁界面上呈現。    

### **介面展示 使用highchart視覺化資料**

**介面（一）呈現即時數據，5秒更新一次**

1. 顯示當前日期時間
2. 顯示每筆即時溫濕度資料之數值、日期時間

<img width="1280" alt="截圖 2024-05-31 凌晨2 11 08" src="https://github.com/jhihyawang/rasberrypi4_esp32_dht11/assets/157604262/e500eaa2-83ac-4422-94b2-dce3cab73049">


**介面（二）觀看過去某個時間區段資料**

防呆：開始和結束的時間僅能選取當下之前

<img width="1280" alt="截圖 2024-05-31 凌晨1 09 06" src="https://github.com/jhihyawang/rasberrypi4_esp32_dht11/assets/157604262/581d41ef-a153-41b1-a370-d1e213fafaaa">

選取時間超過當前時間或結束時間早於開始時間會跳出警告

<img width="1280" alt="截圖 2024-05-31 凌晨1 10 55" src="https://github.com/jhihyawang/rasberrypi4_esp32_dht11/assets/157604262/e8564379-092d-4c8e-bb51-474fa9dd3162">

<img width="766" alt="截圖 2024-05-31 凌晨3 06 34" src="https://github.com/jhihyawang/rasberrypi4_esp32_dht11/assets/157604262/d256a1b4-f10e-4672-ae8e-ac866a79a8be">


成功選擇範圍之輸出圖表
<img width="766" alt="截圖 2024-05-31 凌晨3 07 03" src="https://github.com/jhihyawang/rasberrypi4_esp32_dht11/assets/157604262/603353ce-9c4f-45c4-89e5-09b27f2d0ae1">

[![IMAGE ALT TEXT](http://img.youtube.com/vi/orSADZQNSOg/0.jpg)](https://youtu.be/orSADZQNSOg)


