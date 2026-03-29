# 🛒 Smart Product Locator (Django + AI Inspired)

A smart supermarket kiosk system that helps customers quickly locate products using search and voice input, while allowing store owners to manage inventory through a custom admin panel.

---

## 🚀 Features

### 👤 Customer Side
- 🔍 Search products by name or brand
- 📍 Displays product location (Aisle & Rack)
- 📦 Shows stock availability
- 🔁 Suggests alternative products if out of stock
- 🎤 Voice search using Web Speech API
- ⏱️ Auto reset (kiosk behavior)

---

### ⚙️ Admin Panel
- 🔐 Password-protected access
- ➕ Add new products
- ✏️ Edit existing products
- 🗑️ Delete products
- 🔍 Search products
- 📂 Dynamic category & brand creation (autocomplete + add new)
- 🧭 Easy navigation (back buttons)

---

## 🧠 Future Scope

- 🔗 Integration with billing/POS system for automatic stock updates
- 📊 Analytics (most searched products)
- 🗺️ Store map visualization
- 🔊 Voice output (text-to-speech)
- 📱 Tablet/Kiosk deployment

---

## 🛠️ Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite
- **AI Features:** Voice input (Web Speech API)

---

## 📸 Screenshots

*(Add screenshots here later)*

---

## ⚙️ Installation

```bash
# Clone repo
git clone https://github.com/anjalad0085/smart-product-locator.git

# Go to project
cd smart-product-locator

# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate   # Windows

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Run server
python manage.py runserver