
"""
def find_max(li):
    if len(li)==0:
       return None
    max_item=li[0]
    for item in li:
        if item>max_item:
           max_item=item
    return max_item

maximum=[10,20,50,60]

print(find_max(maximum))

"""

"""

list=[1,2,3,4,5,6,7]
print(1 in list)

"""

"""
def find_item(li,x):
    for item in li:
        if item==x:
            return True
    return False

num=[1,2,3,4,5,6,7]
print(find_item(num,4)) 

"""

"""
def my_func(a,b,c): #POSITIONAL ARGUMENT
    result= a*3 + b*2 +c

    return result

a,b,c = 30,10,20
r= my_func(a,b,c)
print(r)

"""

"""
def my_func(b,a,c): #Keyword argument
    result= a*3 + b*2 +c

    return result


r= my_func(a=10,b=20,c=30)
print(r)

"""

"""
def my_func(b,a,c=0): # Default argument
    result= a*3 + b*2 +c

    return result


r= my_func(a=10,b=20)
print(r)

"""
def fnc(n1,n2):
    print("Received",n1,n2)

    def is_even(n):
        if n % 2 ==0:
           return True
        else:
            return False
    print(n1,is_even(n1))
    print(n2,is_even(n2))

fnc(10,11)        
