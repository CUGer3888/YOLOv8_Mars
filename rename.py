import os  # 导入Python的os模块，提供了许多与操作系统交互的功能

# 定义一个变量path，指向当前目录下的"labels"文件夹
path = "labels"

# 使用os.listdir函数获取path目录下的所有文件和子文件夹的名称，并将结果存储在变量files中
files = os.listdir(path)

# 对files列表进行排序，以便按照某种顺序（通常是字母顺序）排列文件名
files.sort()

# 开始一个循环，遍历排序后的文件列表
for i, file in enumerate(files):
    # 使用enumerate函数获取当前文件在列表中的索引（i）和文件名（file）
    # os.path.join函数用于拼接路径和文件名，确保在不同操作系统下路径的正确性
    # os.rename函数用于重命名文件，第一个参数是旧的文件名路径，第二个参数是新的文件名路径
    # 新的文件名是由当前索引加1（从1开始编号），然后使用字符串的zfill方法填充到三位数（例如：001, 002, ..., 100），加上".txt"扩展名
    os.rename(
        os.path.join(path, file), os.path.join(path, str(i + 1).zfill(3) + ".txt")
    )

# 打印"done"，表示文件重命名操作完成
print("done")
