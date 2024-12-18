# word=input("enter your number:")
# rev=""
# index=0
# while index<len(word):
#     words=word[index]
#     rev=words+rev
#     index+=1
# if word==rev:
#     print("palin")
# else:
#     print("not palin")


# words=input()
# alpha=""
# numeric=""
# sc=""
# index=0
# while index<len(words):
#     first=words[index]
#     index+=1
# if first.isalpha():
#     alpha+=first
#     print("alpha")
# elif first.isnumeric():
#     numeric+=first
#     print("numeric")
# else:
#     sc+=first
#     print("sc")



# items=[(10,20),71,True,['a','s'],'apple']
# index=0
# while index<len(items):
#     item=items[index]
#     index+=1
#     if type(item) in(str,tuple):
#         print("imutable")
#     else:
#         print("mutable")

# wors="if your bsd i sm your dad"
# index=0
# output=""
# while index<len(wors):
#     char=wors[index]
#     index+=1
#     if char==output:
#         output+=char
#     else:
#         output=char+"_"
# print(output)


# string="if your bsd i sm your dad"
# result=string.replace("","_")
# print(result)


# num1=int(input())
# num2=int(input())
# num3=int(input())
# num4=int(input())
# if num1>num2:
#     if num1>num3:
#         if num1>num4:
#             if num2>num3:
#                 print("num2 is 2nd")
#             else:
#                 if num3>num4:
#                     print("num3 is 2nd")
#                 else:
#                     print("num4 is 2nd")
#         else:
#             print("num1 is 2nd")
#     else:
#         print("num1 is 2nd")
# else:
#     if num2>num3:
#         if num2>num4:
#             print("num2 is 2nd")
#         else:
#             if num1>num3:
#                 print("num1 is 2nd")
#             else:
#                 if num3>num4:
#                     print("num3 is 2nd")
#                 else:
#                     print("num4 is 2nd")
#     else:
#         print("num2 is 2nd")

# num=int(input())
# for i in range(0,num,2):
#     print(i)


# multi=int(input())
# for num in range(1,20):
#     result=multi*num
#     print(result)

# for num in range(99,0,-2):
#     print(num)

# num=int(input())
# factorial=1
# for factor in range(1,num+1):
#     factorial*=factor
#     print(factorial)

# collection=[11,12.3,'hello',2+3j]
# for num in collection:
#     if type(num) in [int,float,complex]:
#         print(num)

# string=input()
# for word in string:
#     if word.islower():
#         print(word)

# sentance=input()
# word=sentance.split()
# output={}
# for words in word:
#     output[words]=len(words)
# print(output)


# num=[23,45,67,45]
# max=0
# for nums in num:
#     if nums > max:
#         max=nums
# print(max)


# collection=input()
# count=0
# for coll in collection:
#     count+=1
# print(count)

# dict={"a":10,"b":39,"c":20}
# output={}
# for key in dict:
#     value=dict[key]
#     if type(value) not in [dict,set,list]:
#         output[value]=key
# print(output)

# man={10,23.3,2+3j,"hello",(10,12)}
# output={}
# for item in output:
#     if type(item) in (str,tuple,list,set,dict):
#         man.difference_update(item)
# print(man)


# word=input()
# output=[]
# rev=""
# index=0
# while index<len(word):
#     rev=word[index]+rev
#     index+=1
# if rev==word:
#     output=output.append(rev)
#     print(output)

# string=input()
# output=""
# index=0
# while index<len(string):
#     char=string[index]
#     index+=1
#     if char.isupper():
#         output+=char.lower()
#     elif char.islower():
#         output+=char.upper()
#     else:
#         output+=char
# print(output)

# word=input()
# output={}
# index=0
# while index<len(word):
#     words=word[index]
#     index+=1
#     if words not in output:
#         output[words]=ord(words)
# print(output)


# word=input()
# output={}
# man=word.split()
# index=0
# while index<len(man):
#     words=man[index]
#     index+=1
#     if words not in output:
#         output[words]=len(words)
# print(output)

        

# word=input()
# output={}
# index=0
# while index<len(word):
#     words=word[index]
#     index+=1
#     if words in output:
#         output[words]+=1
#     else:
#         output[words]=1
# print(output)

# files=['start.py','demo.txt','new.py','byr.txt','some.csv']
# output={}
# index=0
# while index < len(files):
#     file=files[index]
#     item=file.split('.')
#     name=item[0]
#     ext=item[1]
#     index+=1
#     if name in output:
#         output[ext]+=[name]
#     else:
#         output[ext]=[name]
# print(output) workput one more time 

# num=int(input())
# sum=0
# index=0
# while index<len(num):
#     last=num%10
#     index+=1
# print(last)
    
# num=int(input())
# output=0
# while num!=0:
#     last=num%10
#     if last%2==0:
#         output+=last
#     num//=10
# print(output)


# num=5
# for row in range(7):
#     for col in range(7):
#         if col<=num//2 or row >num//2:
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# num=7
# for row in range(7):
#     for col in range(7):
#         if row==0 or row==num-1 or col==0 or row+col<=num-1 or row>=col:
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# num=7
# for row in range(7):
#     for col in range(7):
#         if row==0 or row==col or row+col==num-1 or col==0 or row==num-1 or col==num-1:
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# num=7
# for row in range(num):
#     for col in range(num):
#         if row==0  or row == col and row+col<=num-1 or row+col==num-1 and row < col:
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# num=7
# for row in range(7):
#     for col in range(7):
#         if  row+col>=num-1:
#             print("*",end="")
#         else:
#             print("_",end="")
#     # print()

# num=7
# for row in range(7):
#     for col in range(7):
#         if row==0 or col ==num-1 or row==num-1 or row >2 and col==0 :
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# num=7
# for row in range(7):
#     for col in range(7):
#         if row==0 or col==0 or col<=3 and row==num-1 or col==3 and row+col>5 or row==3 and row +col>6 or col==6 and row>3:
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# num=7
# for row in range(7):
#     for col in range(7):
#         if col==0 or col==num-1 or row==col and row+col<=6 or row<col and row+col==num-1:
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# num=7
# for row in range(num):
#     for col in range(num):
#         if col==0 or row==0 or row==num//2 or col==num-1 and row<=2 or row >col and row+col in (5,7,9):
#             print("*",end="")
#         else:
#             print("_",end="")
#     print() not crt

# num=7
# for row in range(7):
#     for col in range(7):
#         if row==0 or row==num-1 or row==num//2 or col==0 and row+col<=2 or col==num-1 and row+col in (10,11):
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# num=7
# for row in range(7):
#     for col in range(7):
#         if row==col and row+col<=6 or row+col==num-1 and row<col or col==num//2 and row>=4 :
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# num=7
# for row in range(7):
#     for col in range(7):
#         if row==num//2 or row ==4 or row==5 or row == 6 or row==0 or row+col==num-1 or row+col<=5 :
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# num=7
# for row in range(num):
#     for col in range(num):
#         if row==col or row<col:
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# num=7
# for row in range(num):
#     for col in range(num):
#         if row==num-1 or col==0 and row in (4,5) or col==num-1 and row>=2 or row==4 and col in (1,2) or col ==2 and row in (2,3) or col==3 and row in (2,3,4) or row==4 and col in (4,5) or col==5 and row in (2,3) or row ==5:
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# n=6
# num=1
# for row in range(1,n):
#     for col in range(row):
#         print(num,end="")
#         num+=1
#     print()


# n=10
# num=0
# for row in range(n):
#     print("_" * (n-row),end=" ")
#     for col in range(row):
#         print(num,end="")
#         num+=1
#     print()


# n=5
# for row in range(n):
#     char="A"
#     for col in range(n):
#         print(char,end="")
#         char=chr(ord(char)+1)
#     print()  abcde,abcde,abcde


# n=3
# char="A"
# for row in range(n):
#     for col in range(n):
#         print(char,end="")
#         char=chr(ord(char)+1)
#     print()  abc,def,ghi


# n=3
# char="A"
# for row in range(n):
#     for col in range(n):
#         print(char,end="")
#     print()
#     char=chr(ord(char)+1) aaa,bbb,ccc


# n=3
# char="A"
# for row in range(n):
#     new=char
#     for col in range(n):
#         print(new,end="")
#         new=chr(ord(new)+1)
#     print()
#     char=chr(ord(char)+1) abc,bcd,cde



    
# n=5
# for row in range(5):
#     for col in range(5):
#         if col==0 or row==n-1 or row==col:
#             print("*",end="")
#     print()

# num=7
# for row in range(7):
#     for col in range(7):
#         if col==0 or col==num-1 or row==col and row+col<=6 or row<col and row+col==num-1:
#             print("*",end="")
#         else:
# #             print("_",end="")
# #     print()

# n=7
# char="A"
# for row in range(n):
#     new=char
#     for col in range(n):
#         if col <n//2:
#             print(new,end="")
#             new=chr(ord(new)+1)
#         else:
#             print(new,end="")
#             new=chr(ord(new)-1)
#     print()
#     char=chr(ord(char)+1)   abcdcba


# count=0
# while count<=20:
#     count+=2
#     print(count)  firts 10 even numberes


# count=1
# while count<=20:
#     count+=2
#     print(count) first 10 odd number

# num=int(input())
# start=1
# while start<=num:
#     print(start)
#     start+=1  natural numbers

# num=int(input())
# start=0
# while start<=num:
#     print(start)
#     start+=1  whole numbers

# num=10
# count=0
# while count<=num:
#     result=count**2
#     print(result)
#     count+=1   square

# num=300
# count=10
# while count<num:
#     print(count)
#     count+=10   10,20,30.....300

# num = 105
# while num >= 7:
#     print(num, end=",")  
#     num -= 7   105,98,91....7

# num=10
# while num<=300:
#     print(num)
#     num+=10  anothe method of 10,20,30

# num=10
# while num>=0:
#     print(num)
#     num-=1  10,9,8,7

# num=10
# sum=0
# start=1
# while start<=num:
#     sum+=start
#     start+=1
#     print(f"The sum of the first {num} natural numbers is: {sum}")

# n = 10 
# sum_of_natural_numbers = 0 
# i = 1 
# while i <= n:
#     sum_of_natural_numbers += i
#     i += 1
# print(f"The sum of the first {n} natural numbers is: {sum_of_natural_numbers}")


# def add():
#     a=10
#     b=20
#     c=a+b
#     print(c)
# add()


# def count(start:int,end:int):
#     if start>end:
#         return None
#     else:
#         print(start)
#         count(start+1,end)
# count(1,10)


# def even(start:int,end:int):
#     if start>end:
#         return None
#     else:
#         if start%2==0:
#             print(start)
#         even(start+1,end)
# even(1,20)

# def factorial(num:int):
#     if num==1 or num==0:
#         return 1
#     else:
#         return num*factorial(num-1)
# hey=factorial(5)
# print(hey) 

# def fibonacci(num):
#     if num==1:
#         return 0
#     elif num==2 or num==3:
#         return 1
#     else:
#         return fibonacci(num-1)+fibonacci(num-2)
# res=fibonacci(7)
# print(res)


# def arm_strong(num:int):
#     sum=0
#     temp=num
#     length=len(str(num))
#     while temp!=0:
#         last=temp%10
#         sum+=last**length
#         temp//10
#     if num==sum:
#         return True
#     else:
#         return False
# hey=arm_strong(123)
# print(hey)

# from math import factorial
# def is_strong(num:int):
#     sum=0
#     temp=num
#     while temp!=0:
#         digit=temp%10
#         sum+=factorial(digit)
#     if num==sum:
#         return True
# res=is_strong(233)
# print(res)


# num=int(input())
# factorial=1
# for factor in range(1,num+1):
#     factorial*=factor
# print(factorial)

# class SBI:
#     location="salem"
#     ceo="Nithishs"
#     isfc_code="420JKAHSDLBVFK"
#     def __init__(self,name:str,account_no:int,pin:int,balance:int):
#         self.name=name
#         self.balance = balance
#         self._account_no = account_no
#         self.__pin = pin
#         self.transaction = []
#     def deposit(self,amount:int):
#         print(f"depositing rs.{amount} into your account")
#         self.balance+=amount
#         self.transaction.append(f"deposited rs.{amount}")
#     def withdraw(self,pin:int,amount:int):
#         if self.__pin == pin:
#             if self.balance>amount:
#                 print(f"{amount}debited")
#                 self.balance-=amount
#                 self.transaction.append(f"{amount}debited")
#             else:
#                 print("Insufficent balance")
#         else:
#             print("Wrong pin")
#     def display_transactions(self):
#         for transaction in self.transaction:
#             print(transaction)
#             import time 
#             time.sleep(.5)
# Nithish=SBI("saranya",17238923,14314,2000)
# Nithish.deposit(2000)
# Nithish.deposit(2000)
# Nithish.deposit(2000)
# Nithish.deposit(2000)
# Nithish.withdraw(14314,2000)
# Nithish.display_transactions()


# class nithisfood:
#     wrap = "paratto"
#     veggies = ["cabbage",'onion']
#     _chicken = "not bad"
#     __masala = ["s","y","q"]
#     def process(self):
#         print("finally chop grilled chicken")
#     @property
#     def masala(self):
#         print("cannot access the file")
#     @masala.setter
#     def masala(self,new_masala):
#         print("cannot modify")
# plate1=nithisfood()
# plate1.__masala

# class Battery:
#     def __init__(self,name,capacity):
#         self.name = name
#         self.capacity = capacity
#     def charge(self):
#         print(f"{self.name}battery is charging...")
#     def discharge(self):
#         print(f"{self.name}battery is discharging...")
# class SmartPhone:
#     Battery = Battery("li-ion",5000)
#     def __init__(self,name):
#         self.name = name
#     def lanch_app(self,app_name):
#         print(f"{self.name}lanchinf{app_name}")
#     def play_music(self,song_name):
#         print(f"{self.name} playing{song_name}")
# apple=SmartPhone("iphone")
# apple.play_music("hey maN")
# print(apple.Battery.name)
# apple.Battery.discharge()

# from math import pi
# class cirlce:
#     perimeter = '2*pi* radius'
#     area = "pi(radius**2)"
#     def __init__(self,raduis:int):
#         self.radius = raduis
#     def get_periometer(self):
#         perimeter = 2*pi*self.radius
#         return perimeter
#     def get_area(self):
#         area = pi*(self.radius**2)
#         return area
#     @classmethod
#     def from_diameter(cls,diameter:int):
#         radius = diameter/2
#         return cls(radius)
# c1=cirlce(10)
# c1=cirlce.from_diameter(20)
# c2=c1.from_diameter(20)
# print(c2)

def closest_number(nums):
    a=0
    closest = nums[0]
    min_distance = abs(nums[0] - a)
    
    for num in nums[1:]:
        distance = abs(num - a)
        if distance < min_distance or (distance == min_distance and num > closest):
            closest = num
            min_distance = distance
    return closest
nums=[-1,-2,1]
print(closest_number(nums))