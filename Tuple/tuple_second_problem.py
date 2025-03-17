#Write a program to find the index of an element in a tuple

def index_finder(test_tuple):
    a=int(input("Enter the Value:"))
    if a in test_tuple:
        print(test_tuple.index(a))
    else:
        print("Entered value not in Tuple!!")

my_tuple=(1,2,6,4,5,9,7)
index_finder(my_tuple)