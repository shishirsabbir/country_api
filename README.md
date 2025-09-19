# 🌍 Country API Service

Welcome to the **Country API Service**! This project is a comprehensive API platform for managing and exploring country data, featuring a modern admin panel built with Jinja, FastAPI, and a beautiful frontend powered by HTML, CSS, and JavaScript.

---

## 🚀 Project Overview

The Country API Service provides a robust backend for storing, retrieving, and managing country information. It includes an intuitive admin panel for administrators to view, add, and update country records. The project is designed for scalability, flexibility, and ease of integration with other systems.

---

## 🏗️ Features

- **RESTful API Endpoints** for country data
- **Admin Panel** built with Jinja templates
- **Add & Edit Country** via web forms
- **Rich Country Data**:
  - Country Name
  - Country Code (Alpha-2)
  - Country Phone Code
  - Short & Full Description
  - Country Flag (SVG)
  - Cover Images (1-5)
  - Population & GDP (optional)
  - And more!
- **Responsive Frontend** with HTML, CSS, JavaScript
- **Secure & Fast** using FastAPI
- **Easy Integration** for other apps and services

---

## 🛠️ Tech Stack

- **Backend:** FastAPI 🏎️
- **Templating:** Jinja2 🧩
- **Frontend:** HTML, CSS, JavaScript 🎨
- **Database:** (To be decided: PostgreSQL, SQLite, etc.)
- **Image & SVG Handling:** Native & third-party libraries

---

## 👥 Contributors

- **Fullstack Developer:** Shishir Sabbir
- **Backend Developer:** Elias Ahmed
- **Frontend Designer:** Sifat Raihan

> Special thanks to all collaborators for their dedication and creativity! ✨

---

## 📦 Installation & Setup

1. **Clone the repository:**
	```bash
	git clone https://github.com/shishirsabbir/country_api.git
	cd country_api
	```
2. **Create a virtual environment:**
	```bash
	python -m venv venv
	venv\Scripts\activate  # On Windows
	```
3. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```
4. **Run the FastAPI server:**
	```bash
	uvicorn main:app --reload
	```
5. **Access the admin panel:**
	- Open your browser and go to: `http://localhost:8000/admin`

---

## 📚 API Endpoints

- `GET /countries` — List all countries
- `GET /countries/{code}` — Get details for a specific country
- `POST /countries` — Add a new country
- `PUT /countries/{code}` — Update country data
- `DELETE /countries/{code}` — Remove a country

> All endpoints return JSON responses. Admin panel uses Jinja templates for rendering.

---

## 🖼️ Country Data Model

Each country record includes:
- `name`: Country name
- `code`: Alpha-2 code
- `phone_code`: International phone code
- `short_description`: Brief summary
- `full_description`: Detailed info
- `flag_svg`: SVG markup for flag
- `cover_images`: List of up to 5 image URLs
- `population`: (Optional) Population count
- `gdp`: (Optional) GDP value
- ...and more fields as needed

---

## 🎨 Admin Panel

- Built with Jinja2 for fast, dynamic rendering
- Add, edit, and view country records
- Upload flag SVGs and cover images
- Responsive design for desktop and mobile

---

## 📝 Usage Examples

### Fetch All Countries
```http
GET /countries
```

### Add a New Country
```http
POST /countries
Content-Type: application/json
{
  "name": "Japan",
  "code": "JP",
  "phone_code": "+81",
  "short_description": "Land of the Rising Sun",
  "full_description": "Japan is an island country in East Asia...",
  "flag_svg": "<svg>...</svg>",
  "cover_images": ["url1", "url2"],
  "population": 125800000,
  "gdp": 5.1
}
```

---

## 🏆 Goals & Vision

- Deliver a reliable, scalable API for country data
- Provide a beautiful, user-friendly admin panel
- Enable easy integration for other apps and services
- Foster collaboration and innovation

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 📬 Contact & Support

For questions, suggestions, or contributions:
- **Lead:** Shishir Sabbir ([GitHub](https://github.com/shishirsabbir))
- **Collaborators:** Elias Ahmed, Sifat Raihan

Feel free to open issues or pull requests!

---

## 💡 Acknowledgements

Thanks to all contributors and the open-source community for inspiration and support! 🙏