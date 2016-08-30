# _*_coding:utf-8_*_
# homework
import time

class peopel(object):
    """docstring for peopel"""

    def __init__(self, money):
        self.money = money

    def allmoeny(self):
        return self.money

    def panduan(self):
        if self.money > 50000:
            return "是一个高富帅"
        else:
            return "是一个穷屌丝"


class gaohushuai(peopel):
    """docstring for gaohushuai"""

    def __init__(self, money):
        super(gaohushuai, self).__init__()
        self.money = money


class qiongdiaosi(peopel):
    """docstring for qiongdiaosi"""

    def __init__(self, money):
        super(qiongdiaosi, self).__init__()
        self.money = money

def characternamestatus():
    print("you all have %s yuan") %charactername.allmoeny()
    print("you is %s")  %charactername.panduan()

charactername = raw_input("请输入角色名：  ")
charactermoney = input("请输入初始金币：  ")


for x in range(3):
    print 3-x
    time.sleep(1)
print
print
print("*******************************************游戏开始**********************************************************")
charactername = peopel(charactermoney)
characternamestatus()
ability = 0

print "now!you have 100 days"

for x in range(100):
	print "第%s天" %x
	print "what want you to do ?"	
	print "                  a：打工"
	print "                  b：逛街"
	print "                  c：玩游戏"
	print "                  d：学习"
	choice = raw_input("请选择：  ")
	if choice == "a" :
	    bility = ability + 1