import os

# 指定源文件夹和目标文件名
label_folder = "D:/gaze_estimate/dataset/FaceBased/MPIIFaceGaze/Label"
train_label_path = "D:/gaze_estimate/dataset/FaceBased/MPIIFaceGaze/Label/train.label"
test_label_path = "D:/gaze_estimate/dataset/FaceBased/MPIIFaceGaze/Label/test.label"

# 合并 p00.label 到 p10.label 为 ritrain.label
ritrain_labels = []
for i in range(11):  # p00.label 到 p10.label
    label_file = os.path.join(label_folder, f"p{str(i).zfill(2)}.label")
    with open(label_file, 'r') as file:
        lines = file.readlines()
        ritrain_labels.extend(lines)

# 合并 p11.label 到 p14.label 为 test.label
test_labels = []
for i in range(11, 15):  # p11.label 到 p14.label
    label_file = os.path.join(label_folder, f"p{str(i).zfill(2)}.label")
    with open(label_file, 'r') as file:
        lines = file.readlines()
        test_labels.extend(lines)

# 写入 ritrain.label 文件
with open(train_label_path, 'w') as file:
    file.writelines(ritrain_labels)

# 写入 test.label 文件
with open(test_label_path, 'w') as file:
    file.writelines(test_labels)

print(f"train.label 和 test.label 已成功创建！")
