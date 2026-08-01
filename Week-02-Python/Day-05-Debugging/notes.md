# Day 5 - Debugging

## What is Debugging?

Debugging is the process of finding and fixing errors (bugs) in a program.

Example:

```python
print("Hello World")
```

If the program doesn't work as expected, we debug it to find the problem.

---

# Types of Errors

Python mainly has three types of errors:

1. Syntax Error
2. Runtime Error
3. Logical Error

---

# 1. Syntax Error

A syntax error occurs when Python cannot understand your code.

Example:

```python
print("Hello"
```

Output:

```
SyntaxError: '(' was never closed
```

Correct Code:

```python
print("Hello")
```

---

# 2. Runtime Error

A runtime error occurs while the program is running.

Example:

```python
num = int(input("Enter a number: "))
print(10 / num)
```

Input:

```
0
```

Output:

```
ZeroDivisionError: division by zero
```

Another Example:

```python
print(age)
```

Output:

```
NameError: name 'age' is not defined
```

---

# 3. Logical Error

The program runs successfully, but the output is incorrect.

Wrong:

```python
length = 10
width = 5

area = length + width

print(area)
```

Output:

```
15
```

Correct:

```python
area = length * width

print(area)
```

Output:

```
50
```

---

# Reading Error Messages

Always read the last line of the traceback first.

Example:

```python
numbers = [1, 2, 3]

print(numbers[5])
```

Output:

```
IndexError: list index out of range
```

This tells us we tried to access an index that doesn't exist.

---

# Debugging with print()

One of the easiest ways to debug is by printing variable values.

Example:

```python
a = 10
b = 20

print("a =", a)
print("b =", b)

print(a + b)
```

Output:

```
a = 10
b = 20
30
```

---

# VS Code Debugger

Steps:

1. Open the Python file.
2. Click beside a line number to set a breakpoint.
3. Press **F5**.
4. Check variable values.
5. Use:
   - F10 → Step Over
   - F11 → Step Into
   - F5 → Continue

---

# Common Python Errors

| Error | Meaning |
|--------|---------|
| SyntaxError | Invalid Python syntax |
| NameError | Variable not defined |
| TypeError | Wrong data type used |
| ValueError | Invalid value |
| ZeroDivisionError | Division by zero |
| IndexError | Invalid list index |
| KeyError | Dictionary key not found |
| AttributeError | Object has no attribute |

Example of TypeError:

```python
age = "20"

print(age + 5)
```

Output:

```
TypeError
```

Correct:

```python
age = int(age)

print(age + 5)
```

Output:

```
25
```

---

# Debugging Tips

- Read the error message carefully.
- Check the line number.
- Use `print()` to inspect variables.
- Use breakpoints in VS Code.
- Fix one error at a time.
- Test the program again after each fix.

---

# Summary

 Debugging means finding and fixing bugs.

 Three types of errors:
- Syntax Error
- Runtime Error
- Logical Error

 Useful debugging tools:
- Error messages
- print()
- VS Code Debugger