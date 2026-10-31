# 1. Di chuyển vào thư mục dự án
import os
project_dir = "/content/drive/MyDrive/NCKH-TSF/iTransformer-main/iTransformer-main"
os.chdir(project_dir)

# 2. Tải tập dữ liệu Weather nếu chưa có
import urllib.request
dataset_dir = "./dataset/weather"
os.makedirs(dataset_dir, exist_ok=True)
data_path = os.path.join(dataset_dir, "weather.csv")

if not os.path.exists(data_path):
    print("Đang tải tập dữ liệu Weather...")
    try:
        urllib.request.urlretrieve("https://raw.githubusercontent.com/thuml/Time-Series-Library/main/dataset/weather/weather.csv", data_path)
        print("Tải thành công tập dữ liệu Weather!")
    except Exception as e:
        print(f"Lỗi khi tải từ nguồn chính, thử nguồn phụ: {e}")
        # Sử dụng link github của Autoformer chính thức
        urllib.request.urlretrieve("https://raw.githubusercontent.com/thuml/Autoformer/main/dataset/weather/weather.csv", data_path)
        print("Tải thành công tập dữ liệu Weather từ nguồn phụ!")
else:
    print("Tập dữ liệu Weather đã tồn tại sẵn.")

# 3. Sửa lỗi tương thích NumPy 2.0 trong utils/tools.py
tools_path = "utils/tools.py"
if os.path.exists(tools_path):
    with open(tools_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Thay thế np.Inf thành np.inf
    if "np.Inf" in content:
        print("Phát hiện np.Inf trong utils/tools.py. Tiến hành thay thế bằng np.inf để tương thích NumPy 2.0...")
        content = content.replace("np.Inf", "np.inf")
        with open(tools_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Đã sửa lỗi tương thích thành công!")

# 4. Chạy thực nghiệm với bộ dữ liệu Weather
print("\nBắt đầu chạy thực nghiệm bộ dữ liệu Weather...")
!bash scripts/multivariate_forecasting/Weather/iTransformer.sh

project_dir = "/content/drive/MyDrive/NCKH-TSF/iTransformer-main/iTransformer-main"
os.chdir(project_dir)

print("=== 1. KIỂM TRA THƯ MỤC CHECKPOINTS (LƯU TRỮ MODEL) ===")
checkpoints_path = "./checkpoints"
if os.path.exists(checkpoints_path):
    models = os.listdir(checkpoints_path)
    print(f"Tìm thấy {len(models)} mô hình đã lưu:")
    for m in models:
        print(f" - {m}")
else:
    print("Chưa tạo thư mục checkpoints hoặc chưa lưu được model.")

print("\n=== 2. KIỂM TRA THƯ MỤC RESULTS (LƯU TRỮ KẾT QUẢ ĐÁNH GIÁ) ===")
results_path = "./results"
if os.path.exists(results_path):
    results = os.listdir(results_path)
    print(f"Tìm thấy {len(results)} thư mục kết quả:")
    for r in results:
        r_full_path = os.path.join(results_path, r)
        print(f"\nThư mục: {r}")
        if os.path.isdir(r_full_path):
            files = os.listdir(r_full_path)
            print(f"  Có các files: {files}")
            # Nếu có lưu file kết quả metrics
            if "metrics.npy" in files:
                metrics = np.load(os.path.join(r_full_path, "metrics.npy"))
                # Thông thường cấu trúc lưu trữ: [mae, mse, rmse, mape, mspe]
                print(f"  Chỉ số đánh giá từ metrics.npy: ")
                print(f"    - MAE: {metrics[0]:.4f}")
                print(f"    - MSE: {metrics[1]:.4f}")
else:
    print("Chưa tìm thấy thư mục 'results'. Hãy đợi thực nghiệm chạy xong hoàn toàn hoặc kiểm tra cấu hình lưu của file script.")