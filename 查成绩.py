
list = []
while 1:
    s = input()
    if s:
      s = s.split(":")
      list.append(s)
    else:
        break
flag = 0
s = input("请输入要查询的课程：\n")
for i in list:
    if i[0]==s:
        print(i[1])
        flag=1
        break
if flag==0:
    print("没有该门课程")

