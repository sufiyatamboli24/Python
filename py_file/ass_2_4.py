"""WPP which accept the string from user and print reverse string up to no of characters which is
entered by user
"""
s=input("enter the string:")
n=int(input("Enter the number..from where u wnat to reverse string:"))
reverse_word=s[:n][::-1]
result=reverse_word+s[n:]
print("the reversed string :",result)
