#301. Python is not strongly typed. it is dynamically typed.
# you can reassign a variable to a completely different type with no error.
x = 5
print(x)       
x = "hello"
print(x)        

#302. input() always returns str. adding str to int raises TypeError.
name = input("Enter name: ")
age = int(input("Enter age: "))
print(age + 10)

#303. because if False: is never executed, x is never created.
# Python does not allocate variables inside blocks that never run.
# so when print(x) is called, x does not exist yet, raising NameError.

#304.
name = "Kelechi"
matric_no = "AUL/22/0001"
course = "Software Engineering"
gpa = 5.0
is_active = True

#305.
a = b = c = [1]
c.append(2)
print(a, b, c)  # [1, 2] [1, 2] [1, 2]
# all three variables point to the same list object in memory.
# changing through c changes the object that a and b also point to.

#306.
a = [1]
b = [1]
c = [1]
c.append(2)
print(a, b, c) 

#307.
# NameError  — accessing a variable that has not been created yet.
# TypeError  — performing an operation on incompatible types e.g int + str.
# ValueError — correct type but wrong value e.g int("hello").

#308.
# crash on purpose:
# print(undefined_var)  # NameError: name 'undefined_var' is not defined

# fix:
undefined_var = "now I exist"
print(undefined_var)

#309.
x = 10  # global x
def show():
    x = 99  # local x, separate from global
    print("inside:", x)
show()
print("outside:", x)  # global x unchanged

#310.
x = 10
def change():
    global x
    x = 20
change()
print(x)  # 20

#311. nonlocal lets a nested function access and modify a variable
#     from its enclosing function (not global, one level up).
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    inner()
    print(count)  # 1
outer()

#312. yes you can chain: a = b = c = 10. all three point to the same value.
# it is acceptable for simple types like int and str.
# avoid it for mutable types like list because of the shared reference bug in Q305.

#313. _ is a throwaway variable used when you need a loop variable
#     but do not actually use the value inside the loop.
for _ in range(5):
    print("hello")

#314.
first_name = "Attah"
last_name = "Maxwell"

full_name1 = first_name + " " + last_name
full_name2 = " ".join([first_name, last_name])
full_name3 = f"{first_name} {last_name}"

print(full_name1)
print(full_name2)
print(full_name3)

#315.
sentence = "I love Python"
words = sentence.split()
word_count = 0
for _ in words:
    word_count += 1
print(word_count)  # 3

#316. False
# int(y) creates a new int object with value 10.
# x already holds 10 but is may or may not be True depending on caching.
# more importantly, is compares identity not value.
# the correct way is x == int(y).
x = 10
y = "10"
print(x == int(y))  # True
print(x is int(y))  # True for small ints due to caching, but not reliable

#317.
name = input("Enter name: ")
age = int(input("Enter age: "))
phone = input("Enter phone: ")
# phone should be str because it may have leading zeros like 08012345678
# and you never do arithmetic on a phone number.

#318. PI = 3.14 is just a regular variable named in UPPER_CASE by convention.
# Python has no enforcement mechanism. you can still do PI = 99 and it works.
# it is not truly constant. UPPER_CASE is only a signal to other developers.

#319. True. Python caches small integers from -5 to 256.
# both a and b point to the same cached object for value 5,
# so their id is identical.
a = 5
b = 5
print(id(a) == id(b))  # True

#320.
# in a script, a=257 and b=257 may share the same id because Python
# optimises the whole file at once and reuses the same object.
# in IDLE or interactive shell, each line is compiled separately,
# so a and b may get different objects and a is b may be False.
a = 257
b = 257
print(a is b)  # True in script, often False in interactive shell

#321.
a = 1
b = 2
c = 3
del a, b, c

#322.
print(dir())    # lists all names in current scope
print(locals()) # shows name-value pairs in local scope

#323.
# str = "hello"    # this shadows the built-in str() function
# print(str(10))   # now raises TypeError because str is now a string not a function
# never name variables after built-ins like str, list, int, print, len.

#324. it is dangerous because you permanently lose access to the built-in str()
# function for the rest of the program. any code that relies on str() will crash
# with a confusing error. always check your variable names against built-ins.

#325.
x = [1, 2, 3]
y_ref = x          # y_ref and x point to same object. changes affect both.
y_copy = x.copy()  # y_copy is independent. changes do not affect x.

y_ref.append(99)
print(x)      # [1, 2, 3, 99]

y_copy.append(0)
print(x)      

#326.
balance = 1000
for _ in range(3):
    balance -= 100
print(balance) 

#327. dynamic variable creation using globals() — creates variable named "x1".
globals()['x' + str(1)] = 10
print(x)  # 10

#328. no. dynamic variables make code hard to read, debug, and maintain.
# you cannot easily track where a variable came from.
# use a dict or list instead to store dynamic data.
data = {"x1": 10, "x2": 20}  # much better

#329.
a, b, c = 1, 2, 3
a, b, c = b, c, a
print(a, b, c)  # 2 3 1

#330. 6. because True has integer value 1. so True + 5 = 1 + 5 = 6.
# bool is a subclass of int so arithmetic works on booleans.
x = True
x = x + 5
print(x)  # 6

#331.
data = None
if data is None:
    print("data has not been assigned yet")
else:
    print("data has a value:", data)

#332.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
total = a + b
difference = a - b
product = a * b
print("Sum:", total)
print("Difference:", difference)
print("Product:", product)

#333. stack stores simple variable names and their references. it is fast and small.
#     heap is where the actual objects (lists, dicts, strings) live in memory.
#     when you write x = [1,2,3], the name x goes on the stack but
#     the list [1,2,3] is created on the heap and x holds the address.

#334.
name = " noun "
clean_name = name.strip().lower()
clean_name = clean_name[0].upper() + clean_name[1:]
print(clean_name)  # Noun

#335.
v = "V"
i = "i"
c = "c"
t = "t"
o = "o"
r = "r"
full = v + i + c + t + o + r
print(full)  # Victor


# DATA TYPES - Deep Dive (336-390)

#336.
print(type([]))    # <class 'list'>
print(type(()))    # <class 'tuple'>
print(type({}))    # <class 'dict'>
print(type(set())) # <class 'set'>

#337. {} creates an empty dict because dict was implemented before set in Python.
# to create an empty set you must use set().
empty_set = set()
print(type(empty_set))  # <class 'set'>

#338.
print(bool(0))      # False
print(bool(0.0))    # False
print(bool(0j))     # False
print(bool(""))     # False
print(bool([]))     # False
print(bool({}))     # False
print(bool(None))   # False

#339. all falsy values in Python:
# 0, 0.0, 0j, "", [], {}, None, set(), tuple(), False

#340. surprising truthy values:
print(bool("False"))   # True  (non-empty string)
print(bool([0]))       # True  (list with one item)
print(bool("  "))      # True  (string with only spaces)

#341.
print("hello" * 0)   # ""   (empty string)
print("hello" * -5)  # ""   (negative also gives empty string)

#342. no. multiplying list by float raises TypeError.
# you can only multiply a list by int.
# [1,2] * 2   gives [1, 2, 1, 2]
# [1,2] * 2.5 raises TypeError

#343. s[::-1] reverses the string using slicing with step -1.
s = "Python"
print(s[::-1])  # nohtyP

#344.
s = "Python Programming"
first_3 = s[:3]
last_3 = s[-3:]
print(first_3)  # Pyt
print(last_3)   # ing

#345. ord() returns the integer ASCII code of a character.
#     chr() returns the character for an ASCII integer.
print(ord('A'))  # 65
print(chr(65))   # A

#346.
s = input("Enter a string: ").lower()
if s == s[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#347.
s = "  hello  "
print(s.strip())   # "hello"   removes both sides
print(s.lstrip())  # "hello  " removes left only
print(s.rstrip())  # "  hello" removes right only

#348.
csv_string = "a,b,c"
parts = csv_string.split(",")   # ['a', 'b', 'c']
joined = "-".join(parts)        # "a-b-c"
print(parts)
print(joined)

#349.
sentence = "I love Java"
new_sentence = sentence.replace("Java", "Python")
print(new_sentence)

#350. strings are immutable. s += "!" does not modify the original string.
# it creates a brand new string object, so the id changes.
s = "hello"
print(id(s))
s += "!"
print(id(s))  # different id — new object was created

#351.
# append() adds the item as a single element (even if it is a list).
# extend() unpacks an iterable and adds each item individually.
a = [1, 2, 3]
a.append([4, 5])
print(a)  # [1, 2, 3, [4, 5]]

b = [1, 2, 3]
b.extend([4, 5])
print(b)  # [1, 2, 3, 4, 5]

#352. None. append() modifies the list in place and returns None.
# never assign the result of append() to a variable.
a = [1, 2, 3]
print(a.append(4))  # None
print(a)            # [1, 2, 3, 4]

#353.
a = [1, 2, 3]
a.insert(0, 99)
print(a)  # [99, 1, 2, 3]

#354.
a = [1, 2, 3]
a.remove(2)   # removes by value (first occurrence)
print(a)      # [1, 3]

b = [1, 2, 3]
b.pop(1)      # removes by index (index 1)
print(b)      # [1, 3]

#355. [2]
a = [1, 2, 3]
a.pop()    # removes last item: 3
a.pop(0)   # removes index 0: 1
print(a)   # [2]

#356. yes. a tuple is immutable but can hold mutable objects inside it.
# you cannot replace the list inside the tuple, but you can change the list itself.
t = ([1, 2], 3)
t[0].append(99)
print(t)  # ([1, 2, 99], 3)

#357. it does NOT error. the tuple structure did not change.
# the list inside the tuple changed, which is allowed.
t = ([1, 2], 3)
t[0].append(99)
print(t)  # ([1, 2, 99], 3)

#358. (5) is NOT a tuple. it is just parentheses around an integer.
print(type((5)))   # <class 'int'>

#359. add a trailing comma to create a single element tuple.
t = (5,)
print(type(t))  # <class 'tuple'>

#360. s={[1,2]} raises TypeError because lists are unhashable (mutable).
# sets require all elements to be hashable.
# s={(1,2)} works because tuples are immutable and hashable.
s = {(1, 2)}
print(s)  # {(1, 2)}

#361. hashable means the object has a fixed hash value that never changes.
# lists are mutable so their content can change, making a consistent hash impossible.
# Python requires dict keys to be hashable so it can find them quickly.

#362.
d = {True: "yes", 1: "no", 1.0: "maybe"}
print(d)  # {True: "maybe"}
# True, 1, and 1.0 are all equal and have the same hash.
# each new entry overwrites the previous one.
# only one key remains, and its value is the last assigned: "maybe".

#363.
d = {"a": 1}
# print(d["b"])      # raises KeyError
print(d.get("b"))    # None  (no error)
print(d.get("b", 0)) # 0    (default value returned)

#364.
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2     # Python 3.9+ merge operator
print(merged)        # {"a": 1, "b": 2}

#365.
d = {"name": "Max", "age": 20}
print(d.keys())    # dict_keys(['name', 'age'])
print(d.values())  # dict_values(['Max', 20])
print(d.items())   # dict_items([('name', 'Max'), ('age', 20)])
# they return special view objects, not plain lists.

#366.
s = "123,456,789"
result = list(map(int, s.split(",")))
print(result)  # [123, 456, 789]

#367.
lst = [1, 2, 3]
result = "-".join(str(n) for n in lst)
print(result)  # "1-2-3"

#368.
result = list(map(int, ["1", "2", "3"]))
print(result)        # [1, 2, 3]
print(type(result))  # <class 'list'>

#369.
mixed = [1, "a", 2.5, True, None, [1]]
for item in mixed:
    print(item, "->", type(item))

#370. True. because bool is a subclass of int in Python.
# True and False are just 1 and 0 with a bool label.
# isinstance checks the entire class hierarchy, so True counts as an int.
print(isinstance(True, int))  # True

#371. isinstance() is better for inheritance checks. type() only matches the exact class.
# if you use type(), a subclass will not match the parent.
print(type(True) == int)       # False (it is bool not int)
print(isinstance(True, int))   # True  (bool is subclass of int)

#372.
value = input("Enter something: ")
if value.isdigit():
    value = int(value)
print(value, type(value))

#373.
data = {"students": [{"name": "Max", "scores": [90, 80]}]}
print(data["students"][0]["scores"][1])  # 80

#374.
import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()       # inner lists are still shared
deep = copy.deepcopy(original)  # completely independent copy
# use deepcopy when you have nested mutable objects.

#375. False. NaN (not a number) is never equal to anything, including itself.
# this is the IEEE 754 floating point standard.
import math
a = float("nan")
print(a == a)  # False

#376.
import math
a = float("nan")
print(math.isnan(a))  # True

#377. they are all falsy but they are NOT the same.
# None means no value.
# 0 is the integer zero.
# "" is an empty string.
# False is a boolean.
# None == False is False. None == 0 is False. None == "" is False.

#378.
lst = [1, 1, 2, 2, 3, 3]
no_duplicates = list(set(lst))
print(no_duplicates)  # order is NOT guaranteed with set

#379.
lst = [1, 1, 2, 2, 3, 3]
no_duplicates = list(dict.fromkeys(lst))
print(no_duplicates)  # [1, 2, 3]  order preserved

#380.
print(len([[]])) # 1  (a list containing one empty list)
print(len([]))   # 0  (an empty list)

#381. a byte string like b"hello" stores raw bytes instead of unicode characters.
# used when reading binary files, working with network data, or encoding text.

#382.
sentence = "hello 42 3.14 world 99"
words = sentence.split()
for word in words:
    try:
        int(word)
        print(word, "-> int")
    except ValueError:
        try:
            float(word)
            print(word, "-> float")
        except ValueError:
            print(word, "-> string")

#383.
import sys
print(sys.getsizeof(10))        # int
print(sys.getsizeof(3.14))      # float
print(sys.getsizeof("hello"))   # str
print(sys.getsizeof([1,2,3]))   # list

#384.
import sys
x = 10
print("value:", x)
print("type:", type(x))
print("id:", id(x))
print("size:", sys.getsizeof(x), "bytes")

#385.
def is_mutable(obj):
    try:
        obj_id = id(obj)
        obj += type(obj)()  # try to add empty version of same type
        return True
    except TypeError:
        return False

print(is_mutable([1, 2]))   # True
print(is_mutable("hello"))  # False

#386. no. you should not use is for string comparison.
# is checks identity (same memory address) not equality.
# string interning means Python sometimes reuses objects for short strings,
# so a is "python" might be True by accident, but this is not guaranteed.
a = "python"
print(a == "python")  # True  (correct way)
print(a is "python")  # True by luck but unreliable

#387. string interning is Python automatically reusing the same memory object
# for identical string literals to save memory.

#388.
student = {
    "name": "Kelechi",
    "age": 20,
    "courses": ["Math", "CS", "English"],
    "grades": {"Math": 85, "CS": 90, "English": 78}
}
print(student)

#389.
import json
student_json = json.dumps(student)
print(student_json)
print(type(student_json))  # <class 'str'>

#390.
import sys
value = input("Enter a value: ")
try:
    value = int(value)
except ValueError:
    pass
print("value:", value)
print("type:", type(value))
print("id:", id(value))
print("bool:", bool(value))
mutable_types = (list, dict, set, bytearray)
print("is mutable:", isinstance(value, mutable_types))


# OPERATORS - Tricky & Projects (391-450)

#391.
# 5 + 2 * 3 ** 2 / 2 - 1
# step 1: 3 ** 2 = 9
# step 2: 2 * 9  = 18
# step 3: 18 / 2 = 9.0
# step 4: 5 + 9.0 = 14.0
# step 5: 14.0 - 1 = 13.0
print(5 + 2 * 3 ** 2 / 2 - 1)  # 13.0

#392. 5.0. division is left to right: 100/10 = 10.0, then 10.0/2 = 5.0
print(100 / 10 / 2)  # 5.0

#393. 5. floor division is also left to right: 100//10 = 10, then 10//2 = 5
print(100 // 10 // 2)  # 5

#394. both give 12. they are identical because * is left-to-right.
print(2 * 3 * 2)    # 12
print((2 * 3) * 2)  # 12

#395.
P = float(input("Principal: "))
r = float(input("Rate (as decimal e.g 0.05): "))
n = int(input("Times compounded per year: "))
t = int(input("Years: "))
amount = P * (1 + r/n) ** (n*t)
print(f"Compound Interest Amount: {amount:.2f}")

#396.
print(-10 / 3)   # -3.3333... (true division)
print(-10 // 3)  # -4         (floor division rounds toward negative infinity)
# -10 // 3 is -4 not -3 because floor always goes to the lower integer.

#397.
print(10 % -3)   # -2  (result takes sign of divisor)
print(-10 % 3)   # 2   (result takes sign of divisor)
# Python's modulo result always has the same sign as the divisor.

#398. divmod(10, 3) returns (3, 1) which is (quotient, remainder).
# same as (10//3, 10%3).
print(divmod(10, 3))  # (3, 1)

#399.
n = 1234
thousands  = n // 1000
hundreds   = (n % 1000) // 100
tens       = (n % 100) // 10
units      = n % 10
print(thousands, hundreds, tens, units)  # 1 2 3 4

#400. 0.1 + 0.2 == 0.3 is False because floats are stored in binary.
# 0.1 and 0.2 cannot be represented exactly in base-2, so their sum
# gives 0.30000000000000004 which does not equal 0.3.
print(0.1 + 0.2 == 0.3)  # False

#401.
a = 0.1 + 0.2
b = 0.3
print(abs(a - b) < 0.00001)  # True (safe float comparison)

#402. False. string comparison uses alphabetical (lexicographic) order.
# 'a' comes before 'b' in the alphabet so "apple" < "banana".
print("apple" > "banana")  # False

#403. True. lists are compared element by element.
# first element 1 == 1, second 2 == 2, third 3 > 2. so left list is greater.
print([1, 2, 3] > [1, 2, 2])  # True

#404. False. a tuple and a list are different types.
# == checks both value and type for these containers.
print((1, 2) == [1, 2])  # False

#405.
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not leap year")

#406.
a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))
if a + b > c and a + c > b and b + c > a:
    print("can form a triangle")
else:
    print("cannot form a triangle")

#407. 2. True is 1 and False is 0. so 1 + 1 + 0 = 2.
print(True + True + False)  # 2

#408.
print(False * 100)  # 0   (0 * 100)
print(True * 100)   # 100 (1 * 100)

#409.
x = 10
y = 20
print(True if x > 5 and y > 5 else False)

#410.
# and truth table:
# True  and True  = True
# True  and False = False
# False and True  = False
# False and False = False

# or truth table:
# True  or True  = True
# True  or False = True
# False or True  = True
# False or False = False

# not truth table:
# not True  = False
# not False = True

#411. 10. and returns the first falsy value or the last value if all are truthy.
# 5 is truthy so Python moves to 10. 10 is the last value so it returns 10.
print(5 and 10)  # 10

#412.
print(0 and 10)   # 0        (0 is falsy so returns immediately)
print(0 or 10)    # 10       (0 is falsy so checks next, 10 is truthy)
print("" or "default")  # "default"

#413.
name = input("Enter name (press enter to skip): ") or "Guest"
print(name)  # if input was empty, name becomes "Guest"

#414.
# not 10 > 5 means not (10 > 5) because > has higher precedence than not.
print(not 10 > 5)     # False
print(not (10 > 5))   # False (same result here)
# they are the same because not is already applied last.

#415.
n = int(input("Enter a number: "))
print(1 <= n <= 100 and n % 2 == 0 and n % 10 != 0)

#416. yes. += works on strings by creating a new concatenated string.
s = "hi"
s += " there"
print(s)  # "hi there"

#417. *= repeats the list. a *= 3 makes the list repeat 3 times.
a = [1]
a *= 3
print(a)  # [1, 1, 1]

#418.
a = [1, 2]
b = a
b += [3]        # += on list calls extend() in place on the same object
print(a)        # [1, 2, 3]  — a is changed because b and a share the object

#419.
a = [1, 2]
b = a
b = b + [3]     # + creates a brand new list, b now points to a new object
print(a)        # [1, 2]    — a is unchanged

#420. += on a list mutates the object in place (like extend).
# because b and a point to the same object, a sees the change.
# b + [3] creates a new list and reassigns b to it.
# a still points to the original object, so a is not affected.

#421. in with dict checks keys only.
d = {"a": 1}
print("a" in d)          # True  (checks keys)
print(1 in d.values())   # True  (checks values)

#422.
sentence = "I Love Python"
word = "python"
print(word.lower() in sentence.lower())  # True

#423. Python caches integers from -5 to 256.
# for those values, any variable holding that number points to the same object.
# for numbers outside that range, Python creates new objects, so is may be False.
a = 10; b = 10
print(a is b)    # True  (cached)

a = 1000; b = 1000
print(a is b)    # False (not cached, separate objects)

#424. interning means Python reuses the same object for certain values to save memory.
# small integers (-5 to 256) and short simple strings are interned automatically.
# this is why is works for small ints but fails for large ones.

#425.
numbers = [1, 3, 5, 7, 8, 9]
has_even = any(n % 2 == 0 for n in numbers)
print(has_even)  # True

#426. ~5 is -6. bitwise NOT flips all bits and the result is -(n+1).
print(~5)   # -6
print(~0)   # -1

#427. << shifts bits left (multiplies by 2 per shift).
#     >> shifts bits right (divides by 2 per shift).
print(5 << 1)  # 10  (5 * 2)
print(5 >> 1)  # 2   (5 // 2)

#428. bitwise operators are used for flags — storing multiple yes/no settings
# in a single integer using individual bits.
READ    = 0b001  # 1
WRITE   = 0b010  # 2
EXECUTE = 0b100  # 4

permission = READ | WRITE  # user has read and write
print(bool(permission & READ))     # True
print(bool(permission & EXECUTE))  # False

#429.
age = int(input("Enter age: "))
status = "adult" if age >= 18 else "minor"
print(status)

#430.
score = int(input("Enter score: "))
grade = "A" if score >= 70 else "B" if score >= 60 else "C" if score >= 50 else "F"
print(grade)

#431.
x = 10 if True else 20
print(x)  # 10

#432. := (walrus) assigns a value AND returns it in the same expression.
# regular = only assigns. := can be used inside conditions and loops.
# while (line := input()) != "quit":  (assigns and tests in one step)

#433.
while (user_input := input("Enter something (or 'quit'): ")) != "quit":
    print("you entered:", user_input)
print("done.")

#434.
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
maximum = a if a >= b and a >= c else b if b >= c else c
print("max:", maximum)

#435.
# top 10 operator precedence (highest to lowest):
# 1.  ()          parentheses
# 2.  **          exponentiation
# 3.  +x, -x, ~x  unary operators
# 4.  *, /, //, % multiplication/division
# 5.  +, -        addition/subtraction
# 6.  <<, >>      bitwise shift
# 7.  &           bitwise AND
# 8.  ^           bitwise XOR
# 9.  |           bitwise OR
# 10. ==,!=,>,<,>=,<=,in,is  comparison

#436.
result = (2 + 3) * 4   # without () it would be 2 + 12 = 14, not 20
print(result)          # 20

#437.
# eval() is dangerous because it executes any Python code passed to it.
# a user could type: __import__('os').system('del C:\\') and cause damage.
# safe alternative: use if/elif to handle only specific operations.

# dangerous:
# result = eval(input("Enter expression: "))

# safe:
a = float(input("Enter a: "))
b = float(input("Enter b: "))
op = input("Operator: ")
if op == "+": print(a + b)
elif op == "-": print(a - b)
elif op == "*": print(a * b)
elif op == "/" and b != 0: print(a / b)

#438.
a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Operator (+,-,*,/,%,//,**): ")

if op == "+":   print(a + b)
elif op == "-": print(a - b)
elif op == "*": print(a * b)
elif op == "/":
    if b == 0: print("cannot divide by zero")
    else: print(a / b)
elif op == "%":  print(a % b)
elif op == "//": print(a // b)
elif op == "**": print(a ** b)
else: print("invalid operator")

#439.
subjects = []
for i in range(5):
    mark = float(input(f"Enter mark for subject {i+1}: "))
    subjects.append(mark)
total = sum(subjects)
average = total / 5
percentage = (total / 500) * 100
print(f"Total: {total}, Average: {average:.2f}, Percentage: {percentage:.2f}%")

#440.
C = float(input("Enter Celsius: "))
F = (C * 9/5) + 32
print(f"{C}°C = {F}°F")

#441.
n = float(input("Enter number: "))
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")

#442.
ch = input("Enter a character: ")
if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
    print("alphabet")
else:
    print("not alphabet")

#443.
balance = 10000
withdraw = float(input("Enter withdrawal amount: "))
if withdraw > balance:
    print("insufficient funds")
else:
    balance -= withdraw
    print(f"Withdrawal successful. New balance: {balance}")

#444.
password = input("Enter password: ")
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "!@#$%^&*()" for c in password)
long_enough = len(password) >= 8

if long_enough and has_upper and has_digit and has_special:
    print("strong password")
elif long_enough and (has_upper or has_digit):
    print("medium password")
else:
    print("weak password")

#445. False. chained comparison 10 > 5 > 3 > 20 means 10>5 and 5>3 and 3>20.
# 3>20 is False so the whole chain is False.
print(bool(10 > 5 > 3 > 20))  # False

#446.
s = input("Enter a string: ")
print(len(s) > 5 and 'a' in s and 'z' not in s)

#447.
username = input("Username: ")
password = input("Password: ")
if username == "admin" and password == "1234":
    print("login successful")
else:
    print("invalid credentials")

#448.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"{'Addition:':<20} {a + b}")
print(f"{'Subtraction:':<20} {a - b}")
print(f"{'Multiplication:':<20} {a * b}")
print(f"{'Division:':<20} {a / b if b != 0 else 'undefined'}")
print(f"{'Floor Division:':<20} {a // b if b != 0 else 'undefined'}")
print(f"{'Modulus:':<20} {a % b if b != 0 else 'undefined'}")
print(f"{'a > b:':<20} {a > b}")
print(f"{'a == b:':<20} {a == b}")
print(f"{'a < b:':<20} {a < b}")

#449.
item1_price = float(input("Item 1 price: "))
item1_qty   = int(input("Item 1 quantity: "))
item2_price = float(input("Item 2 price: "))
item2_qty   = int(input("Item 2 quantity: "))
item3_price = float(input("Item 3 price: "))
item3_qty   = int(input("Item 3 quantity: "))

subtotal = (item1_price * item1_qty) + (item2_price * item2_qty) + (item3_price * item3_qty)
tax = subtotal * 0.10 if subtotal > 5000 else 0
total = subtotal + tax

print(f"Subtotal: {subtotal:.2f}")
print(f"Tax (10%): {tax:.2f}")
print(f"Total: {total:.2f}")

#450.
top_students = ["Kelechi", "Maxwell", "Attah"]

name = input("Enter student name: ")
score1 = float(input("Score 1: "))
score2 = float(input("Score 2: "))
score3 = float(input("Score 3: "))

average = (score1 + score2 + score3) / 3

if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print(f"\nStudent: {name}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
print(f"In top students list: {name in top_students}")