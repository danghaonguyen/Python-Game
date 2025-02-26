import cv2
import numpy as np

# Đọc ảnh
image_path = "C:\Users\HAO NGUYEN\Downloads\Wallpaper\1371922.png"
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

# Chuyển ảnh sang grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Tạo mặt nạ (mask) bằng cách tìm các vùng có màu đỏ
lower_red = np.array([0, 0, 100], dtype=np.uint8)   # Ngưỡng đỏ thấp
upper_red = np.array([100, 100, 255], dtype=np.uint8)  # Ngưỡng đỏ cao
mask = cv2.inRange(image, lower_red, upper_red)

# Tăng độ mờ vùng mặt nạ để loại bỏ dấu hiệu gắt
mask = cv2.GaussianBlur(mask, (5, 5), 0)

# Xoá con dấu bằng inpainting (lấp đầy vùng đã xoá)
result = cv2.inpaint(image, mask, inpaintRadius=5, flags=cv2.INPAINT_TELEA)

# Lưu ảnh kết quả
output_path = "/mnt/data/image_no_stamp.png"
cv2.imwrite(output_path, result)

print(f"Ảnh đã được xử lý và lưu tại: {output_path}")
