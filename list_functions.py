
# Builtin methods for list

L1 = ["John", 102, "USA","iqra",7.89,33,"irtaza",4,7,4] 
print(L1)             
print(L1.clear())                  # clear() Removes all the elements from the list

print("///////////////////////////////////////////////////////////")   

print(L1.copy())                   # copy() Returns a copy of the list

print("///////////////////////////////////////////////////////////")  
                      
print(L1.count(4))                    # count() Returns the number of elements with the specified value              

print("///////////////////////////////////////////////////////////")  
number = [3,5]                        # extend() Add the elements of a list (or any iterable), to the end of the current list
number.extend(L1)
print("updated list is : " ,number) 

print("///////////////////////////////////////////////////////////")  
                      
print(L1.index('iqra'))               # index() Returns the index of the first element with the specified value

print("///////////////////////////////////////////////////////////")                                     
L1.insert(4,"talha")                    # insert() Adds an element at the specified position
print(L1)

print("///////////////////////////////////////////////////////////") 
L1.pop()                                # pop() Removes the element at the specified position
print(L1)

print("///////////////////////////////////////////////////////////") 
L1.append(7)                            # append() Adds an element at the end of the list                      
print(L1)   

print("///////////////////////////////////////////////////////////") 
L1.remove('USA')                        # remove() Removes the first item with the specified value                     
print(L1)  

print("///////////////////////////////////////////////////////////") 
L1.reverse()                            # reverse() Reverses the order of the list                     
print(L1)

print("///////////////////////////////////////////////////////////") 
L2 = [5,9,0,3,1,5]
print(L2)
L2.sort()                               # sort() Sorts the list                                             
print(L2)                