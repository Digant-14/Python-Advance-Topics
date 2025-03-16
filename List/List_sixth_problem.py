#Remove all occurrences of a specific element from a list.
list=[1,2,2,3,3,4,4,4,5,8,9,9]

def remove_items(test_list, item): 
	# remove the item for all its occurrences 
	c = test_list.count(item) 
	for i in range(c): 
		test_list.remove(item) 
	return test_list 
	

#driver code
item = int(input("Enter A NUMBER:"))
# printing the original list 
print("The original list is :" + str(list)) 

# calling the function remove_items() 
res = remove_items(list, item) 

# printing result 
print("The list after performing the remove operation is :" + str(res))