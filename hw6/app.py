from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime
from db_method import DB_NAME, init_database, fetch_data

app = Flask(__name__, template_folder="templates")

sensor_data = {"temperature": [], "humidity": []}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/visualize-realtime", methods=["GET"])
def visualize_realtime():
    return render_template("realtime.html")

@app.route("/visualize-specifiedtime", methods=["GET"])
def visualize_specified_time():
    return render_template("specifiedtime.html")

# @app.route('/post_data')
# def generate_sensor_data():
#     while True:
#         try:
#             humidity = random.uniform(40, 60)
#             temperature = random.uniform(20, 30)
#             sensor_data["temperature"].append(temperature)
#             sensor_data["humidity"].append(humidity)
#             with sqlite3.connect(DB_NAME) as conn:
#                 cursor = conn.cursor()
#                 current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#                 cursor.execute(
#                     "INSERT INTO sensor_data (temperature, humidity, timestamp) VALUES (?, ?, ?)", 
#                     (temperature, humidity, current_time)
#                 )
#                 conn.commit()
#         except Exception as e:
#             print(f"Error generating sensor data: {str(e)}")
#         time.sleep(2)

@app.route('/post_data', methods=['POST'])
def receive_data():
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
            temperature, humidity, timestamp = entry[0], entry[1], entry[2]
            formatted_data.append({"temperature": temperature, "humidity": humidity, "timestamp": timestamp})
        return jsonify(formatted_data)
    else:
        return jsonify({"error": "Failed to retrieve data from database"}), 500


if __name__ == "__main__":
    init_database(DB_NAME)
    app.run(host="0.0.0.0", port=5000, debug=True)
