#定义地瓜类
class SweetPotato:
    #定义初始化方法
    def __init__(self):
        self.cookedLevel=0
        self.cookedString="生的"
        self.condiments=[]
    def __str__(self):
        msg = "您的地瓜已经处于 " + self.cookedString + "的状态"
        # if len(self.condiments)>0:
        #     msg = msg + " ,添加的佐料为:"
        #     for temp in self.condiments:
        #         msg = msg + temp + ", "
        #     msg = msg.strip(", ")
        # return msg        
        # msg=self.cookedString+" 地瓜"
        if len(self.condiments)>0:
            msg = msg + " ,添加的佐料为:"
            for temp in self.condiments:
                msg = msg + temp + ", "
            msg = msg.strip(", ")
            msg=msg+")"
        return msg
        # return "现在地瓜状态是%s，加的作料有%s"%(self.cookedString,self.condiments)
    #烤地瓜方法
    def cook(self,time):
        self.cookedLevel+=time
        if self.cookedLevel>8:
            self.cookString="烤成灰了"
        elif self.cookedLevel>5:
            self.cookString="烤好了"
        elif self.cookedLevel>3:
            self.cookString="半生不熟"
        else:
            self.cookString="生的"
    #添加配料
    def addCondiments(self,condiments):
        self.condiments.append(condiments)
mySweetPotato=SweetPotato()
# mySweetPotato.cook(4)
# print(mySweetPotato.cookedLevel)
# print(mySweetPotato.cookString)
# print(mySweetPotato.coodiments)
print("------有了一个地瓜，还没有烤------")
print(mySweetPotato.cookedLevel)
print(mySweetPotato.cookedString)
print(mySweetPotato.condiments)
print("------接下来要进行烤地瓜了------")
print("------地瓜已经烤了4分钟了------")
mySweetPotato.cook(4)#靠4分钟
print(mySweetPotato)
print("------地瓜已经烤了3分钟了------")
mySweetPotato.cook(3)#靠3分钟
print(mySweetPotato)
print("------接下来要添加配料-番茄酱------")
mySweetPotato.addCondiments("番茄酱")
print(mySweetPotato)
print("------地瓜已经烤了5分钟了------")
mySweetPotato.cook(5)#又烤了5分钟
print(mySweetPotato)
print("------接下来要添加配料-芥末酱------")
mySweetPotato.addCondiments('芥末酱')
print(mySweetPotato)

