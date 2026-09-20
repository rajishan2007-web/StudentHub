# 🎓 Student Hub

A modern student community platform built with Flask — where students can sign up, write blog posts, search content, manage profiles, and grow together.

## ✨ Features

- **User Authentication** — Secure signup, login & logout with hashed passwords
- **Blog System** — Create, read, and browse blog posts
- **Search** — Find posts by title or content instantly
- **Delete Posts** — Remove your own posts with a confirmation prompt
- **User Profiles** — View and edit your username, email & password
- **Flash Messages** — Real-time success/error notifications on every action
- **Dark Premium UI** — Minimal dark theme with teal accents and smooth animations

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Flask, Flask-SQLAlchemy, Flask-Login |
| Database | SQLite |
| Frontend | HTML5, CSS3, Inter (Google Font) |
| Security | Werkzeug password hashing |
| Design | Dark theme, Teal/Cyan accents, CSS animations |

## 📁 Project Structure

```
student_hub/
├── run.py                    # App entry point
├── config.py                 # Configuration settings
├── requirements.txt          # Python dependencies
├── .gitignore
├── app/
│   ├── __init__.py           # App factory
│   ├── models.py             # Database models (User, Post)
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py           # Signup, Login, Logout
│   │   ├── blog.py           # Blog CRUD + Search
│   │   ├── main.py           # Homepage
│   │   └── profile.py        # Profile view + edit
│   ├── static/
│   │   └── css/
│   │       └── style.css     # All styles (dark theme)
│   └── templates/
│       ├── base.html         # Base layout + navbar + flash
│       ├── index.html        # Homepage
│       ├── auth/
│       │   ├── login.html
│       │   └── signup.html
│       ├── blog/
│       │   ├── list.html     # All posts + search
│       │   ├── new.html      # Create post
│       │   └── view.html     # Single post
│       └── profile/
│           ├── view.html     # Profile dashboard
│           └── edit.html     # Edit profile form
└── instance/
    └── database.db           # SQLite database (auto-generated)
```

## 🚀 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/rajishan2007-web/StudentHub.git
   cd StudentHub
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python run.py
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

## 🎨 UI Preview

| Page | Description |
|------|------------|
| **Home** | Dark hero section with gradient accent text, feature cards, and stats bar |
| **Login / Signup** | Centered glass card form with teal focus rings |
| **Blog** | Search bar + post cards with hover effects and delete option |
| **Profile** | User info card with edit button and post management |

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
