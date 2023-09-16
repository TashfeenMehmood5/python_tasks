# Dictionaries have a bunch of methods available.

# clear() Removes all the elements from the dictionary
d = {1: "geeks", 2: "for"}
d.clear()
print("dictonary = ",d)

print("****************************************")

# copy() Returns a copy of the dictionary
original_marks = {'Physics':67, 'Maths':87}

copied_marks = original_marks.copy()

print('Original Marks:', original_marks)
print('Copied Marks:', copied_marks)

# fromkeys() Returns a dictionary with the specified keys and value
# keys for the dictionary
alphabets = {'a', 'b', 'c'}
# value for the dictionary
number = 1
# creates a dictionary with keys and values
dictionary = dict.fromkeys(alphabets, number)
print(dictionary)

print("****************************************")

# get() Returns the value of the specified key

scores = {
    'Physics': 67, 
    'Maths': 87,
    'History': 75
}

result = scores.get('Physics')
print("value of specified key is = ",result)

print("****************************************")

# items() Returns a list containing a tuple for each key value pair

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales.items())

print("****************************************")

# keys() Returns a list containing the dictionary's keys
 
numbers = {'key_1': 'one', 'key_2': 'two', 'key_3': 'three'}
# extracts the keys of the dictionary
dictionary_Keys = numbers.keys()
print(dictionary_Keys)

print("****************************************")

# pop() Removes the element with the specified key
# create a dictionary
marks = { 'Physics': 67, 'Chemistry': 72, 'Math': 89 }
element = marks.pop('Math')
print('Popped Marks:', element)
print("****************************************")

# popitem() Removes the last inserted key-value pair

person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print("original dictonary = ",person)
# ('salary', 3500.0) is inserted at the last, so it is removed.
result = person.popitem()
print('Removed Value = ', result)
print('updated dictonary= ', person)

print("****************************************")
# setdefault() Returns the value of the specified key. If the key does not exist insert the key, with the specified value

person = {'name': 'Phill', 'age': 22}
print('Dictonary = ',person)
age = person.setdefault('age')
print('value of specified key is  = ',age)
print("****************************************")

# update() Updates the dictionary with the specified key-value pairs
marks = {'Physics':67, 'Maths':87}
internal_marks = {'Practical':78}
marks.update(internal_marks)
print(marks)

print("****************************************")
# values() Returns a list of all the values in the dictionary
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
values = sales.values()
print('Original items:', values)























