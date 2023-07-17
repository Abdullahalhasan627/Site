from PIL import Image
import tkinter as tk
from tkinter import filedialog

def convert_jpeg_to_png(input_path, output_path):
    image = Image.open(input_path)
    image.save(output_path, "PNG")

# إنشاء نافذة Tkinter وإخفاءها
root = tk.Tk()
root.withdraw()

# اختيار مسار الصورة الأصلية من المستخدم
input_path = filedialog.askopenfilename(title="اختر صورة JPEG", filetypes=(("JPEG files", "*.jpg"), ("JPEG files", "*.jpeg")))

# التحقق من امتداد الصورة الأصلية
if not input_path.lower().endswith((".jpg", ".jpeg")):
    print("الصورة الأصلية يجب أن تكون بتنسيق JPEG!")
    exit()

# اختيار مسار حفظ الصورة المحولة من المستخدم
output_path = filedialog.asksaveasfilename(title="اختر مسار حفظ الصورة المحولة", defaultextension=".png", filetypes=(("PNG files", "*.png"),))

# التحويل وحفظ الصورة
convert_jpeg_to_png(input_path, output_path)

print("تم تحويل الصورة بنجاح!")
