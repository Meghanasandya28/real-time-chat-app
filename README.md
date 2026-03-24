# 💬 Real-Time Chat Application

A simple real-time chat application built using **Python, Flask, and Socket.IO**.
This application allows multiple users to send and receive messages instantly through a web interface.

---

# 📸 Project Preview

### Chat Interface

Users can enter their name and start chatting instantly.

### Real-Time Messaging

Messages appear instantly for all connected users without refreshing the page.

---

# 📌 Project Objective

* Build a simple **real-time messaging system**
* Understand **WebSockets communication**
* Learn how **Flask + Socket.IO** work together
* Create a **clean chat UI using HTML and CSS**

---

# 🧠 Technologies Used

* Python
* Flask
* Flask-SocketIO
* SQLite
* HTML
* CSS
* JavaScript

---

# 💻 Tech Stack

Python | Flask | Socket.IO | SQLite | HTML | CSS | JavaScript

---

# 📁 Project Structure

real-time-chat-app/

│

├── app.py
├── requirements.txt
├── chat.db

│

├── templates/
│ └── chat.html

│

├── static/
│ └── style.css

---

# ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/Meghanasandya28/real-time-chat-app.git
cd real-time-chat-app
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```
python app.py
```

### 4️⃣ Open in Browser

```
http://localhost:5000
```

---

# 🔄 How the Chat App Works

1. User opens the chat page
2. User enters a username
3. Message is sent through **Socket.IO**
4. Server receives the message
5. Message is stored in **SQLite database**
6. Server broadcasts the message to all users
7. All users see the message instantly

---

# 📊 Features

* Real-time messaging
* Multiple users chat support
* Message timestamps
* Message history storage
* Clean chat interface
* Enter key to send messages

---

# 🏗 System Architecture

Frontend
HTML + CSS + JavaScript interface

Backend
Flask server handling requests

WebSocket Layer
Flask-SocketIO enabling real-time communication

Database
SQLite storing chat history

---

# 👨‍💻 Author

**Meghana Sandya**

📧 Email
[22nn1a0480@gmail.com](mailto:22nn1a0480@gmail.com)

💻 GitHub
https://github.com/Meghanasandya28
