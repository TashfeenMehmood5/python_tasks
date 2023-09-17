# Sets has a whole bunch of methods available.

# add() Adds an element to the set
# Python code to demonstrate addition of tuple to a set.
s = {'g', 'e', 'e', 'k', 's'}
t = ('f', 'o')
l = ['a', 'e']
# adding tuple t to set s.
s.add(t)
# adding list l to set s.
s.update(l) 
print(s)
print("****************************************")

# clear() Removes all the elements from the set
# initialzing a set
number_set = {1, 2, 3, 4, 5}
# clearing the set
number_set.clear()
# printing the set
print(number_set)
print("****************************************")

# copy() Returns a copy of the set
number_set.copy()
print(number_set)
print("****************************************")

# difference() Returns a set containing the difference between two or more sets
number_set1 = {1, 2, 3, 4, 5}
number_set2 = {6, 2, 8, 4, 9}
number_set2.difference(number_set1)
print("Difference of two sets = ",number_set2)
print("****************************************")

# difference_update() Removes the items in this set that are also included in another, specified set

number_set2.difference_update(number_set1)
print("Difference of two sets = ",number_set2)
print("****************************************")

# discard() Remove the specified item

number_set1.discard(4)
print("Difference of two sets = ",number_set1)
print("****************************************")

# intersection() Returns a set, that is the intersection of two or more sets
num_set1 = {1, 2, 3, 4, 5}
num_set2 = {6, 2, 8, 4, 9}
num_set2.intersection(num_set1)
print("Intersection of two sets = ",num_set2)
print("****************************************")

# intersection_update() Removes the items in this set that are not present in other, specified set(s)

num_set2.intersection_update(num_set1)
print("Intersection of two sets = ",num_set2)
print("****************************************")

# isdisjoint() Returns whether two sets have a intersection or not

num_set1.isdisjoint(num_set2)
print("check is two sets have intersection or not  = ",num_set1)
print("****************************************")

# issubset() Returns whether another set contains this set or not
num_set2.issubset(num_set1)
print("check other set contain this set or not  = ",num_set2)
print("****************************************")

# issuperset() Returns whether this set contains another set or not

num_s1 = {5,7,2,9}
num_s2 = {6,9,3,8}
num_s2.issuperset(num_s1)
print("check this set contains another set or not  = ",num_s2)
print("****************************************")

# pop() Removes an element from the set
num_s1.pop()
print("New set is = ",num_s1)
print("****************************************")

# remove() Removes the specified element
num_s2.remove(3)
print("New set after removing an element is =", num_s2)
print("****************************************")

# union() Return a set containing the union of sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print("Symetric difference is = ",z)
print("****************************************")

# symmetric_difference() Returns a set with the symmetric differences of two sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print("Symetric difference is = ",z)
print("****************************************")
# symmetric_difference_update() Inserts the symmetric differences from this set and another

z = x.symmetric_difference_update(y)
print("Symetric difference is = ",z)
print("****************************************")

# update() Update the set with another set, or any other iterable
x.update(y)
print(" updated set is = ",x)