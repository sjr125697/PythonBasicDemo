dict1 = {}
while True:
    inp = input()

    if not inp:
        break

    key, value = inp.split(':')
    dict1[key] = value

while True:
    print(dict1.get(input('请输入要查询的课程：'),'没有该门课程'))