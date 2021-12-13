print("Hello world")

#this is unread
# 
'''
lesson 1 Lists
mylist = ["banana", "cherry", "apple"]
print(mylist)
#aphend an empty list to add to later
mylist2 = list[5, True, "apple", "apple"]
print(mylist2)
#print out the number you ask for
item = mylist[2]
print(item)
#sequence them
for i in mylist:
    print(i)
#check if its in the list
if "orange" in mylist:
    print("yes")
else:
    print("no")
#how many elements in list
print(len(mylist))
#append items
#mylist.append("lemon")
#print(mylist)
#insert items
#mylist.insert(1, "blueberry")
#print(mylist)
#remove last item
#mylist.pop()
#print(item)
#print(mylist)
#remove specific
#item = mylist.remove("cherry")
#print(mylist)
#remove all elements
#item = mylist.clear()
#print(mylist)
#reverse list
#item = mylist.reverse()
#print(mylist)
#sort list
#item = mylist.sort()
#print(mylist)
#new_list = sorted(mylist)
#print(new_list)
#create new list with same elements multiple tiems
#mylist = [0] * 5
#print(mylist)
#concate lists
#mylist2 = [1, 2, 3, 4, 5]
#mylist3 = [4,2,1,0]
#new_list2 = mylist2 + mylist3
#print(new_list2)
"""
"""
#slicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#specify
a = mylist[1:5]
print(a)
#step index
b = mylist[::-1]
print(b)
list_org = ["banana", "cherry", "apple"]
#copy lists
list_cpy = list_org.copy()
print(list_cpy)
#if you modify a copy you modify the original
#list comprehension
mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist]
print(mylist)
print(b)
'''
# 
#lesson 2 Tuples
'''
#tuple cannot be changed after its creation
mytyple = ("Max", 28, "Boston")
print(mytyple)
mytuple = tuple(["Max", 28, "Boston"])
print (mytuple)
item = mytuple[2]
print(item)
for i in mytuple:
    print(i)
if "Jake" in mytuple:
    print("yes")
else:
    print("no")
my_tuple = ('a', 'p', 'p', 'l', 'e')
#how many elements are in
print(my_tuple.count('j'))
#first occurence of element
print(my_tuple.index('p'))
my_list = list(my_tuple)
print(type(my_list))
my_tuple2 = tuple(my_list)
print(my_tuple2)
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)
c = a[:5]
print(c)
d = a[2:]
print(d)
e = a[::-2]
print(e)
my_tuple3 = "Max", 28, "Boston"
name, age, city = my_tuple3
print(name)
print(age)
print(city)
mytuple4 = (0, 1, 2, 3, 4, 5)
i1, *i2, i3 = mytuple4
print(i1)
print(i3)
print(i2)
#comparing tuple and list
#tuple good with large data
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple5 = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_tuple5), "bytes")
print(sys.getsizeof(my_list), "bytes")
# list is larger than tuple even with same
import timeit
print(timeit.timeit(stmt="[0, 1, 2,3, 4, 5]", number = 1000000))
print(timeit.timeit(stmt="(0, 1, 2,3, 4, 5)", number = 1000000))
#takes longer to create list than tuple
'''

#lesson 3 Dictionaries
'''
#dictionary is collectoin data that is unordered and mutable
mydict = {"name": "Max", "Age": 28, "city": "New York"}
print(mydict)
#inserts values into the dict, don't need quotes
mydict2 = dict(name="mary", age=27, city="Boston")
print(mydict2)
value = mydict["name"]
print(value)
#adding values
mydict["email"] = "max@xyz.com"
print(mydict)
#overwriting values
mydict["email"] = "coolmax.com"
print(mydict)
#deleting
#del mydict["name"]
#print(mydict)
#pop method
#mydict.pop("Age")
#print(mydict)
#mydict.popitem()
#print(mydict)
if "name" in mydict:
    print(mydict["name"])
try:
    print(mydict["lastname"])
except:
    print("Error")
#loop through dict
#for keys
for key in mydict.keys():
    print(key)
#for values
for value in mydict.values():
    print(value)
#gives both key and value
for key, value in mydict.items():
    print(key, value)
#creates copy, but changes will change original
mydict_cpy = mydict
print(mydict_cpy)
#to prevent do mydict.copy
my_dict = {"name":"Max", "age":28, "email":"max@xyz.com"}
my_dict2 = dict(name="Mary", age=23, city="Bston")
#to merge
my_dict.update((my_dict2))
print(my_dict)
#will update as well as merge new keys
my_dict_sqr = {3: 9, 6: 36, 9: 81}
print(my_dict_sqr)
#need to use actual keys, not index like 0
value = my_dict_sqr[3]
print(value)
#cannot use lists as keys because they are mutable, key must be unmutable
mytuple = (8, 7)
mydict = {mytuple: 15}
print(mydict)
'''

#lesson 4
#sets are unordered, mutable, no duplicates

myset = {1, 2, 3, 1, 2}
print(myset)
