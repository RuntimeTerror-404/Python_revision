
def sayHello(name):
    print(f"hello {name}, how are you ?")


# sayHello("Mohit")

def sum(x, y):
    z = x+y
    return z

# print(sum(12,32))


def getSum(num1, num2): return num1 + 2*num2


print(getSum(1, 3))

str1 = "2751"  # 7215
str2 = "3219"  # 2391

arr = []

arr[:] = str1

print(arr)

res = " "
x = res.join(arr)
print(x)