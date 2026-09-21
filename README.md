# 🎓 Student Hub

A modern, beautifully designed student community platform built with Flask — featuring a premium dark UI with glassmorphism, gradient accents, and smooth animations. Sign up, write blog posts, search content, manage profiles, and grow together.

## ✨ Features

- **User Authentication** — Secure signup, login & logout with hashed passwords
- **Blog System** — Create, read, and browse blog posts
- **Search** — Find posts by title or content instantly
- **Delete Posts** — Remove your own posts with a confirmation prompt
- **User Profiles** — View and edit your username, email & password
- **Flash Messages** — Real-time success/error notifications on every action
- **Premium Dark UI** — Glassmorphism cards, violet-to-emerald gradient accents, pill-shaped buttons, animated background orbs, and micro-interactions

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Flask, Flask-SQLAlchemy, Flask-Login |
| Database | SQLite |
| Frontend | HTML5, CSS3, Outfit + Inter (Google Fonts) |
| Security | Werkzeug password hashing |
| Design | Glassmorphism, Violet/Blue/Emerald gradient palette, pill buttons, CSS animations |

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

## 🎨 UI Design

The UI features a **premium dark aesthetic** with:

- 🌈 **Violet → Sky Blue → Emerald** gradient color system
- 💊 **Pill-shaped buttons** with animated gradient fills and glow shadows
- 🪟 **Glassmorphism** — frosted-glass cards with `backdrop-filter` blur
- ✨ **Animated background orbs** — soft gradient circles that float gently
- 🎯 **Micro-animations** — shimmer stripes, hover lifts, icon bounces
- 🔤 **Outfit font** — modern, clean typography

| Page | Description |
|------|------------|
| **Home** | Hero section with gradient accent text, glass feature cards with shimmer borders, and gradient stats |
| **Login / Signup** | Frosted glass card with gradient top bar, violet focus rings, and gradient submit button |
| **Blog** | Pill-shaped search bar + glass cards with left accent stripe on hover |
| **Profile** | User info with gradient accents and smooth edit flow |

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
