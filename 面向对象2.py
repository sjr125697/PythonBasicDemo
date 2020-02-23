# 创建类
class Dog:
    # 定义一个方法
    def __init__(self,newname,newweight,newcolor):#魔法方法，使对象拥有默认属性，自动调用，初始化,self相当于选择器id定位对象
        self.weight=newweight
        self.color=newcolor
        self.name=newname
    def __str__(self):#魔法方法，当你打印self所指代的对象名时，会返回return后的的东西
        return "hahahaha,你是小狗！！！"
    # 创建方法，即函数，对象的属性
    def brak(self):
        print("汪汪汪.....")
    def run(self):
        print("狗在疯狂的跑....")
    def eat(self):
        print("吃东西.....")
        # 在方法中可以对属性进行修改
        self.weight+=5
    def printname(self):
        print("名字是%s"%self.name)
def test(name):
    name.printname()
# 创建对象，并将对象归于Dog这个类
xiaogou=Dog("小黄",5,"黄色")
wangcai=Dog("小白",10,"白色")
test(xiaogou)#用调用函数的方法，去调用类的方法
test(wangcai)#用调用函数的方法，去调用类的方法
print("-"*30)
print(xiaogou)
print("-"*30)
# 调用对象所在类的属性
xiaogou.brak()
xiaogou.run()
wangcai.brak()
wangcai.run()
# 添加属性
# xiaogou.weight=5
# xiaogou.color="黄颜色"
# 使用添加的属性
print(xiaogou.weight)
print(xiaogou.color)
print(wangcai.weight)
print(wangcai.color)
# 调用吃方法，这方法中，会对weight这属性进行修改
xiaogou.eat()
print(xiaogou.weight)
wangcai.eat()
print(wangcai.weight)
# 验证，是否直接直接修改属性
xiaogou.weight+=5
print(xiaogou.weight)
wangcai.weight+=5
print(wangcai.weight)
# 打印狗的名字
xiaogou.printname()
wangcai.printname()