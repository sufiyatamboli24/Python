"""WPP accept string from user then change first letter into upper case and print the string then
ask for replace the word and replace that word in string and print the output
"""
s=input("enter the string:")
s=s.capitalize()
print("capital sting:",s)
old=input("Enter the word u want to change:")
new=input("enter new word:")
s=s.replace(old,new)
print("updated string:",s)