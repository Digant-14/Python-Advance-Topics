#Convert a tuple (1, 2, 3, 4, 5) into a list, modify it, and convert it back to a tuple.
f_tuple=("Digant","Abhijeet","Rahul","Aditya","Arbaz","Deepanshu")

try:
    f_list=list(f_tuple)
    print("Tuple converted to List Successfully!:",f_list)
except:
    print("Something went wrong")

try:
    s_tuple=tuple(f_list)
    print("List converted to Tuple successfully!:",s_tuple)
except:
    print("Error occured")