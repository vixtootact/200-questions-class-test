#1. a variable is a container that stores values called data types.
#2. by making a name and assigning it to another value using = operator.
#3. no

#4
age = 25

#5.
name = "Kelechi"

#6. it outputs 5
#7. using type() function
#8. = is an assignment operator, while == is used to check if one value is equal to the other
#9. yes you can
#10. =

#11.
a, b, c = 1, 2, 3

#12. 10 20

#13. 
a = 5
b = 10
a, b = b, a 

#14.
#i. you cant start the variable with a number
#ii. you cant use inbuilt function and method and special python terms to name the variable.
#iii. you cant put spaces in the variable
#iv. you cant use dashes in the variable
#15. my_var
#16. no
#17. a constant is used to store values that need to be permanent.
#    you write it by putting const then =

#18. 
PI = 3.14

##19. it prints 20
##20. del variablename

#21.
school = "Noun"

#22.
is_student = True

#23. invalid syntax

#24.
second_name = "Maxwell"

#25.
pythonclass = "Python"

#26. 
#27.

#28.
x = "Python"; y = "Python"; z = "Python"

#29.

#30.
price = 100
price += 50

#31. 

#32.

#33. ordinary text

#34. it will print x is not defined

#35.
name = "Bobmanuel Victor Tamunotonye "
age = 19
state = " Rivers State"

me = name + str(age) + state

#36. 20
#37. 510
#38. 15
#39. bool
#40. 15
#41. 8
#42. 10
#43. you cant assign multiple variables to one value at once.
#44. JohnDoe
#45. John Doe
#46. make a variable and assign it to input() function.

#47.
name = input("Whats your name?")
print("Hello")

#48. 
#49. 
#50. its used to delete a variable or const
#51. no
#52. 

#53. 
question = "I'm a student"
print(question)

#54. using const
#55. its used when you have 2 words and you want to write both of them without space.
#56. 20 10
#57. the one inside the function
#58. no

#59. if, else, while, for, elif

#60. type() is used to show the type of a variable while 
#isinstance is used to check if x is an instance of a type or a class or subclass.

#61. 
my_list = ["Bob", "christine", "vlad"]

#62. 
data = {
    "name" : "Max",
    "age" : 20
}

#63. it equates x to y to z and finally to 0
#64. unpacking is assigning individual values from an iterable and assignign them to one line.
#65. [1, 2, 3]
#66. using the copy() function
#67. 

#68. 
all_variables = str(age) + name + str(PI) + str(is_student) + second_name + pythonclass + x + y + z + str(age) + state + str(price) + question + str(my_list) + str(data)
print(all_variables)

#69. 

#70.
phone_num = 19012345678
#it should be int because phone numbers don't have decimals.

#71. int, float, str, bool
#72. int, float, compelx
#73. int handles whole numbers while float handles numbers with decimals.
#74. a str is a data type that stores any characters in quotation marks.
#75. bool is a data type that only has True and False values
#76. 10 is an int while 10.5 is a float
#77. int
#78. str
#79. bool
#80. list
#81. tuple
#82. set
#83. dict
#84. 
#85. using the type() function

#86. 
num = 10
string = str(num)

#87. 
string = "10"
num = int(string)

#88. a syntax error

#89. 
floatnum = 10.6
intnum = int(floatnum)
print(intnum)
#it completely removes the decimals.

#90.
num = 0
num = bool(num)
print(num)
#it prints False

#91. it prints True.
#92. it prints False.
#93. 100200
#94. it wont work

#95. using the typle() function, e.g.
tuplee = tuple([1, 2, 3])
print(type(tuplee))

#96. 
#i. s1 = 'Hello'
#ii. s2 = "Hello"
#iii. s3 = """Hello"""

#97. there's not much difference, but double is used when the string contains an apostrophe

#98.
s = """Line one
Line two"""

#99. 6
#100. 'P'

#101. Slicing is extracting a portion of a string. s[0:3] gives "Pyt"
#102. 'n'
#103. it makes every character in upper case. "PYTHON"
#104. it makes every character in lower case. "python"
#105. it's joining strings together. Example:
string_concatenation = "Hello" + "World"

#106. Yes
"Hi" * 3 = "HiHiHi"

#107. It's a formatted string that's used to combine string and 
#variables using f"" to contain it and {} to store the brackets.

#108. 
name = "Max"; age = 20
print(f"My name is {name} and I am {age}")

#109. strip removes spaces in front and behind the variable's value.

#110.
if "python" in "I love python":
    print("True")
else:
    print()

#111. a list is an ordered mutable collecton of values. it's mutable.
#112. it's an ordered, indexed collection. it's immutable.
#113. List uses [] and is mutable while Tuple uses () and is immutable.

#114. it is used to store Key-value pairs: 
{"name": "Max", "age": 20}

#115. it is an unordered collection of unique values: 
{1, 2, 3}

#116. no. sets do not allow duplicate values. they are automatically removed.

#117. yes. a list can hold any mix of data types.
mixed = [1, "hello", True, 3.14]

#118. mutable means it can be changed examples: list, dict. 
#immutable means it cant be changed: str, tuple.
#119. [99, 2]
#120. no. it raises a TypeError because tuples are immutable and cannot be changed.
#121. list
#122. tuple
#123. dict. an empty {} always creates a dict, never a set.

#124.
empty_set = set()

#125.
empty_dict = {}

#126. type([]) gives <class 'list'>. type({}) gives <class 'dict'>

#127. indexing is accessing a single element by its position number.
#     e.g: my_list[0] gets the first item.

#128. 4

#129. bool([]) is False. bool([0]) is True.
#     an empty list is falsy. any list with at least one element is truthy.

#130. bool("") is False. bool(" ") is True.
#     an empty string is falsy. a string with any character including a space is truthy.

#131.
x = 10
print(isinstance(x, int))  # True

#132. complex is a numeric data type for numbers with real and imaginary parts.
c = 3 + 5j
print(type(c))  # <class 'complex'>

#133. all of them at once. a list has no restriction on data types.
everything = [1, "hello", True, None, [1, 2], {"a": 1}]

#134.
converted = set([1, 2, 2, 3])
print(converted)  # {1, 2, 3}
#    duplicates are removed automatically when converting to a set.

#135. NoneType is the type of the None object. type(None) gives <class 'NoneType'>

#136. == checks if values are equal. is checks if both variables point to the same
#     object in memory (same identity/address).

#137.
value = input("Enter a value: ")
print(type(value))  # always <class 'str'> because input() always returns a string.

#138.
a_int    = 10
b_float  = 3.14
c_str    = "hello"
d_bool   = True
e_list   = [1, 2, 3]
f_tuple  = (1, 2, 3)
g_dict   = {"key": 1}
h_set    = {1, 2, 3}

#139. type(True) returns <class 'bool'>.
#     yes, bool is a subclass of int. True == 1 and False == 0.

#140. floats are stored in binary (base-2) and 0.1 and 0.2 have no exact binary
#     representation. the tiny rounding errors accumulate so 0.1 + 0.2 gives
#     0.30000000000000004 instead of 0.3.


# SECTION C: OPERATORS

#141. +, -, *, /, //, %, **

#142. + is addition. e.g: 5 + 3 gives 8
#143. - is subtraction. e.g: 10 - 4 gives 6
#144. * is multiplication. e.g: 4 * 3 gives 12
#145. / is division. e.g: 10 / 3 gives 3.333... it always returns a float.
#146. // is floor division. e.g: 10 // 3 gives 3, it rounds down.
#147. % is modulus and returns the remainder. e.g: 10 % 3 gives 1
#148. ** is exponentiation. e.g: 2 ** 3 gives 8

#149. 3.3333333333333335
#150. 3
#151. 1

#152. Python follows BODMAS so multiplication comes before addition.
#     2 + 3 * 4 gives 14 not 20.

#153. ** is right-associative. 2 ** 3 ** 2 = 2 ** (3**2) = 2 ** 9 = 512

#154.
length = 10
width = 5
area = length * width
print(area)  # 50

#155.
P = 1000
R = 5
T = 2
SI = (P * R * T) / 100
print(SI)  # 100.0

#156. ==, !=, >, <, >=, <=

#157. == checks equality. e.g: 5 == 5 gives True
#158. != checks not equal. e.g: 5 != 3 gives True
#159. > checks greater than, < checks less than. e.g: 10 > 5 gives True
#160. >= checks greater than or equal, <= checks less than or equal. e.g: 5 >= 5 gives True
#161. True (Python compares values across int and float)
#162. False (different types, "5" is str and 5 is int)
#163. True
#164. True (True equals 1 because bool is a subclass of int)
#165. True (False equals 0)

#166. and returns True only if both sides are True.
#     or returns True if at least one side is True.
#     not inverts the boolean value.

#167. False
#168. True
#169. False
#170. True
#171. True

#172. =, +=, -=, *=, /=

#173. += adds and assigns. e.g: x = 5; x += 3 makes x equal 8
#174. -= subtracts and assigns. e.g: x = 10; x -= 4 makes x equal 6
#175. *= multiplies and assigns. e.g: x = 3; x *= 2 makes x equal 6
#176. /= divides and assigns. e.g: x = 10; x /= 2 makes x equal 5.0
#177. x = x + 1
#178. = replaces the value entirely. += adds to the current value.

#179. in checks if a value exists in a sequence. e.g: "a" in "apple" gives True
#180. not in is the opposite of in. e.g: "z" not in "apple" gives True
#181. is checks if two variables point to the exact same object in memory.
#182. == compares values. is compares identity (memory address).
#     two variables can be == without being is.

#183.
list_a = [1, 2]
list_b = [1, 2]
print(list_a == list_b)  # True  (same values)
print(list_a is list_b)  # False (different objects in memory)

#184. True
#185. True
#186. True
#187. in checks keys only when used on a dict.

#188. & is bitwise AND. e.g: 5 & 3 gives 1
#     | is bitwise OR.  e.g: 5 | 3 gives 7
#     both operate on the binary representations of the numbers.

#189. the ternary operator is a one-line conditional expression.
#     a = 10 if x > 5 else 20

#190.
n = 8
result = "Even" if n % 2 == 0 else "Odd"
print(result)

#191. operator chaining lets you write multiple comparisons in one expression.
#     1 < 2 < 3 gives True. it means 1 < 2 and 2 < 3.

#192. 70.0
#     precedence: 20 * 30 = 600, 600 / 10 = 60.0, then 10 + 60.0 = 70.0

#193. using parentheses to force a different evaluation order.
#     (10 + 20) * 30 / 10 gives 90.0

#194.
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Addition:",       a + b)
print("Subtraction:",    a - b)
print("Multiplication:", a * b)
print("Division:",       a / b)
print("Modulus:",        a % b)
print("Floor Division:", a // b)

#195.
age = int(input("Enter age: "))
print(age >= 18)

#196.
n = int(input("Enter number: "))
print(n % 3 == 0 and n % 5 == 0)

#197.
letter = input("Enter a letter: ").lower()
print(letter in "aeiou")

#198.
x = 5
x *= 2
x *= 2
x *= 2
print(x)  # 40

#199. BODMAS stands for Brackets, Orders (exponents), Division, Multiplication,
#     Addition, Subtraction. Python follows this exact order of precedence.
#     e.g: 2 + 3 * 4 gives 14 because * is evaluated before +.

#200.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"Addition:       {a + b}")
print(f"Subtraction:    {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division:       {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus:        {a % b}")
print(f"Exponentiation: {a ** b}")