import sys
sys.path.insert(0, '.')

from my_add import add

# 测试用例
assert add(2, 3) == 5, "测试1失败"
assert add(-1, 1) == 0, "测试2失败"
assert add(0, 0) == 0, "测试3失败"
assert add(10, -5) == 5, "测试4失败"

print("所有测试通过！")
