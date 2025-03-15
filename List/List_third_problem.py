#Find the second largest number in a list without using max()

#1 method by using indexing technique 
list=[2,8,5,6,9,55,27,36]
sec_max=sorted(list)[-2]
print("SECOND MAXIMUM ELEMENT IN LIST 1 IS:",sec_max)

#2 method by using loop
list2=[87,85,63,95,24,64]
sl_val=list2[0] #storing first elemnt
l_val=list2[0] #storing first element

for i in range(len(list2)):
    if list2[i]>l_val:   #using loop find largest no.
        l_val=list2[i]   #overwrite the value by storing largest no.
for i in range(len(list2)):
    if list2[i]>sl_val and list2[i]!=l_val:  #again using loop find second largest y compare with sl-val with l-wal
        sl_val =list2[i] #overwrite the value by storing second largest no.

print("SECOND MAXIMUM ELEMENT IN LIST 2 IS:",sl_val)