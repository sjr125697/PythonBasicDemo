sr="生人"
jr="家人"
class Dog:
    def __init__(self,newcolor,newname):
        self.color=newcolor
        self.name=newname
    def __str__(self):
        # print("一只%s的狗狗叫%s"%(self.color,self.name))
        return "一只%s的狗狗叫%s"%(self.color,self.name)
    def act(self,judge):
        if self.name=="大黄":
            if judge=="生人":
                print("------它看见了%s------"%(sr))
                print("汪汪...")
            else:
                print("------它看见了%s------"%(jr))
                print("摇尾巴...")
        else:
            if judge=="生人":
                print("------它看见了%s------"%(sr))
                print("喵喵...")
            else:
                print("------它看见了%s------"%(jr))
                print("摇尾巴...")

dahuang=Dog("黄颜色","大黄")
xiaobai=Dog("白颜色","小白")
print(dahuang)
dahuang.act(sr)
dahuang.act(jr)
print(xiaobai)
xiaobai.act(sr)
xiaobai.act(jr)






            
        
        
