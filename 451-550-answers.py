#451.
a = 256; b = 256
print(a is b)  # True  — 256 is within the cached range (-5 to 256)

c = 257; d = 257
print(c is d)  # True in script (Python optimises the whole file at once)

#452.
a = [1, 2]; b = [1, 2]
print(a is b)  # False — two separate list objects in memory
print(a == b)  # True  — same values
print(id(a)==id(b))  # False — different memory addresses

#453. it gives UnboundLocalError: local variable 'x' was referenced before assignment.

#454.
x = 10

def f_global():
    global x
    print(x) 
    x = 20
f_global()

#nonlocal technique
def outer():
    x = 10
    def f_nonlocal():
        nonlocal x
        print(x) 
        x = 20
    f_nonlocal()
    print(x)  
outer()

#455. 20
x = 100
def outer():
    x = 20
    def inner():
        print(x) 
    inner()
outer()

#456. UnboundLocalError

#457.
a = 5
b = 5.0
print(type(a), type(b))  
print(id(a), id(b))  
print(a == b) 
print(a is b)  

#458. [1], [1,2], [1,2,3]
def add(item, L=[]):
    L.append(item)
    return L
print(add(1))  
print(add(2))
print(add(3))  

#459.
def add_fixed(item, L=None):
    if L is None:
        L = []  
    L.append(item)
    return L
print(add_fixed(1))  
print(add_fixed(2))  
print(add_fixed(3))

#460. y=[1,2,3,4], z=[1,2,3]
x = [1, 2, 3]
y = x
z = x.copy()
x.append(4)
print(y, z) 

#461.
import copy
a = [[1, 2], [3, 4]]
b = a.copy()  
c = copy.deepcopy(a) 
a[0][0] = 99
print(b)  
print(c)  

#462. True
a = "hello_world_test_123"
b = "hello_world_test_123"
print(a is b) 

#463. ValueError: too many values to unpack.

#464. b=[2,3,4,5], type is list
a, *b, c = [1, 2, 3, 4, 5, 6]
print(b, type(b)) 

#465. a=1, b=5
a, *_, b = [1, 2, 3, 4, 5]
print(a, b)  

#466. Python 3: SyntaxError — True and False are keywords, they cannot be used as
#variable names.

#467.
t = (1, 2, [3, 4])
try:
    t[2] += [5, 6]
except TypeError as e:
    print(e)  # 'tuple' object does not support item assignment
print(t)  # (1, 2, [3, 4, 5, 6])
#It raises TypeError: tuple object does not support item assignment, 
#but the list is mutated — it becomes [3, 4, 5, 6].

#468.
data = {}
for i in range(1, 101):
    data[f"var{i}"] = i

#469. x=20, y=30
x = 10
y = 20
new_x = y
new_y = x + y
x = new_x
y = new_y
print(x, y)  

#470. yes. n exists outside the if block.
if (n := 10) > 5:
    print(n)  # 10
print(n) 

#471. Python 3: x=10. the loop variable x does not leak out of list comprehensions.
x = 10
result = [x for x in range(5)]
print(x)  # 10 in Python 3 (original x remains)

#472.
a = None
b = None
print(a is b, id(a) == id(b))  # True True

#473. [1]
a = b = []
a.append(1)
print(b)  # [1]

#474.
a, b = [], []
print(a is b)  # False — two separate independent empty lists

#475.
a = 10
b = 20
a ^= b  # a = 10^20 = 30
b ^= a  # b = 20^30 = 10
a ^= b  # a = 30^10 = 20
print(a, b)  # 20 10

#476.
print(type(True), isinstance(True, int), isinstance(True, bool))
print(True + True + True)  # 3  (1+1+1)

#477.
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False
print((0.1 + 0.2) - 0.3)  # 5.551115123125783e-17

#478.
from decimal import Decimal
import math

print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))  # True

print(math.isclose(0.1 + 0.2, 0.3))  # True

#479.
a = float('inf')
b = float('-inf')
print(a > 1000000)  # True
print(a + b)  # nan  (infinity minus infinity is undefined)
print(a - a)  # nan
print(a == a)  # True (inf equals itself)
print(b == b)  # True

#480.
a = float('nan')
print(a == a)  # False (NaN is not equal to anything including itself)
print(a is a)  # True  (same object in memory, identity check)
print(a != a)  # True  (NaN is not equal to itself)
import math
print(math.isnan(a))  # True

#481.
a = "a" * 20
b = "a" * 20
print(a is b)  # True  (short repeated strings often interned)

a = "a" * 1000
b = "a" * 1000
print(a is b)  # False (long strings not interned, separate objects)

#482.
s = "Python"
print(s[100:200])  # ""  (empty string, no error)

#483.
s = "hello"
print(id(s))
s += " world"
print(id(s))  # different — a new string object was created

#484. [[99,0],[99,0],[99,0]]
a = [[0]] * 3
a[0][0] = 99
print(a)  # [[99], [99], [99]]

#485.
a = [[0] for _ in range(3)]  # each [0] is a brand new independent list
a[0][0] = 99
print(a)  # [[99], [0], [0]]

#486.
t = (1, [2, 3], 4)
t[1].append(99)
print(t)  # (1, [2, 3, 99], 4)  — list inside changed, no error

try:
    t[1] += [100, 101]  # extends list first, then tries t[1] = ...
except TypeError as e:
    print(e)
print(t)  # (1, [2, 3, 99, 100, 101], 4) — list changed despite the TypeError

#487.
d = {True: "A", 1: "B", 1.0: "C", False: "D", 0: "E", 0.0: "F"}
print(d, len(d))

#488.
print({1, 2, 3} == {3, 2, 1})  # True  — sets are order-independent
print({1, 2, 3} == {1, 2, 3, 3})  # True  — duplicates don't matter in sets
print({} == set())  # False — {} is dict, set() is set

#489.
print([] == False, "" == False, 0 == False, 0.0 == False, {} == False)

print(bool([]), bool(""), bool(0))  # False False False

#490. TypeError: unhashable type: 'list'

#491.
print(hash(10))  # 10
print(hash(10.0))  # 10  — same hash as int 10 because 10.0 == 10
print(hash((1, 2)))  # some integer (tuples are hashable)

#492.
s = {1, 2, 3}
print({frozenset(s)})  # {frozenset({1, 2, 3})} — frozenset IS hashable

#493.
d = dict(a=1, b=2, c=3)
print(list(d.keys()))  # ['a', 'b', 'c']  — dicts preserve insertion order (Python 3.7+)

d2 = {True: 1, 1.0: 1}
print(d2)  # {True: 1}

#494.
a = "abc"
print(list(a))  # ['a', 'b', 'c']
print(set(a))  # {'a', 'b', 'c'} (order not guaranteed)
print(tuple(a))  # ('a', 'b', 'c')
print(dict.fromkeys(a, 0))  # {'a': 0, 'b': 0, 'c': 0}

#495.
print(bool(complex(0, 0)))  # False (real=0 and imaginary=0)
print(bool(complex(0, 1)))  # True  (imaginary part is non-zero)
print(bool(complex(1, 0)))  # True  (real part is non-zero)

#496.
print(type("abc"[0]))  # <class 'str'>   — single char is still str
print(type("abc"[0:1]))  # <class 'str'>   — slice of str is str
print(type([1,2,3][0]))  # <class 'int'>   — single element from list is the element type
print(type([1,2,3][0:1]))  # <class 'list'>  — slice of list is still list

#497.
s = "hello"
id1 = id(s)
s += "!"
print(id1 == id(s))  # False — new object

t = (1, 2)
id1 = id(t)
t += (3,)
print(id1 == id(t))  # False — new object

lst = [1, 2]
id1 = id(lst)
lst.append(3)
print(id1 == id(lst))  # True — same object mutated

d = {"a": 1}
id1 = id(d)
d["b"] = 2
print(id1 == id(d))  # True

#498.
b = bytearray(b"abc")
b[0] = 100  # 'd' is ASCII 100
print(b)  # bytearray(b'dbc')

#499.
import sys
s = "a" * 1000
t = "a" * 1000
print(s == t, s is t)  # True False — equal values, different objects
print(sys.intern(s) is sys.intern(t))  # True — interning forces same object

#500.
def analyze(x):
    print("value:", x)
    print("type:", type(x))
    print("id:", id(x))
    print("truthy:", bool(x))

    try:
        hash(x)
        print("hashable: True")
    except TypeError:
        print("hashable: False")

analyze([1, 2, 3])
analyze("hello")

#501.
print(2 * 3 * 2)  # 12
print((2*3) * 2)  # 12
print(2 * (3*2))  # 12  — all same, * is left-associative
print(-3 * 2)  # -6
print((-3) * 2)  # -6  — same result

#502.
print(10/3, 10//3, 10%3, divmod(10,3))  # 3.333 3 1 (3,1)
print(-10//3)  # -4   (floor toward negative infinity)
print(-10%3)  # 2    (result takes sign of divisor)
print(10//-3)  # -4   (floor toward negative infinity)
print(10%-3)  # -2   (result takes sign of divisor -3)

#503. Python uses floor division (always rounds toward negative infinity).

#504. Python has no ++ or -- operators.
a = 5
print(+a)  # 5  (unary plus, no change)
print(++a)  # 5  (+(+a) = a)
print(--a)  # 5  (-(-a) = a)

#505.
x = 5
print(1 < x < 10 < 20)  # True  — all conditions true
print(1 < x > 2)  # True  — x>1 and x>2
print(5 == 5.0 == True + 4)  # True  — True+4=5, 5==5.0==5

#506.
print(5 == True)  # False (True == 1 not 5)
print(1 == True)  # True  (True == 1)
print(0 == False)  # True  (False == 0)
print(5 is True)  # False (different objects entirely)
print(1 is True)  # False (1 is int, True is bool — different cached objects)

#507. logical operators return one of the actual values, not necessarily True/False.
print(5 and 10)  # 10
print(0 and 10)  # 0
print([] or 5)  # 5
print("" or "default")  # "default"
print(0 or 10 or 20)  # 10

#508.
value = 0
result = value or 10
print(result)  # 10  — wrong if 0 was intended

result = value if value is not None else 10
print(result)  # 0   — correct

#509.
print(True or False and False)  # True  — reads as True or (False and False)
print((True or False) and False)  # False — brackets change the order

#510.
print(not 5 > 3)  # False — reads as not (5>3) = not True = False
print(not (5 > 3))  # False — same
print(not True == False)  # True  — reads as not (True == False) = not False = True

#511.
a = 1000
b = 1000
print(a == b)  # True
print(a is b)  # False (large ints not cached, separate objects)
import sys
print(sys.getrefcount(a))  # 2 or more (one for a, one for getrefcount arg)

#512.
a = []
b = []
print(a is b)  # False — two separate list objects
print(a == b)  # True  — both empty, same value
print(a is not b)  # True

#513.
print(1 in [1, 2, 3])  # True — checks values in list
print(1 in {1: "a"})  # True — checks keys in dict
print("a" in {"a": 1, "b": 2})  # True — checks keys in dict
print(1 in {(1, 2): "a"})  # False — key is tuple (1,2), not int 1

#514. "odd" — because x=5 is odd.
x = 5
print("even" if x%2==0 else "odd" if x==5 else "other")
print("even" if x%2==0 else ("odd" if x==5 else "other"))

#515.
x = -3
result = "negative" if x < 0 else "zero" if x == 0 else "positive even" if x % 2 == 0 else "positive odd"
print(result)

#516.
a = [1, 2, 3, 4, 5]
if (n := len(a)) > 3:
    print(f"Long {n}")  # Long 5
print(n)  # 5 — walrus leaks n into surrounding scope

#517. the code keeps taking input and storing each entry in data list.

#518. manual bitwise calculation for 5 (0101) and 3 (0011):

#519.
print(True & False)  # False — bitwise AND on bools
print(True | False)  # True  — bitwise OR on bools
print(True ^ False)  # True  — bitwise XOR on bools
print(True and False)  # False
print(True or False)  # True
print(5 & 3 == 1)  # False — reads as 5 & (3 == 1) = 5 & False = 5 & 0 = 0 = False
print((5 & 3) == 1)  # True  — correct: (1) == 1

#520.
print("a" * 3)  # "aaa"
print([1] * 3)  # [1, 1, 1]
print([1, 2] * 3)  # [1, 2, 1, 2, 1, 2]
print([1] + [2])  # [1, 2]
print("a" + "b")  # "ab"
print([1]*3 + [2]*2)  # [1, 1, 1, 2, 2]

#521.
a = [1, 2]
print(id(a))
a += [3]  # in-place extend, same object
print(id(a), a)  # same id as before, [1, 2, 3]
a = a + [4]  # creates new list, a points to new object
print(id(a), a)  # different id, [1, 2, 3, 4]

#522. += on list calls __iadd__ which calls extend() in place.
a = [1, 2]
id1 = id(a)
a += [3]
print(id(a) == id1)  # True  — same object
a = a + [4]
print(id(a) == id1)  # False — new object

#523. a=20, b=20
a = 10
b = (a := a + 10)
print(a, b)  # 20 20

#524.
def is_power_of_2(n):
    return n > 0 and (n & (n-1)) == 0

print(is_power_of_2(8))  # True
print(is_power_of_2(7))  # False
print(is_power_of_2(16))  # True

#525.
def is_even(n):
    return (n & 1) == 0

print(is_even(4))  # True
print(is_even(7))  # False

#526.
a = 5
b = 3
a ^= b  # a = 5^3 = 6
b ^= a  # b = 3^6 = 5
a ^= b  # a = 6^5 = 3
print(a, b)  # 3 5

#527.
print(False and 1/0)  # False — short-circuit, 1/0 never evaluated
print(True or 1/0)  # True  — short-circuit, 1/0 never evaluated
try:
    print(True and 1/0)  # ZeroDivisionError — right side IS evaluated
except ZeroDivisionError as e:
    print(e)

#528.
print(None == 0)  # False
print(None == False)  # False
print(None == "")  # False
print(None is None)  # True
try:
    print(None > 0)
except TypeError as e:
    print(e)

#529.
try:
    print([1, "a"] > [1, "b"])  # TypeError in Python 3
except TypeError as e:
    print(e)  # '>' not supported between 'str' and 'str' after matching int

print([1, "a", 2] > [1, "a"])  # True — longer list is greater if prefix matches

#530.
print([] == [])  # True  — same value (both empty)
print(bool([]))  # False — empty list is falsy
print([] is [])  # False — different objects
print(not [])  # True  — not falsy = True
print([[]] == [[]])  # True  — list containing empty list equals same
print(bool([[]]))  # True  — list is not empty (contains one item)

#531.
nested = [[1, 2], [3, 4], [5]]

flat = []
for sublist in nested:
    flat = flat + sublist
print(flat)  # [1, 2, 3, 4, 5]

flat2 = [item for sublist in nested for item in sublist]
print(flat2)  # [1, 2, 3, 4, 5]

#532.
x = 10
result = [y := i * 2 for i in range(5)]
print(y)  # 8 — last assigned value of y is accessible outside

result2 = [i for i in range(5)]

#533.
def simple_calculator(expression):
    parts = expression.split()
    tokens = []
    for p in parts:
        tokens.append(p)

    i = 0
    new_tokens = [tokens[0]]
    i = 1
    while i < len(tokens) - 1:
        op = tokens[i]
        right = float(tokens[i+1])
        if op == "*":
            new_tokens[-1] = str(float(new_tokens[-1]) * right)
            i += 2
        elif op == "/":
            new_tokens[-1] = str(float(new_tokens[-1]) / right)
            i += 2
        else:
            new_tokens.append(op)
            new_tokens.append(tokens[i+1])
            i += 2

    result = float(new_tokens[0])
    i = 1
    while i < len(new_tokens) - 1:
        op = new_tokens[i]
        right = float(new_tokens[i+1])
        if op == "+":
            result += right
        elif op == "-":
            result -= right
        i += 2
    return result

print(simple_calculator("10 + 5 * 2"))  # 20.0

#534.
a = [1]
b = [1]
print(a is b is b)  # False

#535.
print(type(...))  # <class 'ellipsis'>

#536.
print((2).__add__(3))  # 5

#537.
class Num:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return Num(self.value + other.value + 10)
    def __repr__(self):
        return f"Num({self.value})"

a = Num(5)
b = Num(3)
print(a + b)  # Num(18)  — 5+3+10=18

#538.
print(2 * 3 ** 2 + 4 // 2 * 3)  # 24

#539.
def all_same(a, b, c):
    return a == b == c  # chained comparison, cleaner and identical to:

print(all_same(5, 5, 5))  # True
print(all_same(5, 5, 6))  # False

#540. False — the chain stops at 30 < 25 which is False.
x = 5
y = 10
print(x < y < 20 < 30 < 25)

#541. three bugs:

age = int(input("Age: "))  # fix 1: convert to int
if age > 18:
    print("Adult")
else:
    print("Child")  # fix 2: remove + 5

#542. bug: using is instead of ==.
a = [1, 2, 3]
if a == [1, 2, 3]:  # fix: use == for value comparison
    print("Same")

#543. bug: using = (assignment) inside if condition.
x = 5
if x == 10:  # fix: use ==
    print(x)

#544.
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print(is_number("-12.5"))  # True
print(is_number("abc"))  # False
print(is_number("3.14"))  # True

#545.
def count_operators(code):
    operators = ["+", "-", "*", "/", "%"]
    counts = {}

    for op in operators:
        counts[op] = code.count(op)

    return counts

code = "x = 5 + 3 * 2 - 1 / 2 % 3 ** 2 // 1"
print(count_operators(code))

#546.
def custom_in(item, container):
    return item in container

print(custom_in(2, [1, 2, 3]))  # True
print(custom_in(5, [1, 2, 3]))  # False

#547.
def safe_divide(a, b):
    if b == 0:
        return 0
    return a / b

print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # 0

#548.
print(1 == 1 == 1)  # True  — chained: 1==1 and 1==1
print(1 == 1 == 0)  # False — chained: 1==1 and 1==0 = True and False
print((1 == 1) == 0)  # False — (True) == 0 = 1 == 0 = False

#549.
a = 5
b = 10
c = 20
print(a or b and c)  # 5
print((a or b) and c)  # 20
print(a and b or c)  # 10
print(a and (b or c))  # 10

#550.
def type_coercion_calculator(val1, val2, operator):
    def parse(v):
        try:
            return int(v)
        except ValueError:
            try:
                return float(v)
            except ValueError:
                if v.lower() == "true": return True
                if v.lower() == "false": return False
                if v.startswith("["):
                    return list(v.strip("[]").split(","))
                return v

    a = parse(val1)
    b = parse(val2)

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if operator == "+":  return a + b
        if operator == "-":  return a - b
        if operator == "*":  return a * b
        if operator == "/":  return a / b if b != 0 else "undefined"

    if isinstance(a, str) and isinstance(b, str) and operator == "+":
        return a + b

    if isinstance(a, str) and isinstance(b, int) and operator == "*":
        return a * b

    if isinstance(a, list) and isinstance(b, list) and operator == "+":
        return a + b

    return "unsupported operation"

print(type_coercion_calculator("10", "20.5", "+"))  # 30.5
print(type_coercion_calculator("hello", "world", "+"))  # helloworld
print(type_coercion_calculator("ha", "3", "*"))  # hahaha
