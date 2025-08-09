from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
# ========= Script to Frontend ======= #
raw_script = ""

def set_script(script):
    global raw_script
    raw_script = script

def get_script():
    return raw_script
    
# ========== Create table once when app starts ==========
def init_db():
    conn = sqlite3.connect("cell_database.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cellData (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Cell_Name TEXT,
            Content_Type TEXT,
            Upload_To TEXT,
            Schedule TEXT,
            Frequent INT,
            Auto_Run TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ========== Insert data into database ==========
def insert_data(cellName, contentType, uploadTo, schedule, frequent, autoRun):
    conn = sqlite3.connect("cell_database.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cellData (
            Cell_Name, Content_Type, Upload_To, Schedule, Frequent, Auto_Run
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (cellName, contentType, uploadTo, schedule, frequent, autoRun))
    conn.commit()
    conn.close()

# ========== Route to receive data ==========
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    print("Received:", data)

    cell_name = data.get('cellName')
    content_name = data.get('contentName')
    tags = data.get('platformsToUpload', [])
    platform_to_upload = ",".join(tags)
    schedule = data.get('scheduleTime')
    frequent_limit = data.get('frequentLimit')
    auto_run = data.get('autoRun')
# ===== Get Script ===== #
    raw_script = data.get('script')
    with open("script_dump.txt", "w", encoding="utf-8") as f:
        f.write(raw_script)
    # inside submit():
    set_script(data.get('script'))
    
    insert_data(cell_name, content_name, platform_to_upload, schedule, frequent_limit, auto_run)

    return jsonify({"status": "success", "message": "Data saved to database"})

@app.route('/get', methods=['GET'])
def get_data():
    conn = sqlite3.connect("cell_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cellData")
    rows = cursor.fetchall()
    conn.close()

    # Convert rows to list of dictionaries
    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "cellName": row[1],
            "contentType": row[2],
            "uploadTo": row[3],
            "schedule": row[4],
            "frequent": row[5],
            "autoRun": row[6]
        })
    print("Sending to FrontEnd",result)
    print("script",raw_script)
    return jsonify(result)

    
# ========== Run Server ==========
if __name__ == '__main__':
    app.run(debug=True)

