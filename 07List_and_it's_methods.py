l1 = [7728,73.3,"manas",78,69]

print(type(l1))
print(l1)

# there are many methods in list 
''' list are mutable 
and strings are inmutable 
so we can modify lists using various methods '''

l1.remove(73.3)
print("after modification in l1 = ",l1)

l1.remove("manas")
print("after modification in l1 = ",l1)


l1.sort()
print("after sorting list is ",l1)

''' there are many more methods like append(),extend(),pop(), etc'''