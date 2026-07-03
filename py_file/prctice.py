# def sum(test_tup):
#     test=list(test_tup)
#     count=0
#     for i in test:
#         count+=i
#     return count
# test_tup=(2,4,6,8)
# print(sum(test_tup)) 

# test_tup=(2,4,6,8)
# old=int(input("Enter the no.u want to change:"))
# new=int(input("enter the new number:"))
# n=list(test_tup)
# for i in range(len(n)):
#     if n[i]==old:
#         n[i]=new
# test_tup=tuple(n)
# print("updated list:",test_tup)        

# set1={"a","b","c"}
# set2={1,3,5}
# set3=set1.union(set2)
# print(set3)

# thisdict={"pasnad":"omkar",
#           "love":"family",
#           "name":"chandani"}
# result=thisdict["pasnad"]
# print(result)

# child1={"name":"chand",
#         "ID":234
# }
# child2={"name":"omkar",
#         "ID":567
# }
# child3={"name":"maa",
#         "ID":8910
# }
# myfamily={"child1":child1,
#         "child2":child2,
#         "child3":child3,
# }
# print(myfamily["child2"]["name"])

"""WPP accept string from user then change first letter into upper case and print the string then
ask for replace the word and replace that word in string and print the output
"""
# s=input("Enter the string:")
# s=s.capitalize()
# print(s)
# old=(input("Enter the word u want to change:"))
# new=(input("enter the new number:"))
# s=s.replace(old,new)
# print(s)

"""WPP accept two strings from user then concatenate them and print and then repeat the first
string 4 times using Repetition Operator and print
"""
# s1=input("Enter the 1 string:")
# s2=input("Enter the 2 string:")
# con=s1+s2
# print(con)
# repeat=s1*4
# print(repeat)

"""WPP accept the string from users and print the reverse string word by word"""
# s=input("Enter the string:")
# w=s.split()
# result=s[::-1]
# print(result)

"""WPP which accept the string from user and print reverse string up to no of characters which is
entered by user"""
# s=input("Enter the string:")
# n=int(input("Enter the number:"))
# r_w=s[:n][::-1]
# result=s[n:]
# print(result)

"""WPP accept the input from user and calculate the square root and power using the math
functions"""
import math 
# n=float(input("Enter the number:"))
# s=math.sqrt(n)
# print(s)
# p=int(input("Enter the number:"))
# po=math.pow(n,p)
# print(po)

"""write a class Person which accept name and age from user and print them using function """
# class person:
#     def get(self):
#         self.name=input("Enter the string:")
#         self.age=input("Enter the age:")
#     def put(self):
#         print(self.name)
#         print(self.age)
# p=person()
# p.get()
# p.put()

# fibonacci
# n=int(input("Enter the number:"))
# a,b=0,1
# for i in range(n):
#  print(a)
#  a,b=b,a+b 