Python3 错误和异常

#Python 的语法错误或者称之为解析错，是初学者经常碰到的，如下实例
# while True print('Hello world')
#   File "<stdin>", line 1, in ?
#     while True print('Hello world')

# SyntaxError: invalid syntax
# 这个例子中，函数 print() 被检查到有错误，是它前面缺少了一个冒号（:）。
# 语法分析器指出了出错的一行，并且在最先找到的错误的位置标记了一个小小的箭头。


#即便Python程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。
#大多数的异常都不会被程序处理，都以错误信息的形式展现在这里:
# 10 * (1/0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# ZeroDivisionError: division by zero
# 4 + spam*3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# NameError: name 'spam' is not defined
# '2' + 2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# TypeError: Can't convert 'int' object to str implicitly