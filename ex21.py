def add(a, b):
2 print(f"ADDING {a} + {b}")
3 return a + b
4
5 def subtract(a, b):
6 print(f"SUBTRACTING {a} - {b}")
7 return a - b
8
9 def multiply(a, b):
10 print(f"MULTIPLYING {a} * {b}")
11 return a * b
12
13 def divide(a, b):
14 print(f"DIVIDING {a} / {b}")
15 return a / b
16
17
18 print("Let's do some math with just functions!")
19
20 age = add(30, 5)
21 height = subtract(78, 4)
22 weight = multiply(90, 2)
23 iq = divide(100, 2)
24
25 print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
26
27
28 # A puzzle for the extra credit, type it in anyway.
29 print("Here is a puzzle.")
30
31 what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
32
33 print("That becomes: ", what, "Can you do it by hand?")
