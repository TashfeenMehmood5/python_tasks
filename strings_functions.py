# Strings have a bunch of methods available.

# capitalize() Converts the first character to upper case
name = "geeks FOR geeks"
print(name.capitalize())
print("****************************************")

# casefold() Converts string into lower case
my_string_1 = "THIS SHOULD ALL BE IN LOWERCASE!"
print(my_string_1.casefold())
print("****************************************")

# center() Returns a centered string
string = "geeks for geeks"
new_string = string.center(24)
# here fillchar not provided so takes space by default.
print("After padding String is: ", new_string)
print("****************************************")

# count() Returns the number of times a specified value occurs in a string

my_string = "GeeksForGeeks"
char_count = my_string.count('e')
print(char_count)
print("****************************************")

# encode() Returns an encoded version of the string

s = 'ciao'
b=s.encode()
s=b.decode()
# default encoding in Python
print(b)
print(s)
print("****************************************")
# endswith() Returns true if the string ends with the specified value

message = 'Python is fun'
# check if the message ends with fun
print(message.endswith('fun'))
print("****************************************")

# expandtabs() Sets the tab size of the string

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
print("****************************************")
# find() Searches the string for a specified value and returns the position of where it was found

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
print("****************************************")

# format() Formats specified values in a string

txt = "For only {price:.2f} dollars!"
print("format specificied value is = ",txt.format(price = 49))
print("****************************************")

# format_map() Formats specified values in a string

point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))
print("****************************************")
# index() Searches the string for a specified value and returns the position of where it was found

text = 'Python is fun'
# find the index of is
result = text.index('is')
print("index = ",result)
print("****************************************")

# isalnum() Returns True if all characters in the string are alphanumeric

txt1 = "Company12"
x = txt1.isalnum()
print("string is alphaneumeric = ",x)
print("****************************************")

# isalpha() Returns True if all characters in the string are in the alphabet

x = txt.isalpha()
print("string is alphabetic = ",x)
print("****************************************")

# isascii() Returns True if all characters in the string are ascii characters
x = txt.isascii()
print(" characters are ASCII = ", x)
print("****************************************")

# isdecimal() Returns True if all characters in the string are decimals

txt2 = "1234"

x = txt2.isdecimal()

print(" String is decimal = ",x)
print("****************************************")

# isdigit() Returns True if all characters in the string are digits

phoneNumber = '9625783624'
isCorrect = phoneNumber.isdigit()
print('does phoneNumber contains all the number ->', isCorrect)
print("****************************************")

# isidentifier() Returns True if the string is an identifier

txt3 = "Demo"
x = txt3.isidentifier()
print(" String is identifier = ",x)
print("****************************************")

# islower() Returns True if all characters in the string are lower case
t = "hello world!"
x = t.islower()
print("characters are lowercase ",x)
print("****************************************")

# isnumeric() Returns True if all characters in the string are numeric
n = "788"
y = n.isnumeric()
print("string is numeric ",y)
print("****************************************")
# isprintable() Returns True if all characters in the string are printable
value = "Hello!\nAre you #1?"
x = value.isprintable()
print("string is printable ",x)
print("****************************************")

# isspace() Returns True if all characters in the string are whitespaces
string = "\n\t\n"
print("string are whitespaces ",string.isspace())
print("****************************************")

# istitle() Returns True if the string follows the rules of a title
v = "Hello, And Welcome To My World!"
x = v.istitle()
print("string follows the rule of title ",x)
print("****************************************")

# isupper() Returns True if all characters in the string are upper case
tx = "THIS IS NOW!"
x = tx.isupper()
print("string is in uppercase ",x)
print("****************************************")

# join() Converts the elements of an iterable into a string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print("convert iterable into string ",x)
print("****************************************")

# ljust() Returns a left justified version of the string
t = "banana"
x = t.ljust(20)
print(x, "is my favorite fruit.")
print("****************************************")

# lower() Converts a string into lower case
message = 'PYTHON IS FUN'
# convert message to lowercase
print("convert message to lowercase",message.lower())
print("****************************************")

# lstrip() Returns a left trim version of the string
string1 = " hey how are you " 
# Removes spaces from left.
print(string1.lstrip())
print("****************************************")

# maketrans() Returns a translation table to be used in translations specify to translate chars
str1 = "wy"
# specify to replace with
str2 = "gf" 
# delete chars
str3 = "u" 
# target string
trg = "weeksyourweeks" 
# using maketrans() to  construct translate table
table = trg.maketrans(str1, str2, str3)
# Printing original string
print ("The string before translating is : ", end ="")
print ("translation table ",trg)
print("****************************************")

# partition() Returns a tuple where the string is parted into three parts
q= "I could eat bananas all day"
z = q.partition("bananas")
print("partition of string is ",z)
print("****************************************")

# replace() Returns a string where a specified value is replaced with a specified value
i = "one one was a race horse, two two was one too."
x = i.replace("one", "three")
print("replaced value is ",x)
print("****************************************")

# rfind() Searches the string for a specified value and returns the last position of where it was found
p = "Mi casa, su casa."
x = p.rfind("casa")
print("search and find specified value which is ",x)
print("****************************************")

# The rindex() method finds the last occurrence of the specified value.
f = "Mi casa, su casa."
m = f.rfind("casa")
print("finds the last occurrence of the specified value. ",m)
print("****************************************")

# rjust() Returns a right justified version of the string
g = "banana"
c = g.rjust(20)
print(c, "is my favorite fruit.")
print("****************************************")

# rpartition() Returns a tuple where the string is parted into three parts
s = "I could eat bananas all day, bananas are my favorite fruit"
d = s.rpartition("bananas")
print("Returns a tuple where the string is parted into three parts ",d)
print("****************************************")

# rsplit() Splits the string at the specified separator, and returns a list
w = "apple, banana, cherry"         # setting the maxsplit parameter to 1, will return a list with 2 elements!
l = w.rsplit(", ", 1)
print("Splits the string at the specified separator, and returns a list ",l)
print("****************************************")

# rstrip() Returns a right trim version of the string
h = "     banana     "
k = h.rstrip()
print("of all fruits", k, "is my favorite")
print("****************************************")

# split() Splits the string at the specified separator, and returns a list
o= "welcome to the jungle"
a= o.split()
print("Splits the string at the specified separator, and returns a list",a)
print("****************************************")

# splitlines() Splits the string at line breaks and returns a list
# \n is a line boundary 
sentence = 'I\nlove\nPython\nProgramming.'
# returns a list after spliting string at line breaks 
resulting_list = sentence.splitlines()
print("Splits the string at line breaks and returns a list ",resulting_list)
print("****************************************")

# startswith() Returns true if the string starts with the specified value
message1 = 'Python is fun'
# check if the message starts with Python
print(message1.startswith('Python'))
print("****************************************")

# strip() Returns a trimmed version of the string
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(" trimmed version of the string is ",x)
print("****************************************")

# swapcase() Swaps cases, lower case becomes upper case and vice versa
my_string = "foLLow SCALER topics on TWIttER"
# Swapping the case with the swapcase function
my_string_swapcase = my_string.swapcase()
print("Swaps cases, lower case becomes upper case and vice versa are",my_string_swapcase)
print("****************************************")

# title() Converts the first character of each word to upper case
txt = "Welcome to my world"
x = txt.title()
print("Converts the first character of each word to upper case ",x)
print("****************************************")

# translate() Returns a translated string
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print("translated string is",txt.translate(mydict))
print("****************************************")

# upper() Converts a string into upper case
message2 = 'python is fun'
# convert message to uppercase
print("upercase string is ",message2.upper())
print("****************************************")

# fill() Fills the string with a specified number of 0 values at the beginning
original_string = "42"
desired_length = 5
filled_string = "0" * (desired_length - len(original_string)) + original_string
print("Filled string with a specified number of 0 values at the beginning is ",filled_string)  
