import pytesseract
from PIL import Image, ImageTk
import cv2
from tkinter import filedialog, Tk, Label, Button, Text, Scrollbar, END, ttk, Menu, messagebox, Canvas
import os
import time

# Set up the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Tesseract configuration to optimize cursive text recognition
tess_config = '--oem 1 --psm 6'

# Function to scan an image and extract text
def scan_document(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, config=tess_config)
    return text

# Function to capture image from webcam and scan it
def scan_from_webcam():
    global camera_feed_label
    cap = cv2.VideoCapture(0)

    def show_frame():
        _, frame = cap.read()
        if frame is not None:
            # Convert the frame to a format Tkinter can display
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)

            # Show the frame on the Label
            camera_feed_label.imgtk = imgtk
            camera_feed_label.configure(image=imgtk)
        
        # Continue to update the frame in real-time
        camera_feed_label.after(10, show_frame)

    show_frame()

# Function to capture image from webcam and scan it for text
def capture_and_scan_from_webcam():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        image_path = "captured_image.png"
        cv2.imwrite(image_path, frame)
        cap.release()
        extracted_text = scan_document(image_path)
        text_box.delete(1.0, END)
        text_box.insert(END, extracted_text)
    else:
        messagebox.showerror("Error", "Unable to access webcam.")

# Function to browse and select an image
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        # Simulate loading and update progress bar
        progress_bar['value'] = 0
        root.update_idletasks()

        for i in range(1, 101):
            time.sleep(0.03)
            progress_bar['value'] = i
            root.update_idletasks()

        extracted_text = scan_document(file_path)
        text_box.delete(1.0, END)
        text_box.insert(END, extracted_text)

        progress_bar['value'] = 100

# Function to export text as a file
def export_as_txt():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(text_box.get(1.0, END))
        messagebox.showinfo("Export", f"File saved as {file_path}")

# Function to export text as PDF (basic implementation)
def export_as_pdf():
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(text_box.get(1.0, END))
        messagebox.showinfo("Export", f"PDF saved as {file_path}")

# Placeholder function for future conversions
def coming_soon():
    messagebox.showinfo("Coming Soon", "This feature will be available in a future update!")

# Function to quit the application
def quit_app():
    root.destroy()

# Create the GUI
root = Tk()
root.title("Document Translator Scanner")
root.geometry("900x700")
root.config(bg='#ffffff')  # White modern background

# Create tabs for menu transitions
notebook = ttk.Notebook(root)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text="Scan Image")
notebook.add(frame2, text="Scan with Webcam")
notebook.pack(expand=1, fill="both")

# Style for buttons and progress bar
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 14))
style.configure("TProgressbar", thickness=20)

# Add a modern label for the title
title_label = Label(root, text="Document Translator Scanner", font=("Helvetica", 24, "bold"), bg='#ffffff', fg='#333333')
title_label.pack(pady=20)

# Tab 1: Browse Image for Scanning
browse_label = Label(frame1, text="Upload Image to Scan", font=("Helvetica", 16), bg='#ffffff')
browse_label.pack(pady=10)

browse_button = ttk.Button(frame1, text="Browse Image", command=browse_file)
browse_button.pack(pady=10)

# Progress bar for loading
progress_bar = ttk.Progressbar(frame1, orient='horizontal', length=500, mode='determinate')
progress_bar.pack(pady=10)

# Tab 2: Webcam Scanning
webcam_label = Label(frame2, text="Capture from Webcam to Scan", font=("Helvetica", 16), bg='#ffffff')
webcam_label.pack(pady=10)

webcam_button = ttk.Button(frame2, text="Start Webcam Feed", command=scan_from_webcam)
webcam_button.pack(pady=10)

capture_button = ttk.Button(frame2, text="Capture and Scan", command=capture_and_scan_from_webcam)
capture_button.pack(pady=10)

# Label to display webcam feed
camera_feed_label = Label(frame2, bg='#ffffff')
camera_feed_label.pack(pady=10)

# Text box to display extracted text
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
text_box = Text(root, wrap="word", yscrollcommand=scrollbar.set, height=10, font=("Helvetica", 12), bg='#f9f9f9', fg='#333333')
text_box.pack(expand=True, fill="both", padx=20, pady=20)
scrollbar.config(command=text_box.yview)

# Export Menu (added as a dropdown)
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Export as .txt", command=export_as_txt)
file_menu.add_command(label="Export as .pdf", command=export_as_pdf)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_app)

convert_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Convert", menu=convert_menu)
convert_menu.add_command(label="Coming Soon", command=coming_soon)
root.config(menu=menu_bar)

# Add infamous troll face logo in the bottom right corner
def add_troll_face():
    logo_path = r'assets/sterf.png'  # Update this to match the correct path
    logo = Image.open(logo_path)
    logo = logo.resize((100, 100))  # Resize the image
    logo = ImageTk.PhotoImage(logo)
    logo_label = Label(root, image=logo, bg='#ffffff')
    logo_label.image = logo  # Keep a reference to avoid garbage collection
    logo_label.place(x=780, y=580)  # Position the logo in the bottom-right corner

add_troll_face()

# Add a version info label
version_label = Label(root, text="v0.2 - Coded by Sterf.exe", font=("Helvetica", 10), bg='#ffffff', fg='#666666')
version_label.pack(side="bottom", pady=10)

# Run the GUI loop
root.mainloop()
