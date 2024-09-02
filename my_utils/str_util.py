"""
字符串相关的工具模块
"""


def str_reverse(s):
    """
    功能是将字符串完成反转
    :param s: 将被反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]  # 字符串切片反转


def substr(s, x, y):
    """
    功能是按照给定的下标完成给定字符串的切片
    :param s: 即将被切片的字符串
    :param x: 切片的开始位置（序号）
    :param y: 切片的结束位置（序号）
    :return: 切片完成后的字符串
    """
    return s[x-1:y]


if __name__ == '__main__':
    s = "123456"
    print(str_reverse(s))
    print(substr(s, 1, 3))
