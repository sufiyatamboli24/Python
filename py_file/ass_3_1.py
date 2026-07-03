#W PP which calculates the Sum of tuple element
def sum(test_tup):
    count=0
    for i in test_tup:
        count+=i
    return count
test_tup=(2,3,4,1)
print(sum(test_tup))
