# Week 4 Homework Teacher Key

## Problem 1 Solution

```python
score = int(input("Score: "))
print("Result: Pass" if score >= 70 else "Result: Fail")
```

### Problem 2 Solution

```python
age = int(input("Age: "))
if age < 13:
    print("Ticket type: Child")
elif age < 18:
    print("Ticket type: Teen")
else:
    print("Ticket type: Adult")
```

### Problem 3 Solution

```python
temp = int(input("Temperature: "))
rain = input("Raining? (yes/no): ").strip().lower()
if temp < 60 and rain == "yes":
    print("Advice: Wear a jacket and bring an umbrella.")
elif temp < 60:
    print("Advice: Wear a jacket.")
else:
    print("Advice: Light clothing is okay.")
```

### Problem 4 Solution

```python
level = int(input("Level: "))
if level >= 10:
    print("Gate status: Open")
elif level >= 5:
    print("Gate status: Almost")
else:
    print("Gate status: Locked")
```

### Problem 5 Solution

```python
stored = "tiger123"
entered = input("Enter password: ")
print("Access granted" if entered == stored else "Access denied")
```
