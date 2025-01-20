
"""
#what is object

class add:
    x=20
    y=30

    def addtwo(self):
        z=self.x+self.y
        print(z)

object=add()
object.addtwo() #to help print z,to print the value of z

print(object.x)
print(object.y)

"""

"""

#what is static...... access class properties without object 

class add:
    x=10
    y=20
    
    @staticmethod
    def addtwo():
        z=add.x+add.y
        print(z)

add.addtwo()

"""

"""
# what is constructior(auto exicuted method)...(__init__)

class add:
    x=10
    y=20
    
    def __init__(self):
        z=self.x-self.y
        print(z)

add()        

"""

"""
#...................................

#inheritance


class Father:

    x=10
    y=30

    def __init__(self):
        z=self.x-self.y
        print(z)

    def addTwo(self):
        z=self.x+self.y
        print(z)    
     
    @staticmethod 
    def mulTwo():    
        z=Father.x*Father.y
        print(z)

class son(Father):
    pass


son()
object=son()
object.addTwo()
object.mulTwo()

"""

"""

class Father:

    x=10
    y=30

    def __init__(self):
        z=self.x-self.y
        print(z)

    def addTwo(self):
        z=self.x+self.y
        print(z)    
     
    @staticmethod 
    def mulTwo():    
        z=Father.x*Father.y
        print(z)

class son(Father):
    pass


Father()
object=Father()
object.addTwo()
object.mulTwo()

"""


"""
#Overriding


class Father:

    x=10
    y=30

    def __init__(self):
        z=self.x-self.y
        print(z)

    def addTwo(self):
        z=self.x+self.y
        print(z)    
     
    @staticmethod 
    def mulTwo():    
        z=Father.x*Father.y
        print(z)

class son(Father):

     x=10
     y=10
     def addTwo(self):
        z=self.x+self.y
        print(z) 


object=son()
object.addTwo()

"""

"""
#Abstraction

from abc import ABC,abstractmethod
class Father(ABC):

    x=10
    y=30
    
    @abstractmethod
    def addTwo(self):
        pass

     #we can also use like this

   # @abstractmethod
    #def addTwo(self):
        #z=self.x+self.y
        #print(z) 
          
     
class son(Father):
      x=10
      y=30

      def addTwo(self):
         z=self.x+self.y
         print(z)   
               
     
               
object=son()
object.addTwo()

"""
"""
#Multiple inheritance

class Father:

    def add(self,num1,num2):
        print(num1+num2)

class Mother:

    def mul(self,num1,num2):
        print(num1*num2)

class son(Father,Mother):
      pass

obj=son()
obj.add(3,4)
obj.mul(3,2)            

"""

"""
#multilable inheritance

class GrandFather:

    x=10
    y=30

   
    def addTwo(self):
        z=self.x+self.y
        print(z)    
     
class Father(GrandFather):
      pass

class son(Father):
      pass


class Grandson(son): 
      pass

object=Grandson()
object.addTwo()

"""

"""
#private access modifier

class GrandFather:

    __x=10
    __y=30

   
    def addTwo(self):
        z=self.__x+self.__y
        print(z)    

obj=GrandFather()
#print(obj.__x)
obj.addTwo()     

"""

"""
#.....................................
#Method overloading

# 1.Default AArguments

class Father:
    def Numadd(self,a,b,c=0):
        print(a+b+c)



object=Father()
object.Numadd(2,3,4)
object.Numadd(2,2)

"""
"""

#Variable length Argument

class Father:
    def Numadd(self,*argument):
        print(*argument)



object=Father()

object.Numadd(2,3,4)
object.Numadd(2,2)

"""