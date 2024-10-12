import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

folderPath = r'F:\commonProgram\test\3Dcoordinate'
new_csv_file = f'3dCoordinate22.csv'
new_file_path = os.path.join(folderPath, new_csv_file)

# 读取CSV文件
points = []
with open(new_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        point = [float(row[0]), float(row[1]), float(row[2])]
        points.append(point)

# 提取 x、y、z 坐标
x = [point[0] for point in points]
y = [point[1] for point in points]
z = [point[2] for point in points]

# 创建一个3D图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图
ax.scatter(x, y, z, c='r', marker='o')

# 设置坐标轴标签
ax.set_xlabel('X Label(mm)', fontsize=25, labelpad=20)
ax.set_ylabel('Y Label(mm)', fontsize=25, labelpad=20)
ax.set_zlabel('Z Label(mm)', fontsize=25, labelpad=20)

# 设置坐标轴刻度标签字体大小  
for axis in ['x', 'y', 'z']:  
    ax.tick_params(axis=axis, labelsize=25)  # 刻度标签字体大小设置为12  

# 显示图形
plt.show()