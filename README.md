# 🔄 Naukri.com Auto Resume Uploader using Selenium

This Python script automates the process of logging in to your Naukri.com account and uploading your updated resume. It's useful for keeping your profile active and appearing more frequently in recruiter searches.

---

## 🚀 Features

- Auto login to Naukri.com
- Navigates to your profile page
- Uploads the updated resume PDF
- Closes browser after completion

---

## 🧰 Requirements

- Python 3.7 or higher  
- Google Chrome browser  
- ChromeDriver (matching your Chrome version)

---

## 🛠️ Installation Guide

### 1. ✅ Install Python

Download and install Python from the official site:  
https://www.python.org/downloads/

During installation:

- ✅ **Check the box that says** `Add Python to PATH`  
- ✅ **OR** manually set the Environment Variable after installation:
  - Right-click on **This PC** > **Properties**
  - Click **Advanced system settings**
  - Click **Environment Variables**
  - Under **System Variables**, find and edit `Path`
  - Add the path to your Python installation (e.g., `C:\Python311\` and `C:\Python311\Scripts\`)

### 2. ✅ Install Required Python Packages

Open terminal / command prompt and run:

```bash
pip install selenium
```

### 3. ✅ Download ChromeDriver

- Check your Chrome version by visiting: `chrome://settings/help`
- Download matching ChromeDriver from:  
  https://sites.google.com/chromium.org/driver/

- Extract the downloaded file and do the following:

### 📁 Folder Structure Setup

1. Create a folder `C:\WebDriver`  
   Place your downloaded `chromedriver.exe` file inside this folder.

2. Create another folder `C:\NaukriResume`  
   Place your latest resume in PDF format inside this folder with the exact filename:  
   **`resume_updated.pdf`**

---

## 📝 Setup Script Configuration

Open the script and update these variables with your actual data:

```python
EMAIL = "your_email@example.com"
PASSWORD = "yourNaukriPassword"
CHROMEDRIVER_PATH = "C:\\WebDriver\\chromedriver.exe"
RESUME_FILE_PATH = "C:\\NaukriResume\\resume_updated.pdf"
```

Make sure:

- `CHROMEDRIVER_PATH` points to the correct `chromedriver.exe` location.
- `RESUME_FILE_PATH` points to your latest resume PDF.

---

## ▶️ How to Run

Simply open command prompt in the script directory and run:

```bash
python naukri_resume_uploader.py
```

It will:

1. Open Naukri.com
2. Login with your credentials
3. Upload your resume
4. Close the browser

---

## ❗ Notes

- Your credentials are stored in plain text — **use with caution.**
- Make sure your Naukri account is active and working.
- Resume file must be a valid `.pdf` or `.docx`.

---

## 💡 Pro Tips

- Schedule this script weekly using Windows Task Scheduler to keep your profile fresh!
- Avoid running it too frequently to prevent account restrictions.

---

## 📷 Preview

_Example of the script in action (GIF or screenshot goes here, optional)_

---

## 📄 License

MIT License – feel free to modify and use.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.
