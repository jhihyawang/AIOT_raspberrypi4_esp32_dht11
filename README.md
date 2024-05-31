# HW6 rasberry pi & 溫濕度感測器

**資管三 4110029009 王致雅**

本來源碼需更改#define SERVER_URL "http://192.168.50.65:5000/post_data"

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

<img width="1280" alt="截圖 2024-05-31 上午9 26 25" src="https://github.com/jhihyawang/rasberrypi4_esp32_dht11/assets/157604262/f453165c-f690-4bbf-a859-e6d26a54000f">



**介面（二）觀看過去某個時間區段資料**

防呆：開始和結束的時間僅能選取當下之前



選取時間超過當前時間

<img width="1280" alt="截圖 2024-05-31 凌晨1 10 55" src="https://github.com/jhihyawang/rasberrypi4_esp32_dht11/assets/157604262/75deef0d-f929-4dbb-8dfc-c79502332e4d">




成功選擇範圍之輸出圖表
<img width="1280" alt="截圖 2024-05-31 上午9 29 56" src="https://github.com/jhihyawang/rasberrypi4_esp32_dht11/assets/157604262/872b28db-98d4-4cc6-adad-06308e1f7d1d">

[![IMAGE ALT TEXT](http://img.youtube.com/vi/orSADZQNSOg/0.jpg)](https://youtu.be/orSADZQNSOg)


