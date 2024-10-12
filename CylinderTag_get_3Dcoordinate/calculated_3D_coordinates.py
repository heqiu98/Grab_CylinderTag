import csv  
import os  
import numpy as np
import math  


def main():
    # 设置Tag的像素尺寸大小和物理尺寸大小
    pixelLenght = 1950
    pixelHeight = 1300 
    physicalLenght = 175 #单位mm
    physicalHeight = 116.6 #单位mm
      
    # 假设的文件夹路径  
    pixelCoordinateFolderPath = r'F:\commonProgram\test\Pixel_coordinate'  # 替换为你的文件夹路径
    
    # 计算出的三维坐标后的文件夹路径
    coordinate3DFolderPath = r'F:\commonProgram\test\3Dcoordinate' # 替换为你的文件夹路径
     
  
    # 获取文件夹中所有的CSV文件名  
    csv_files = [f for f in os.listdir(pixelCoordinateFolderPath) if f.startswith('Pixel_coordinate') and f.endswith('.csv')]  
  
    # 对每个CSV文件进行处理  
    for csv_file in csv_files:  
        # 读取CSV文件  
        file_path = os.path.join(pixelCoordinateFolderPath, csv_file)  
        with open(file_path, mode='r', newline='') as csvfile:  
            csvreader = csv.reader(csvfile)   
          
            # 初始化三维坐标列表  
            three_d_coords = []  
          
            # 对每个二维点进行处理计算，得到三维坐标  
            for row in csvreader:  
                x = float(row[0])  # 假设第一列是x坐标  
                y = float(row[1])  # 假设第二列是y坐标
                
                xPhysical = x * (physicalLenght / pixelLenght) # 计算出x的物理坐标
                yPhysical = (1300 - y) * (physicalHeight / pixelHeight) # 计算出y的物理坐标 

                r = physicalLenght / (2 * math.pi) # 圆柱半径
                
                x3d = r * math.cos (2 * math.pi * (xPhysical / physicalLenght))
                y3d = r * math.sin (2 * math.pi * (xPhysical / physicalLenght))
                z3d = yPhysical
              
                # 将三维坐标添加到列表中  
                three_d_coords.append([x3d, y3d, z3d])  
      
        #构建新的文件名  
        new_csv_file = f'3dCoordinate{csv_file.split("Pixel_coordinate")[1]}'  
        new_file_path = os.path.join(coordinate3DFolderPath, new_csv_file)  
      
        # 将三维坐标写入新的CSV文件  
        with open(new_file_path, mode='w', newline='') as new_csvfile:  
            csvwriter = csv.writer(new_csvfile)  
          
            # 写入表头  
            csvwriter.writerow(['x', 'y', 'z'])  
          
            # 写入三维坐标  
            for coord in three_d_coords:  
                csvwriter.writerow(coord)  
      
        print(f"处理完成: {csv_file} -> {new_csv_file}")
    
if __name__ == "__main__":
    main()