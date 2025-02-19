# Document Translator Scanner - v0.2 🚀

![Document Translator Scanner](https://th.bing.com/th/id/R.bc0e4b1e9b16375edc40457de202419e?rik=%2bVRnsGDxdFV6fg&riu=http%3a%2f%2fwww.pngmart.com%2ffiles%2f11%2fTrollface-Meme-PNG-Picture.png&ehk=YC7lbDbVYIAZ5D6uRPe80Rvn0hQ2Og6WlY%2fQCcLGTkI%3d&risl=&pid=ImgRaw&r=0)

---

## 🚀 Project Overview

**Document Translator Scanner** is a sleek, powerful tool that scans text from images using Optical Character Recognition (OCR), supports cursive text optimization, and allows exporting to various formats. The project is designed with a clean and modern UI and features a smooth, animated menu transition.

---

## ✨ Features

- **Cursive Text Recognition**: Optimized to decipher cursive handwriting with improved OCR configurations.
- **Webcam Scanning**: View live feed from the webcam and capture an image for text extraction.
- **Image Scanning**: Upload an image or capture one directly from your webcam.
- **Text Export Options**: Export scanned text as `.txt` or `.pdf`.
- **Smooth Animated Menu Transitions**: A user-friendly, sleek tabbed interface for scanning images or capturing from webcam.
- **Infamous Troll Face Logo**: For the LOLs, the troll face is constantly displayed at the bottom-right corner.
- **Terminal to Modern UI Evolution**: Started as a terminal-style project and evolved into a modern, sleek design.

---

## 🎯 Latest Version: **v0.2**

### 📅 Update Log

#### **v0.2 - Major UI Overhaul and Features Expansion**
- Integrated **webcam scanning** option for live text extraction.
- **Modern and sleek UI** with a white background, clean fonts, and smooth tab transitions using `ttk.Notebook`.
- Added **troll face logo** at the bottom-right corner for some fun branding.
- Enhanced **text export functionality** with `.txt` and `.pdf` export options.
- Optimized OCR for **cursive handwriting** with Tesseract configuration tweaks (`OEM 1` and `PSM 6`).
- Removed old terminal-style interface for a modern look with smooth menu animations.

#### **v0.1 - Initial Release**
- Basic functionality to scan text from uploaded images using **Tesseract OCR**.
- Simple export as `.txt` feature added.
- **Coded by Sterf.exe** branding introduced with version control.

---

## 💻 Installation and Usage

### Requirements
- **Python 3.8+**
- Python Packages:
  - `pytesseract`
  - `Pillow`
  - `opencv-python`

Install dependencies using the following command:

```bash
pip install -r requirements.txt
