# 🎓 Student Hub

A student community platform built with Flask where users can sign up, write blog posts, and manage their profiles.

## Features

- **User Authentication** — Signup, login, and logout with secure password hashing
- **Blog System** — Create, read, and browse blog posts
- **User Profiles** — View your profile info and all your published posts
- **Glassmorphism UI** — Modern glass-effect design with gradient backgrounds

## Tech Stack

- **Backend:** Flask, Flask-SQLAlchemy, Flask-Login
- **Database:** SQLite
- **Frontend:** HTML5, CSS3 (Glassmorphism + Poppins font)
- **Security:** Werkzeug password hashing

## Project Structure

```
student_hub/
├── run.py
├── config.py
├── requirements.txt
├── .gitignore
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── blog.py
│   │   ├── main.py
│   │   └── profile.py
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── auth/
│       │   ├── login.html
│       │   └── signup.html
│       ├── blog/
│       │   ├── list.html
│       │   ├── new.html
│       │   └── view.html
│       └── profile/
│           └── view.html
└── instance/
    └── database.db
```

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/rajishan2007-web/StudentHub.git
   cd StudentHub
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the app**
   ```bash
   python run.py
   ```

6. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

## Screenshots

| Home Page | Login | Blog |
|-----------|-------|------|
| Gradient hero section with feature cards | Glass-effect login form | Post listing with author info |

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).
