# 🐳 Flask + MySQL Docker Compose Project

A retro-styled Flask web application connected to MySQL database, containerized with Docker Compose. Built as a hands-on learning project for mastering Docker Compose, Flask development, and MySQL integration.

## 📚 What I Learned

This project was my journey into:
- 🐋 Docker Compose multi-container orchestration
- 🔧 Troubleshooting Flask-MySQL connectivity issues
- 🗄️ Database configuration in containerized environments
- 🌐 Building full-stack web apps with Docker

## 🎯 Features

- **Retro UI**: Classic terminal-inspired interface with green-on-black styling
- **Flask Backend**: Lightweight Python web framework
- **MySQL Database**: Persistent data storage with Docker volumes
- **Live Clock**: Real-time updates on the homepage
- **Database Query**: Test endpoint that fetches data from MySQL

## 🏗️ Project Structure

```
.
├── app.py                  # Flask application
├── docker-compose.yml      # Multi-container orchestration
├── Dockerfile             # Web app container configuration
├── requirements.txt       # Python dependencies
└── templates/
    └── index.html         # Retro-styled homepage
```

## 🚀 Quick Start

### Prerequisites
- Docker
- Docker Compose

### Running the Application

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. **Start the containers**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Homepage: `http://localhost:5000`
   - Test endpoint: `http://localhost:5000/hello`

4. **Stop the containers**
   ```bash
   docker-compose down
   ```

## 🔌 Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Retro-styled homepage with animated stats |
| `/hello` | Simple Hello page |

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript (vanilla)
- **Backend**: Flask (Python)
- **Database**: MySQL 5.7
- **Containerization**: Docker & Docker Compose

## 📦 Container Services

### `web` - Flask Application
- **Image**: python:3.9.23-slim-trixie
- **Port**: 5000
- **Environment**: Development mode with hot-reload

### `db` - MySQL Database
- **Image**: MySQL 5.7
- **Port**: 3306
- **Database**: `test_db`
- **Persistent Storage**: Docker volume `db_data`

## 🐛 Common Issues & Solutions

### Database Connection Errors
If you see connection refused errors, the MySQL container might still be initializing. Wait 10-15 seconds and refresh.

### Port Already in Use
If port 5000 or 3306 is busy:
```bash
# Change ports in docker-compose.yml
ports:
  - "5001:5000"  # Use different host port
```

### Container Won't Start
Clean up and rebuild:
```bash
docker-compose down -v
docker-compose up --build
```

## 🎨 Customization

### Change Database Credentials
Edit `docker-compose.yml` and `app.py` with matching credentials:
```yaml
# docker-compose.yml
environment:
  MYSQL_ROOT_PASSWORD: your_password
```

```python
# app.py
password = 'your_password'
```

### Modify the UI
Edit `templates/index.html` to customize colors, text, or add new features.

## 📝 Notes

- The database persists data in a Docker volume (`db_data`)
- Flask runs in development mode with auto-reload enabled
- MySQL takes ~10 seconds to fully initialize on first run

## 🎓 Learning Resources

Things that helped me along the way:
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)

## 🤝 Contributing

This is a learning project, but feel free to fork it and make it your own!

## 📄 License

Free to use for learning purposes.

---


