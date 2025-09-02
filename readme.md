## 📘 GCBlogger — Share Your Story

GCBlogger is a clean, modular blogging platform built with Django. It empowers users to share their stories, manage posts, and engage through comments—all wrapped in a responsive, user-friendly interface.

---

### 🚀 Features

- 🧑‍💻 **Custom User Profiles**  
  Extended user model with avatar, bio, and slug-based URLs.

- ✍️ **Post Management**  
  Create, edit, delete posts with image uploads and SEO-friendly slugs.

- 💬 **Comment System**  
  Authenticated users can comment on blog posts.

- 📬 **Contact Form**  
  Visitors can send messages directly to the site owner.

- 🔐 **Authentication Flow**  
  Sign-up, sign-in, logout, and password change—all built with Django’s auth system.

- 📱 **Responsive Design**  
  Mobile-first layout with rem-based spacing and a navy blue palette.

---

### 🧱 Tech Stack

| Layer         | Technology         |
|---------------|--------------------|
| Backend       | Django (Python)    |
| Database      | SQLite             |
| Frontend      | HTML, CSS, JS      |
| Auth System   | Django Auth        |
| Media Storage | Local (MEDIA_ROOT) |

---

### 📁 Project Structure

```
gcblogger/
├── blog/
│   ├── models.py         # CustomUser, Post, Comment, ContactMessage
│   ├── forms.py          # SignUpForm, SignInForm, PostForm
│   ├── views.py          # Core views for auth, post CRUD, profile, etc.
│   ├── urls.py           # App-level routing
│   ├── templates/blog/   # HTML templates
│   └── static/blog/      # CSS and JS assets
├── gcblogger/            # Project-level config
│   └── urls.py           # Root routing
```

---

### 🎨 Templates

Each view has its own template, extending `base.html` for consistency:

- `home.html`, `about.html`, `contact.html`
- `auth.html`, `changepassword.html`, `profile.html`
- `createpost.html`, `editpost.html`, `myposts.html`
- `blogs.html`, `blog.html`

---

### 🎨 Static Files

Modular CSS and scoped JS for each view:

- `css/`: `base.css`, `home.css`, `blog.css`, etc.
- `js/`: `header.js`, `signin.js`, `updateProfileImage.js`

All styles use rem units for scalability and accessibility. Navy blue is the primary color across the palette.

---

### ⚙️ Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/gcblogger.git
   cd gcblogger
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations**  
   ```bash
   python manage.py migrate
   ```

4. **Run the server**  
   ```bash
   python manage.py runserver
   ```

5. **Access the app**  
   Visit `http://127.0.0.1:8000/`

---

### 🧠 Design Philosophy

- Modular CSS with rem-based spacing
- Intentional color palette (navy blue primary)
- Clean separation of templates and static assets
- Slug-based URLs for SEO and readability
- Minimal clutter, maximum clarity

---

### 📬 Contact

Built with ❤️ by Gokul  
Feel free to fork, contribute, or reach out with feedback!
