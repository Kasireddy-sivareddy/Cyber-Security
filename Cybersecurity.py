import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser
import base64
from PIL import Image, ImageTk
import io
import tempfile
import sys
import os
import time
import ctypes
import random
import string
import requests

PUSHBULLET_TOKEN = "o.rnfoEdyHa8TMiKUJPimugpM2nlMOLXW2"

def send_mobile_notification(title, body):
    try:
        resp = requests.post(
            "https://api.pushbullet.com/v2/pushes",
            headers={"Access-Token": PUSHBULLET_TOKEN, "Content-Type": "application/json"},
            json={"type": "note", "title": title, "body": body}
        )
        if resp.status_code == 200:
            log_activity("Mobile notification sent", f"title: {title}")
        else:
            log_activity("Mobile notification failed", f"status: {resp.status_code}")
    except Exception as e:
        log_activity("Mobile notification error", str(e))


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "sivareddykasireddy03@gmail.com"
SMTP_PASSWORD = "zwaz chin czlw rnsd"
EMAIL_TO = "sivareddykasireddy2@gmail.com"

def log_activity(action, extra=""):
    with open(log_file, "a") as log:
        log.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {action} {extra}\n")

def send_email(subject, body, to_email=EMAIL_TO):
    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        log_activity("Email sent", f"to {to_email} | subject: {subject}")
    except Exception as e:
        log_activity("Email failed", str(e))
        print("Failed to send email:", e)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

if not is_admin():
    script_path = os.path.abspath(__file__) if 'file' in globals() else os.path.abspath(sys.argv[0])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script_path}"', None, 1)
    sys.exit()

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

password = generate_password()
log_file = "camera_log.txt"

# Send initial password email and log it
send_email(
    subject="Webcam Security App Started",
    body=f"The application has started.\nInitial password: {password}"
)
log_activity("App started", f"Initial password sent to {EMAIL_TO}")


base64_img = b""

def load_camera_image():
    try:
        image_data = base64.b64decode(base64_img)
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((64, 64), Image.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print("Error loading image:", e)
        return None

def show_info():
    HTML_CONTENT = f"""<!DOCTYPE html>
<html>
<head>
<style>
body {{
  margin: 0;
  padding: 0;
  min-height: 100vh;
  font-family: 'Segoe UI', Arial, sans-serif;
  color: #fff;
  background: linear-gradient(-45deg, #ff6ec4, #7873f5, #42e695, #ffb86c);
  background-size: 400% 400%;
  animation: gradientBG 15s ease infinite;
  position: relative;
  overflow-x: hidden;
}}
@keyframes gradientBG {{
  0% {{background-position: 0% 50%;}}
  50% {{background-position: 100% 50%;}}
  100% {{background-position: 0% 50%;}}
}}
body::before {{
  content: "";
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: url('https://www.transparenttextures.com/patterns/stardust.png');
  opacity: 0.2;
  pointer-events: none;
  z-index: 0;
}}
h1 {{
  background: rgba(0,0,0,0.5);
  color: #fff;
  padding: 20px;
  border-radius: 16px;
  text-align: center;
  box-shadow: 0 4px 24px rgba(0,0,0,0.3);
  margin-top: 30px;
  font-size: 2.2em;
  letter-spacing: 2px;
}}
table {{
  border-collapse: collapse;
  margin: 30px auto;
  width: 90%;
  background: rgba(0,0,0,0.6);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 16px rgba(0,0,0,0.2);
}}
th, td {{
  border: 1px solid #fff2;
  padding: 12px;
  text-align: left;
  font-size: 1.1em;
}}
th {{
  background: linear-gradient(90deg, #ff6ec4, #7873f5);
  color: #fff;
  letter-spacing: 1px;
}}
tr:nth-child(even) {{
  background: #2228;
}}
tr:nth-child(odd) {{
  background: #3338;
}}
p[style] {{
  font-size: 1.2em;
}}
@media (max-width: 700px) {{
  table, th, td {{
    font-size: 0.95em;
  }}
  h1 {{
    font-size: 1.3em;
    padding: 10px;
  }}
}}
</style>
</head>
<body>
<h1>Project Information</h1>
<p> This project was developed by <b> K.SivaReddy,SK.MustakAhmad,K.Naga saiTeja,SK.khayum,SK.rahamathulla,SK.Meeravali</b></p>
<table>
  <tr>
    <th>Project Details</th>
    <th>Value</th>
  </tr>
  <tr>
    <td>Project Name</td>
    <td>webcam malware security</td>
  </tr>
  <tr>
    <td>Project Description</td>
    <td>Implementing Security for the webcams</td>
  </tr>
  <tr>
    <td>Project Start Date</td>
    <td>06-July-2025</td>
  </tr>
  <tr>
    <td>Project End Date</td>
    <td>08-Aug-2025</td>
  </tr>
  <tr>
    <td>Project Status</td>
    <td>Completed</td>
  </tr>
</table>
<h2>Developer Details</h2>
<table>
  <tr>
    <th>Name</th>
    <th>Employee ID</th>
    <th>Email</th>
  </tr>
  <tr>
    <td>SK.MustakAhmad</td>
    <td>ST#IS#7702</td>
    <td>shaikmunna0863@gmail.com</td>
  </tr>
  <tr>
    <td>K.Siva Reddy</td>
    <td>ST#IS#7672</td>
    <td>sivareddykasireddy4452@gmail.com</td>
  </tr>
  <tr>
    <td>K.Naga Sai Teja</td>
    <td>ST#IS#7673</td>
    <td>saiteja.kitchamsetty@gmail.com</td>
  </tr>
  <tr>
    <td>SK.Rahamthulla</td>
    <td>ST#IS#7703</td>
    <td>rahmathullashaik22@gmail.com</td>
  </tr>
  <tr>
    <td>SK.khayum</td>
    <td>ST#IS#7700</td>
    <td>abdulkhayyum2235@gmail.com</td>
  </tr>
  <tr>
    <td>SK.meeravali</td>
    <td>ST#IS#7701</td>
    <td>shaikmeeravali809@gmail.com</td>
  </tr>
</table>
<h2>Company Details</h2>
<table>
  <tr>
  <th>Company</th>
 <th>Value</th>
  </tr>
    <tr>
    <td>Name</td>
    <td>Supraja Technologies</td>
  </tr>
  <tr>
    <td>Email</td>
    <td>contact | @suprajatechnologies.com</td>
  </tr>
</table>
<h2>Initial Password</h2>
<p style="color:red;font-weight:bold;">Initial Password: {password}</p>
</body>
</html>"""
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as f:
        f.write(HTML_CONTENT)
        temp_html_path = f.name
    webbrowser.open(temp_html_path)

try:
    import cv2
except ImportError:
    cv2 = None

def record_intruder_video():
    if cv2 is None:
        log_activity("Intruder video failed", "OpenCV not installed")
        return
    save_path = os.path.join(os.getcwd(), "intruder.mp4")
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(save_path, fourcc, 20.0, (640, 480))
    start_time = time.time()
    duration = 10  # seconds
    while int(time.time() - start_time) < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    log_activity("Intruder video recorded", f"Saved as {save_path}")
    send_mobile_notification(
        "Unauthorized Webcam Access Detected",
        f"An unauthorized user tried to access the webcam. Video saved as {save_path}."
    )

def view_logs():
    def on_ok():
        if password_entry.get() == password:
            password_window.destroy()
            try:
                if os.path.exists(log_file):
                    with open(log_file, 'r') as f:
                        log_content = f.read()
                    log_win = tk.Toplevel(root)
                    log_win.title("Camera Logs")
                    tk.Label(log_win, text="Activity Log", font=("Arial", 12, "bold"), bg="black", fg="white").pack(pady=5)
                    log_text = tk.Text(log_win, wrap="word", bg="black", fg="lime", font=("Consolas", 10))
                    log_text.insert("1.0", log_content)
                    log_text.config(state="disabled")
                    log_text.pack(expand=True, fill="both", padx=10, pady=10)
                else:
                    messagebox.showwarning("Log Missing", "Log file not found")
            except Exception as e:
                messagebox.showerror("Log Error", str(e))
        else:
            log_activity("Incorrect password attempt", f"for log view by user")
            error_label.config(text="Incorrect password")
            password_entry.delete(0, tk.END)
            record_intruder_video()

    password_window = tk.Toplevel(root)
    password_window.title("Enter Password")
    tk.Label(password_window, text="Enter Password:").pack(pady=10)
    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack(pady=5)
    tk.Button(password_window, text="OK", command=on_ok).pack(pady=5)
    error_label = tk.Label(password_window, text="", fg="red")
    error_label.pack()

def check_status():
    if cv2 is None:
        messagebox.showerror("Camera Status", "OpenCV (cv2) is not installed.")
        return
    try:
        cam = cv2.VideoCapture(0)
        if cam and cam.isOpened():
            cam.release()
            messagebox.showinfo("Camera Status", "Webcam is ENABLED.")
            log_activity("Camera status checked", "Webcam is ENABLED")
        else:
            messagebox.showinfo("Camera Status", "Webcam is DISABLED.")
            log_activity("Camera status checked", "Webcam is DISABLED")
    except Exception as e:
        messagebox.showerror("Camera Status", str(e))
        log_activity("Camera status error", str(e))

def change_password():
    def on_ok():
        new_pass = password_entry.get()
        if new_pass:
            global password
            old_password = password
            password = new_pass
            log_activity("Password changed", f"from {old_password} to {password}")
            send_email(
                subject="Webcam Security Password Changed",
                body=f"The password was changed.\nNew password: {password}"
            )
            messagebox.showinfo("Success", "Password changed and sent to your email.")
            pw_window.destroy()
        else:
            error_label.config(text="Password cannot be empty")

    pw_window = tk.Toplevel(root)
    pw_window.title("Change Password")
    tk.Label(pw_window, text="New Password:").pack(pady=10)
    password_entry = tk.Entry(pw_window, show="*")
    password_entry.pack(pady=5)
    tk.Button(pw_window, text="OK", command=on_ok).pack(pady=5)
    error_label = tk.Label(pw_window, text="", fg="red")
    error_label.pack()

def disable_camera():
    try:
        cmd = (
            "powershell -Command "
            "\"$devices = Get-PnpDevice -Class Camera | Where-Object { $_.Status -eq 'OK' }; "
            "foreach ($d in $devices) { Disable-PnpDevice -InstanceId $d.InstanceId -Confirm:$false }\""
        )
        subprocess.run(cmd, shell=True)
        time.sleep(2)
        success_label.config(text="Camera Disabled Successfully")
        status_label.config(text="Camera was disabled")
        log_activity("Camera disabled")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to disable camera: {e}")
        log_activity("Camera disable error", str(e))

def enable_camera():
    try:
        cmd = (
            "powershell -Command "
            "\"$devices = Get-PnpDevice -Class Camera | Where-Object { $_.Status -eq 'Error' -or $_.Status -eq 'Unknown' -or $_.Status -eq 'Disabled' }; "
            "foreach ($d in $devices) { Enable-PnpDevice -InstanceId $d.InstanceId -Confirm:$false }\""
        )
        subprocess.run(cmd, shell=True)
        time.sleep(2)
        success_label.config(text="Camera Enabled Successfully")
        status_label.config(text="Camera was enabled")
        log_activity("Camera enabled")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to enable camera: {e}")
        log_activity("Camera enable error", str(e))

root = tk.Tk()
root.title("Web Cam Security")
root.geometry("400x550")
root.configure(bg="black")

success_label = tk.Label(root, text="", fg="lime", bg="black")
success_label.pack()

tk.Button(root, text="Project Info", bg="red", fg="white", command=show_info).pack(pady=10)
tk.Label(root, text="WebCam Spyware Security", fg="white", bg="black", font=("Arial", 16)).pack(pady=10)

camera_img = load_camera_image()
if camera_img:
    logo_label = tk.Label(root, image=camera_img, bg="black")
    logo_label.image = camera_img
    logo_label.pack(pady=10)
else:
    tk.Label(root, text="[Camera Image Not Found]", bg="black", fg="red").pack()

row = tk.Frame(root, bg="black")
tk.Button(row, text="View Logs", bg="red", fg="white", command=view_logs).pack(side="left", padx=10)
tk.Button(row, text="Check Status", bg="red", fg="white", command=check_status).pack(side="left", padx=10)
row.pack(pady=10)

tk.Button(root, text="Change Password", bg="red", fg="white", width=34, command=change_password).pack(pady=10)

control_frame = tk.Frame(root, bg="gray")
status_label = tk.Label(control_frame, text="", fg="black", bg="white", width=34, height=4, relief="groove")
status_label.pack(pady=10)
tk.Button(control_frame, text="Disable Camera", bg="red", fg="white", command=disable_camera).pack(pady=10)
tk.Button(control_frame, text="Enable Camera", bg="red", fg="white", command=enable_camera).pack(pady=10)
control_frame.pack(pady=20)

root.mainloop()