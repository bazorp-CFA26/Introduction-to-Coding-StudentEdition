Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> age = int(input("Enter your age: "))
... print("Next year you will be", age + 1)
SyntaxError: multiple statements found while compiling a single statement
>>> age = int(input("Enter your age: "))
... 
Enter your age: 2
>>> print("Next year you will be", age + 1)
Next year you will be 3
