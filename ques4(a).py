def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
# Driver Code
duplicate = [[10,20],[40],[30,56,25],[10,20],[33],[40]]
print(Remove(duplicate))
