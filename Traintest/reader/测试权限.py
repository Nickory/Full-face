import os

# 文件夹路径
folder_path = r"D:\gaze_estimate\dataset\FaceBased\MPIIFaceGaze\Label"

# 遍历文件夹中的文件
try:
    # 获取文件夹内的所有文件
    files = os.listdir(folder_path)

    # 只选择label文件（假设后缀为 .label）
    label_files = [f for f in files if f.endswith('.label')]

    # 遍历所有 label 文件并读取内容
    for label_file in label_files:
        file_path = os.path.join(folder_path, label_file)

        with open(file_path, 'r') as file:
            content = file.read()
            print(f"文件 {label_file} 内容读取成功：")
            print(content)
except FileNotFoundError:
    print(f"文件夹 {folder_path} 未找到。")
except IOError as e:
    print(f"读取文件时发生错误：{e}")
