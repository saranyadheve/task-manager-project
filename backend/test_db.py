from database import engine

try:
    conn = engine.connect()
    print("MySQL Connected Successfully!")
    conn.close()
except Exception as e:
    print("Error connecting to MySQL:", e)
