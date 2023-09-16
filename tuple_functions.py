#Python Tuple inbuilt functions

# 1	cmp(tuple1, tuple2)	It compares two tuples and returns true , if tuple1 is greater than tuple2 otherwise false.
# cmp is not used in pyhton 3 , its used in pyhton 2 so now we are implementing alternative of cmp function.

# when a<b
a = 1
b = 2
print((a<b)) 
 
# when a = b
a = 2
b = 2
print((a == b)) 
 
# when a>b
a = 3
b = 2
print((a > b))

print("****************************************")

# 2	len(tuple)	It calculates the length of the tuple.

tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
print ("First tuple length : ", len(tuple1))
print ("Second tuple length : ", len(tuple2))
print("****************************************")

# 3	max(tuple)	It returns the maximum element of the tuple.
# Creating tuples
Tuple = ( 1, 3, 4, 2, 5, 6 ) 
res = max(Tuple)
print('Maximum element of Tuple is = ', res)
print("****************************************")

# 4	min(tuple)	It returns the minimum element of the tuple.
res = min(Tuple)
print('Minimum element of Tuple is = ', res)
print("****************************************")

# 5	tuple(seq)	It converts the specified sequence to the tuple.
List = [123, 'xyz', 'zara', 'abc']
print("Given sequence =  ",List)
Tuple = tuple(List)
print("Above sequence is converted into tuple = ", Tuple)






















