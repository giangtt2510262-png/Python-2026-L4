import math
x = 2
x = x + 2
print(x)

j = 23 
k = j % 5
print(k)

print(99 / 100 )

print(float(99) / 100)


i = 42
f = float(i)
print(f)

print('Hi' * 5)

x = 21
if x < 10:
 print('Smaller than 10')
elif x < 20:
 print('Smaller than 20')
else:
 print('Bigger than 20')
print('End')
names = [ "ICT", "ict" ]
names += ["Ict"]
print(names)
names[1] = "I See Tea"
print(names)
names[1:3] = [ "Icy Tea", "I See Tea" ]
print(names)
names[1:1] += ["Ice city"]
print(names)
del names[1]
print(names)
names.remove('ICT')
print(names)
numbers = range(1, 10, 5)
print(list(numbers))

info = {"name": "USTH", "age": 10, \
        "depts": [ "ict", "ged"] }
print(info["name"])
print(info["age"])
print(info["depts"])

del info["depts"]
print(info)

n=5
while n > 0:
 print(n)
 n = n -1 
 print("Blast off!")

x= range(5)
print(x)

a = 23 
b = 5 
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

x = 21
if x < 10:
 print("Smaller than 10")
elif 10 < x < 20:
  print("Smaller than 20") 
else:
 print("Bigger than 20")
print("End") 
#append
names.append("Ict")
print(names)
#replace
names[1] = "I See Tea"
print(names)
#name.sorts
names.sort()
print("After sort(): ", names)
del names[1]
print("After del names[1]:  ", names)

for n in range(5,0,-1):
   print(n)
  print("Blast ooff!") 
