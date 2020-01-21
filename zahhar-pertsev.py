class Dog():
   age = 0
   name = ""
   weight = 0
   
class Person():
    name = ""
    cellPhone = ""
    email = ""
    
class Bird():
    color=''
    name=''
    breed=''
myBird=Bird()
myBird.color = "green"
myBird.name = "Sunny"
myBird.breed = "Sun Conure"

#4
class Hero():
    name = ''
    power = 0
    x=0
    y=0
myhero=Hero()
myhero.x=1
myhero.y=2
myhero.cords=myhero.x,myhero.y
myhero.name='Karat'
myhero.power=10
    
#5
class Person2():
    name=''
    money=0
nancy=Person2()
nancy.name='Nancy'
nancy.money=100

#6
class Person3():
    name=''
    money=0
pat=Person3()
pat.name = 'Pat'
print(pat.name,'has',pat.money,'dollars.')
    
        
#Второе задание
#1
class Cat():
    name=''
    color=''
    weight='0'
    def meow(self):
        print('Meow')
osel=Cat()
osel.name='osel'
osel.color='red'
osel.weight=47
osel.meow()

#2
#-----
#3
class Monster():
    name=''
    health=0
    def decreaseHealth(self,amount):
        while True:
            self.health-=amount
            if self.health<=0:
                print('Монстр погиб')
                break
            else:
                print('У монстра',self.health,'здоровья.')
                
monster=Monster()
monster.name='Roba'
monster.health=100
monster.decreaseHealth(10)
    
#Практическая работа (класс "Воин")
import random
class warrior():
    health=100
    
    def fight(self,first,second):
        self.first=first
        self.second=second
        while first.health>0 and second.health>0:
            fighter=random.randint(1,2)
            if fighter==1:
                second.health-=20
                print('Володя бьет с вертушки в голову Башке')
                print('Володя','=',first.health,'HP')
                print('Башка','=',second.health,'HP')
                if second.health==0:
                    print('Володя выйграл!')
                
            elif fighter==2:
                first.health-=20
                print('Башка прямым ударом в нос бьет Володе')
                print('Володя','=',first.health,'HP')
                print('Башка','=',second.health,'HP')
                if first.health==0:
                    print('Башка выйграл!')
                
volodya=warrior()

bashka=warrior()

start=warrior()
start.fight(volodya,bashka)

    
    
                
    


