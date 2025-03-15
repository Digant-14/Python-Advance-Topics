#Write a Python program to remove all even numbers from a given list.\
list=[]
a=int(input("Enter Range:"))
#for takibg user input data
for i in range(a):
    element=int(input("Enter list item:"))
    list.append(element)
print("Entered List:",list)

#applying given condition
for i in list:
    if(i%2==0):
        list.remove(i)
print("Output List",list)