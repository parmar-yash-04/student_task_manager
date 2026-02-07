<h1 align="center">📚 Student Task Manager — FastAPI Backend</h1>

<p align="center">
🔗 <b>Live API:</b> 
<a href="https://yash-task-manager-baq2.onrender.com/" target="_blank">
https://yash-task-manager-baq2.onrender.com/
</a>
<br><br>

A high-performance REST API built with <b>FastAPI, SQLAlchemy, and PostgreSQL</b> for managing student tasks and assignments.
<br>
Secure • Scalable • Cloud-Ready
</p>

<hr>

<h2>🚀 Overview</h2>

<p>
Student Task Manager Backend is a modern REST API that helps students create, update, and track their academic tasks efficiently.
It includes JWT authentication, user-based task ownership, and automatic interactive API documentation.
</p>

<hr>

<h2>✨ Features</h2>

<ul>
<li>🚀 FastAPI high-performance framework</li>
<li>📝 Full CRUD operations for tasks</li>
<li>🔐 JWT Authentication & Authorization</li>
<li>💾 PostgreSQL + SQLAlchemy ORM</li>
<li>🔄 Alembic database migrations</li>
<li>📚 Swagger & ReDoc auto documentation</li>
<li>✅ Pydantic data validation</li>
<li>⚡ Async-ready architecture</li>
<li>☁️ Render cloud deployment ready</li>
<li>🧪 Strong type safety</li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>

<table>
<tr><td><b>Framework</b></td><td>FastAPI</td></tr>
<tr><td><b>Language</b></td><td>Python 3.8+</td></tr>
<tr><td><b>Database</b></td><td>PostgreSQL</td></tr>
<tr><td><b>ORM</b></td><td>SQLAlchemy</td></tr>
<tr><td><b>Migrations</b></td><td>Alembic</td></tr>
<tr><td><b>Validation</b></td><td>Pydantic</td></tr>
<tr><td><b>Server</b></td><td>Uvicorn (ASGI)</td></tr>
<tr><td><b>Deployment</b></td><td>Render</td></tr>
</table>

<hr>

<h2>🚀 Getting Started</h2>

<h3>📌 Prerequisites</h3>
<ul>
<li>Python 3.8+</li>
<li>PostgreSQL</li>
<li>pip</li>
<li>Virtual environment (recommended)</li>
</ul>

<h3>⚙️ Installation</h3>

<pre><code>git clone https://github.com/parmar-yash-04/student_task_manager.git
cd student_task_manager
</code></pre>

<h4>Create Virtual Environment</h4>

<pre><code># Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
</code></pre>

<h4>Install Dependencies</h4>

<pre><code>pip install -r requirements.txt</code></pre>

<h4>Create .env File</h4>

<pre><code>DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
</code></pre>

<h4>Run Application</h4>

<pre><code>uvicorn app.main:app --reload</code></pre>

<p>
API runs at:<br>
<b>http://127.0.0.1:8000</b>
</p>

<hr>

<h2>📖 API Documentation</h2>

<ul>
<li>📘 Swagger UI → http://127.0.0.1:8000/docs</li>
<li>📗 ReDoc → http://127.0.0.1:8000/redoc</li>
</ul>

<hr>

<h2>🔐 Security</h2>

<ul>
<li>bcrypt password hashing</li>
<li>JWT token authentication</li>
<li>OAuth2 password flow</li>
<li>CORS middleware enabled</li>
<li>SQL injection protection</li>
<li>Pydantic input validation</li>
</ul>

<hr>

<h2>☁️ Deployment</h2>

<p>
Configured for <b>Render</b> deployment using <code>render.yaml</code> blueprint setup with managed PostgreSQL.
</p>

<hr>

<h2>📄 License</h2>

<p>MIT License — free to use and modify.</p>

<hr>

<h2>👤 Author</h2>

<p>
<b>Yash Parmar</b><br>
GitHub: https://github.com/parmar-yash-04
</p>

<hr>

<p align="center">
⭐ Star the repo if you found it useful<br>
🚀 Build on top of it
</p>
