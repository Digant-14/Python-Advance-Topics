#Write a program to merge two lists alternately.

#1 method by using operator
list1=[1,2,8,5,6,7]
list2=["Motherboard","RAM","ROM","IC","PSU"]
list3=list1+list2
print(list3)

#2 method by using extend function
list1.extend(list2)
print(list1)