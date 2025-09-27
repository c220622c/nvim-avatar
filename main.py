import subprocess
#-----#-----#-----#-----#-----CONFIG------#-----#-----#-----#-----#-----#-----
image_path = "/Users/wzj/Downloads/IDEA.png"
cmd = f"ascii-image-converter {image_path} -b -H 20 -n > avatar.txt"
#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----
def process_ascii_art_from_file(filename):
    # 读取文件
    with open(filename, 'r', encoding='utf-8',errors='ignore') as file:
        lines = file.readlines()
    # 去除空行和首尾空白，但保留行内的空格
    # 直接移除所有⠀字符后检查是否为空
    lines = [line.rstrip() for line in lines if line.replace('⠀', '').strip()]
    lines = [line.rstrip() for line in lines if line.rstrip()]

    # 找到最长的非空行长度
    max_length = max(len(line) for line in lines)

    # 处理每一行
    processed_lines = []
    for line in lines:
        # 计算居中所需的左边空格数
        padding = (max_length - len(line)) // 2
        centered_line = ' ' * padding + line

        # 添加[[和]]
        processed_line = f"[[{centered_line}]],"
        processed_lines.append(processed_line)

    return '\n'.join(processed_lines)

# 使用示例
if __name__ == "__main__":
    result1 = subprocess.run(cmd, shell=True,timeout=30)
    print(result1)
    print(f"执行完成，退出码: {result1.returncode}")
    # 从文件读取并处理
    result2 = process_ascii_art_from_file("avatar.txt")

    # 输出结果
    print(result2)