#WPP to update the element in tuple
test_tup = (5, 20, 3, 7, 6, 8)
old = int(input("Enter the value in above tuple which you want to change = "))
new = int(input("Enter the new value = "))

n = list(test_tup)

for i in range(len(n)):
    if n[i] == old:
        n[i] = new

test_tup = tuple(n)
print("Updated tuple:", test_tup)