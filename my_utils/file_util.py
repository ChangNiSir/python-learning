"""
文件处理相关的工具模块
"""


def print_file_info(file_name):
    """
    功能是给定路径的文件内容输出到控制台中
    :param file_name: 即将被读取文件的文件路径
    :return: None
    """
    f = None  # 定义f（open失败finally要运行f需要事先定义）
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print(f"读取成功：\n{content}")
    except Exception as e:
        print(f"异常为：{e}")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    """
    功能是将指定数据追加到指定文件中
    :param file_name: 指定文件的文件路径
    :param data: 指定的数据
    :return: None
    """
    with open(file_name, "a", encoding="UTF-8") as f:
        f.write(data)


if __name__ == '__main__':
    # print_file_info("D:/word.txt")
    append_to_file("D:/word.txt", "\nlike you apple and banana")
    print_file_info("D:/word.txt")