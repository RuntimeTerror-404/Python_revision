name = "Mohit"
# print("my name is "+name)

age = 19

# print(f"my name is {name} and my age is {age}")

s = "123@12, hello"
# print(s.capitalize())
# print(s.split())
# print(s.startswith("w"))
# print(s.find("W"))
# print(s.isalnum())
# print(s.isnumeric())
# print(s.strip())

leng = name.__len__()

str = "hello world"
arr = []

arr[::] = str

arr1 = list(str.split(" "))
# print(arr1)
# print(len(arr1))

arr3 = []
for i in range(0, leng):
    arr3.append(name[i])

print(arr3)
