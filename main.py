# copy move files
import os
import time
import uuid
import glob
import shutil

# 原始路径
original_path = "D:\\Temp\\"

# 目标路径
target_path = "D:\\Temp1\\"

# 文件类型
file_type = '*.png'

# 遍历原始路径下的目录以及所有的文件
for resources in os.listdir(r'%s' % original_path):
    if os.path.isdir(original_path + resources):  # 判断是否是目录
        for files in glob.glob(r'%s\\%s' % (original_path + resources + "\\", file_type)):
            shutil.copy(files, target_path)  # 复制原始路径中的文件到目标路径中
    else:
        for files in glob.glob(r'%s\\%s' % (original_path, file_type)):
            shutil.copy(files, target_path)  # 复制原始路径中的文件到目标路径中
    time.sleep(0.5)
