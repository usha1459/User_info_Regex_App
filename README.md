# 🧾 User Info Streamlit App

This is a modern and visually styled Streamlit web app for collecting **user information** with basic validation using regular expressions. The app provides a downloadable **CSV** and **PDF receipt** of the submitted data.

---

## ✅ Features

- Beautiful warm UI with background image and styling
- Fields:
  - Full Name (validated with regex)
  - Date of Birth (must be 18+)
  - Email Address (validated with regex)
  - Mobile Number (validated with regex, 10 digits)
- Real-time age display
- Validation feedback (warnings for incorrect input)
- Download options:
  - CSV file with submitted info
  - PDF receipt with details

---

## 📁 Project Structure
```bash
User_Info_Regex_App/
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
└── README.md # Project documentation (this file)
````

---

## 🚀 How to Run

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
2. Run the Streamlit app
``` bash
streamlit run app.py
```
📦 Requirements
Contents of requirements.txt:
``` bash
nginx
Copy
Edit
streamlit
fpdf
pandas
```

📄 Output Example
After submission, the user can:

See the validated output on screen

Download the details as:

📄 A PDF named user_info.pdf

📊 A CSV named user_info.csv

🛡️ Validations Used
Field	Validation Pattern
Name	Only letters and spaces
Email	Standard email format (e.g., abc@example.com)
Mobile	Exactly 10 digits
DOB	Must be at least 18 years old

👤 Author
Prathyusha Kopur
🔗 GitHub: usha1459(https://github.com/usha1459)

