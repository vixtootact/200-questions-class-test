# VARIABLES - Advanced Practical (201-230)

#201.
user_name = input("Enter your name: ")
print(user_name.upper())

#202. it raises a NameError because x was deleted before print() was called.

#203.
a = 10
b = "10"
# print(a + b)  # raises TypeError: unsupported operand type(s) for +: 'int' and 'str'
# you cannot add int and str directly. Python does not auto-convert types.
# fix:
print(a + int(b))   # 20
print(str(a) + b)   # "1010"

#204.
a = "Python"
b = "Java"
a, b = b, a
print(a, b)  # Java Python

#205. 30

#206.
x = 50
print(id(x))

#207.
first = "Attah"
last = "Maxwell"
full_name = f"{first} {last}"
print(full_name)

#208.
# __name  valid  (double underscore prefix is allowed)
# _age    valid  (single underscore prefix is allowed)
# age_    valid  (underscore suffix is allowed)
# age2    valid  (letters followed by number is allowed)
# 2age    INVALID (cannot start with a number)

#209. 20
# x = 5
# x = 5 + 5 = 10
# x = 10 + 10 = 20

#210.
count = 0
for i in range(10):
    count += 1
print(count)  # 10

#211. Python uses dynamic typing. the interpreter assigns the type automatically
#     at runtime based on the value given. this means you don't declare int x or
#     str name like in Java or C. the variable just stores whatever value you give it.

#212.
data = [1, 2, 3]
data2 = data
data2[0] = 99
print(data)   # [99, 2, 3]
# data is also changed because data2 = data does not create a copy.
# both variables point to the same list object in memory.

#213.
data = [1, 2, 3]
data2 = data.copy()
data2[0] = 99
print(data)   # [1, 2, 3]  (unchanged)
print(data2)  # [99, 2, 3]

#214.
student1 = "Kelechi"
student2 = "Maxwell"
student3 = "Attah"
print([student1, student2, student3])

#215. globals() returns a dict of all variables in the global scope.
#     locals() returns a dict of all variables in the current local scope.
#     inside a function, locals() shows only that function's variables.

#216.
student_maths_score_2024 = 85

#217. yes it is valid. Python evaluates the condition and prints accordingly.
x = 10
y = 20
print(x, y) if x > y else print(y, x)  # 20 10

#218.
a = 10
b = 20
result = a if a > b else b
print(result)  # 20

#219. yes, Python 3 allows unicode identifiers including some emoji as variable names.
# 🎯 = 10  is technically valid in Python 3 but strongly discouraged by convention.

#220. _ is used to ignore values you do not need during unpacking.
my_list = [1, 2, 3, 4, 5]
a, _, c, _, e = my_list
print(a, c, e)  # 1 3 5

#221.
price = 19.99
qty = 3
total = price * qty
print(total)  # 59.97

#222.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name, age)

#223. there is no difference in result. x = 10 stores the integer 10 directly.
#     x = int(10) calls int() on an already-integer value, giving the same result.
#     int() is only useful when converting from another type like str or float.

#224.
is_logged_in = False
is_logged_in = not is_logged_in
print(is_logged_in)  # True

#225. True

#226.
x = 10  # global x
def my_func():
    x = 5  # local x
    print("inside function:", x)
my_func()
print("outside function:", x)

#227. write the variable name in UPPER_CASE by convention.
#     Python has no real constant enforcement but UPPER_CASE signals to other
#     developers that this value should not be changed.
MAX_SCORE = 100

#228.
text = "NOUN"
length = len(text)
print(length)  # 4

#229. Kelechi Noun

#230.
# file_path = "C:\new\folder"
# \n is interpreted as a newline character so the path breaks.
# fix using a raw string with r prefix:
file_path = r"C:\new\folder"
print(file_path)  # C:\new\folder


# DATA TYPES - Logic & Bug Finding (231-270)

#231. float. because / always returns float in Python 3, even if result is whole number.
print(type(1/2))   # <class 'float'>

#232. int. // is floor division and always returns int when both operands are int.
print(type(2//2))  # <class 'int'>

#233. no. "True" is a string. True is a boolean.
#     type("True") is str. type(True) is bool.
#     "True" == True gives False.

#234.
print(int(True))   # 1
print(int(False))  # 0

#235. "TrueFalse"

#236. True. because bool() of any non-empty string is True.
#     "False" is a non-empty string so Python sees it as truthy, not the boolean False.

#237.
s = ""
# method 1:
print(len(s) == 0)
# method 2:
print(not s)

#238.
s = " python is easy "
result = s.strip().upper().replace("EASY", "POWERFUL")
print(result)  # PYTHON IS POWERFUL

#239. it raises an IndexError: string index out of range.
#     index 100 does not exist in a 6-character string.

#240. "ython". no error. slicing never raises IndexError even if the end is out of range.
#     Python just returns as far as the string goes.

#241. immutable means the object cannot be changed after creation.
#     no. "python"[0] = "P" raises TypeError: 'str' object does not support item assignment.

#242.
s = "python"
print(s[::-1])  # nohtyp

#243.
print(len(" "))  # 1 (one space character)
print(len(""))   # 0 (empty string)

#244.
age = "20"
print(int(age) + 5)  # 25

#245. list("abc") splits the string into individual characters: ['a', 'b', 'c']
#     ["abc"] creates a list with one item which is the whole string: ['abc']

#246. [1, 2, 3, 1, 2, 3]
print([1, 2, 3] * 2)

#247. (1, 2, 3, 1, 2, 3)
print((1, 2, 3) * 2)

#248. it will not work. dicts do not support the * operator.
#     it raises TypeError: unsupported operand type(s) for *: 'dict' and 'int'.

#249.
# dict cannot have list as key because lists are mutable and unhashable.
# d = {[1,2]: "value"}  raises TypeError

# dict CAN have tuple as key because tuples are immutable and hashable.
d = {(1, 2): "value"}
print(d)  # {(1, 2): 'value'}

#250. {1, 2, 3}
print(set([1, 1, 2, 2, 3]))

#251. add(). sets use add() not append().
my_set = {1, 2}
my_set.add(3)
print(my_set)

#252. append(). lists use append() not add().
my_list = [1, 2]
my_list.append(3)
print(my_list)

#253. the common mistake is that append() returns None.
#     so if you write: my_list = [1,2,3].append(4) then my_list is None.
my_list = [1, 2, 3]
my_list.append(4)   # correct way: call append separately
print(my_list)      # [1, 2, 3, 4]

#254. [1, 2]
# b = [3,4] gives b a completely new list object. it does not change a.
# this is different from b[0] = 99 which would mutate the shared object.
a = [1, 2]
b = a
b = [3, 4]
print(a)  # [1, 2]

#255.
t = (1, 2, 3)
lst = list(t)
lst.append(4)
t = tuple(lst)
print(t)  # (1, 2, 3, 4)

#256.
d = {"name": "Max", "dept": "NOUN"}
print(d.keys())    # dict_keys(['name', 'dept'])
print(d.values())  # dict_values(['Max', 'NOUN'])

#257. isinstance([1,2], list) is better. it returns True even for subclasses.
#     type([1,2]) == list is strict and only matches the exact type.
print(isinstance([1, 2], list))       # True
print(type([1, 2]) == list)           # True

#258. None is used to represent the absence of a value.
#     practical use 1: default function return value when nothing is returned.
#     practical use 2: initializing a variable before you know its value.
result = None

#259.
print(float("inf"))        # inf
print(type(float("inf")))  # <class 'float'>

#260. 2
print(int(True) + int(False) + int(True))  # 1 + 0 + 1 = 2

#261.
x = 10.5
if isinstance(x, int):
    print("int")
elif isinstance(x, float):
    print("float")
else:
    print("other")

#262.
# shallow copy: copies the outer object but inner objects are still shared.
# use when your list has no nested objects.
import copy
a = [1, 2, 3]
b = a.copy()         # shallow copy

# deep copy: copies everything including all nested objects. fully independent.
# use when your list contains other lists or dicts inside.
c = [[1, 2], [3, 4]]
d = copy.deepcopy(c)  # deep copy

#263. 5.0
a = "5"
b = int(a)    # 5
c = float(b)  # 5.0
print(c)

#264.
mixed_list = [42, 3.14, "hello", True, None]
print(mixed_list)

#265. True. bool([0]) is True because the list itself is not empty.
#     it has one item (which happens to be 0) but Python only checks if the
#     container is empty, not what is inside it. only bool([]) is False.

#266. bytes is an immutable sequence of integers from 0-255 representing raw byte data.
#     bytearray is the mutable version of bytes that you can change after creation.

#267.
print(str(123))     # "123"
print(float("123")) # 123.0

#268.
x = ["a", "b", "c"]
print(x[0][1])  # 'b' — no wait:
# x[0] is "a", then "a"[1] is... wait, "a" only has index 0.
# actually raises IndexError: string index out of range
# x[0] = "a", which is a single character. "a"[1] is out of range.

#269. complex(2, 3) creates the complex number 2+3j.
print(complex(2, 3))        # (2+3j)
print(type(complex(2, 3)))  # <class 'complex'>

#270.
value = input("Enter a value: ")
try:
    value = int(value)
    print("type: int, value:", value)
except ValueError:
    print("type: str, value:", value)


# OPERATORS - Calculation & Logic (271-300)

#271. 8
# ** is right-associative so 2 ** 3 ** 2 = 2 ** (3**2) = 2 ** 9 = 512
# but 2 * 3 * 2 is just left-to-right multiplication: 2*3 = 6, 6*2 = 12
# wait — the question writes 2 * 3 * 2 which is 12, not 8.
print(2 * 3 * 2)  # 12

#272. -9. because -3 ** 2 is evaluated as -(3**2) = -9.
#     Python applies ** before the unary minus sign.
print(-3 ** 2)    # -9

#273. 9. because (-3) ** 2 means (-3) squared = 9.
#     the parentheses force the minus into the base.
print((-3) ** 2)  # 9

#274.
# 10 + 3 * 2 ** 2 (reading * as multiply and ** as exponent)
# step 1: 2 ** 2 = 4
# step 2: 3 * 4  = 12
# step 3: 10 + 12 = 22
print(10 + 3 * 2 ** 2)  # 22

#275.
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.2f}")

#276.
x = 15
print(10 < x < 20)  # True

#277. False. all three conditions must be True for and. 15 == 20 is False.

#278. True. or only needs one condition to be True. 5 == 5 is True.

#279. False. 5 > 3 is True, not True gives False.

#280.
print(not 0)   # True  (0 is falsy)
print(not 1)   # False (1 is truthy)
print(not "")  # True  (empty string is falsy)

#281. it will NOT error. False and ... short-circuits immediately.
#     when the first operand is False, Python knows the result is already False
#     and does not evaluate the right side. so 10/0 is never reached.
print(False and (1/0))  # False (no ZeroDivisionError)

#282. it will NOT error. True or ... short-circuits immediately.
#     when the first operand is True, Python knows the result is already True
#     and does not evaluate the right side.
print(True or (1/0))   # True (no ZeroDivisionError)

#283.
# for 10:
print(10 % 2 == 0 and 10 % 3 == 0)  # False (10 % 3 is 1 not 0)
# for 15:
print(15 % 2 == 0 and 15 % 3 == 0)  # False (15 % 2 is 1 not 0)

#284.
n = int(input("Enter a number: "))
print(n % 2 == 0)

#285.
n = int(input("Enter a number: "))
print(n % 2 == 0 and n > 10)

#286.
a = 5
a += 2 * 3   # 2*3 = 6, then 5+6 = 11
print(a)     # 11

#287.
x = 10
x //= 3
print(x)  # 3

#288.
x = 2
x *= 3   # x = 6
x *= 2   # x = 12
print(x)  # 12

#289. there is no difference in result. x += 1 is shorthand for x = x + 1.
#     both increase x by 1. += is just shorter to write.

#290. True
print("ab" in "abc" and "d" not in "abc")

#291.
letter = input("Enter a letter: ").lower()
if letter in "python":
    print("letter is in the word python")
else:
    print("letter is not in the word python")

#292.
# a = 1000; b = 1000; a is b  →  False (usually)
# large integers are not cached so Python creates separate objects.

# a = 10; b = 10; a is b  →  True (usually)
# Python caches small integers (-5 to 256) so both variables point to the same object.
a = 10; b = 10
print(a is b)   # True

a = 1000; b = 1000
print(a is b)   # False

#293.
print([] == [])  # True  (same value, both empty)
print([] is [])  # False (different objects in memory)

#294.
x = 5
y = 5
z = 5
print(x == y and y == z)  # True

#295. the walrus operator := assigns and returns a value in one step inside an expression.
my_list = [1, 2, 3]
if (n := len(my_list)) > 2:
    print(f"list is too long: {n} items")

#296.
while (user_input := input("Type something (or 'exit' to quit): ")) != "exit":
    print("you typed:", user_input)
print("exited.")

#297. 2
# 10 in binary: 1010
#  2 in binary: 0010
# AND:          0010  =  2
print(10 & 2)  # 2

#298. 10
# 10 in binary: 1010
#  2 in binary: 0010
# OR:           1010  =  10
print(10 | 2)  # 10

#299.
a = 5
b = 3
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  # 3 5

#300.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, %, //): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Error: cannot divide by zero")
    else:
        print(a / b)
elif op == "%":
    print(a % b)
elif op == "//":
    print(a // b)
else:
    print("invalid operator")