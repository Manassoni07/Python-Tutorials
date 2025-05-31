dict1 = {"Manas":"Good Person","r":"R"}
marks = {"manas" : 99 ,"aditya" : 39}
print(dict1["Manas"])
print(marks["manas"])

# dictionary in python is same as map in cpp 
# .get is used because if key not found in dict so it will not throw error 
print("Marks of manas is ",marks.get("manas"))
print("tuple of keys is ",marks.keys())
print("tuple of values is ",marks.values())
print("tuple of items is ",marks.items())