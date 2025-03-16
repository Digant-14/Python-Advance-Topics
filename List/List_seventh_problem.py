#Count the frequency of each element in a list

def count(lst):
    freq_dict = {}
    
    for elem in lst:
        if elem in freq_dict:
            freq_dict[elem] += 1
        else:
            freq_dict[elem] = 1
            
    return freq_dict


print(count([1,2,2,3,3,4,4,4,5,7,8,9,9]))