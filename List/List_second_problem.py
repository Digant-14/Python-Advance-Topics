#Reverse a list without using the built-in reverse() method.

#1 method by using slicing
list=["APPLE","BANANA","MANGO","GRAPES","GUAVA"]
print(list[::-1])

#2 method by using loop
list2=[8,5,6,3,5,7,4]
list3=[]
for i in list2:
    list3.insert(0,i)
print(list3)

#3 method list comprehension
list4=[1,"Digant",2,"Arbaz",3,"Abhijeet",4,"Rahul"]
rev=[list4[i] for i in range(len(list4)-1,-1,-1)]
print(rev)