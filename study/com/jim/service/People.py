class People:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

# p = People('runoob',10,30)
# p.speak()
# print(p.weight)
