

# a = list() # a=[]

a = [1, 2, 3]
print(a)

a.append(4)
print(a)

a.insert(3, 5)
print(a)

print(a[3])

try:
    print(a[9])
except IndexError:
    print("존재하지 않는 인덱스")

del a[1]
print(a)

a.remove(3)
print(a)

print(5 in a)