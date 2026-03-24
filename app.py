from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, send, emit
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, async_mode='eventlet')

# ---------- DB ----------
conn = sqlite3.connect('chat.db', check_same_thread=False)
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    message TEXT,
    timestamp TEXT
)
''')
conn.commit()

# track users
online_users = 0

# ---------- ROUTES ----------
@app.route('/')
def index():
    return render_template('chat.html')


@app.route('/history')
def history():
    c.execute("SELECT username, message, timestamp FROM messages ORDER BY id ASC")
    return jsonify({"messages": c.fetchall()})


# ---------- SOCKET EVENTS ----------

# 🔵 user connected
@socketio.on('connect')
def handle_connect():
    global online_users
    online_users += 1
    emit('user_count', {'count': online_users}, broadcast=True)


# 🔴 user disconnected
@socketio.on('disconnect')
def handle_disconnect():
    global online_users
    online_users -= 1
    emit('user_count', {'count': online_users}, broadcast=True)


# 💬 message send
@socketio.on('message')
def handle_message(msg):
    time = datetime.now().strftime("%I:%M %p")

    if "|" in msg:
        username, message_text = msg.split("|", 1)

        # save to DB
        c.execute(
            "INSERT INTO messages (username, message, timestamp) VALUES (?, ?, ?)",
            (username.strip(), message_text.strip(), time)
        )
        conn.commit()

        # broadcast
        send(f"{username}|{message_text}", broadcast=True)


# ✏ typing indicator
@socketio.on('typing')
def handle_typing(data):
    emit('typing', data, broadcast=True, include_self=False)


# ---------- RUN ----------
if __name__ == '__main__':
    socketio.run(app, debug=True)