#Given a list of numbers, create a new list with squares of each number

first_list=[]
squared_list=[]
a=int(input("Enter the Length of List:"))

for i in range(a):
    b=int(input("Enter list Item:"))
    first_list.append(b) #adding element in empty list through loop

for i in first_list:
    squared_list.append(i**2) #squaring the user input list

print(first_list)
print(squared_list)