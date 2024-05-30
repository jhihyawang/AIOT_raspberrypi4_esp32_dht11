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




