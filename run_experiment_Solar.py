import os
import shutil

# 1. Di chuyển vào thư mục dự án
project_dir = "/content/drive/MyDrive/NCKH-TSF/iTransformer-main/iTransformer-main"
os.chdir(project_dir)

# 2. Cài đặt các thư viện phụ thuộc bắt buộc để tránh lỗi ModuleNotFoundError
print("Đang kiểm tra và cài đặt các thư viện yêu cầu...")
!pip install -r requirements.txt
!pip install reformer-pytorch

solar_dir = "./dataset/Solar"
txt_file = os.path.join(solar_dir, "solar_AL.txt")
csv_file = os.path.join(solar_dir, "solar_AL.csv")

# 3. Tạo file .csv bằng cách sao chép từ .txt nếu script yêu cầu đuôi .csv
if os.path.exists(txt_file) and not os.path.exists(csv_file):
    print("\nĐang đồng bộ tạo tệp tin solar_AL.csv từ solar_AL.txt...")
    shutil.copy(txt_file, csv_file)
    print("Đã tạo file solar_AL.csv thành công!")
elif os.path.exists(csv_file):
    print("\nCả hai phiên bản .txt và .csv đều đã sẵn sàng.")

# 4. Chạy thực nghiệm bộ dữ liệu Solar Energy
print("\nBắt đầu chạy huấn luyện mô hình iTransformer với bộ dữ liệu Solar Energy...")
!bash scripts/multivariate_forecasting/SolarEnergy/iTransformer.sh