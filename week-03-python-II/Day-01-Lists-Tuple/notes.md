## Day 01 – Lists and Tuples

### Objective

Learn how to create, access, modify, and manipulate lists and tuples using methods, slicing, and comprehensions.

---

# 1. Lists

A **list** is an ordered and mutable collection of items.

### Creating a List

```python
numbers = [10, 20, 30, 40, 50]
names = ["Karthik", "Rahul", "Arun"]
```

A list can contain different data types:

```python
student = ["Karthik", 21, 85.5, True]
```

### Accessing List Elements

List indexing starts from `0`.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])    # 10
print(numbers[2])    # 30
print(numbers[-1])   # 50
```

---

# 2. List Slicing

Slicing is used to extract a portion of a list.

### Syntax

```python
list[start:stop:step]
```

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

The `stop` index is not included.

### More Examples

```python
print(numbers[:3])     # [10, 20, 30]
print(numbers[2:])     # [30, 40, 50]
print(numbers[::2])    # [10, 30, 50]
print(numbers[::-1])   # [50, 40, 30, 20, 10]
```

---

# 3. List Methods

List methods are built-in functions used to modify or work with lists.

### `append()`

Adds an item to the end.

```python
numbers = [10, 20, 30]
numbers.append(40)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

### `insert()`

Adds an item at a specific index.

```python
numbers.insert(1, 15)
```

### `remove()`

Removes the first occurrence of a value.

```python
numbers.remove(20)
```

### `pop()`

Removes and returns an item.

```python
numbers.pop()
```

By default, it removes the last item.

You can also specify an index:

```python
numbers.pop(1)
```

### `sort()`

Sorts the list in ascending order.

```python
numbers.sort()
```

### `reverse()`

Reverses the order of the list.

```python
numbers.reverse()
```

### `index()`

Returns the index of a value.

```python
numbers.index(30)
```

### `count()`

Counts how many times a value occurs.

```python
numbers.count(10)
```

---

# 4. Tuples

A **tuple** is an ordered and immutable collection of items.

### Creating a Tuple

```python
numbers = (10, 20, 30, 40, 50)
```

### Accessing Elements

```python
print(numbers[0])
print(numbers[-1])
```

### Tuple Slicing

Tuples also support slicing.

```python
print(numbers[1:4])
```

Output:

```text
(20, 30, 40)
```

---

# 5. List vs Tuple

| List                     | Tuple               |
| ------------------------ | ------------------- |
| Uses `[]`                | Uses `()`           |
| Mutable                  | Immutable           |
| Can be modified          | Cannot be modified  |
| Has more methods         | Has fewer methods   |
| Used for changeable data | Used for fixed data |

Example:

```python
my_list = [10, 20, 30]
my_list[0] = 100

print(my_list)
```

Output:

```text
[100, 20, 30]
```

But:

```python
my_tuple = (10, 20, 30)
my_tuple[0] = 100
```

This produces an error because tuples are immutable.

---

# 6. List Comprehension

List comprehension provides a short way to create a list.

### Normal `for` Loop

```python
numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)
```

### List Comprehension

```python
numbers = [i for i in range(1, 6)]

print(numbers)
```

Output:

```text
[1, 2, 3, 4, 5]
```

### List Comprehension with an Expression

```python
squares = [i * i for i in range(1, 6)]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

### List Comprehension with a Condition

```python
even_numbers = [i for i in range(1, 11) if i % 2 == 0]

print(even_numbers)
```

Output:

```text
[2, 4, 6, 8, 10]
```

### General Syntax

```python
[expression for item in iterable if condition]
```

---
