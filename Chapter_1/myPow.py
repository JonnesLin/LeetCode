"""
心路历程：
    1. 尝试了一手暴力求解，但是爆内存了qaq
    2. 使用二分法进行求解，完美完成～

总结：
    1. 使用递归的时候需要依靠函数的意义进行操作，以这道题为例：
        将mul(n)函数理解为为计算前n个数相乘的结果，这样做起来就很轻松了
    2. 多尝试正向考虑再考虑逆向考虑～
"""


def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    def mul(n):
        if n == 0:
            return 1.0

        result = mul(n//2)
        if n % 2 == 0:
            return result * result
        else:
            return result * result * x
    if n > 0:
        return mul(n)
    else:
        return 1.0/mul(-n)
    return mul(n)
