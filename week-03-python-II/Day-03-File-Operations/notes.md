# Week 3 - Day 3: File Operations

Today we move from **temporary data** to **persistent data**.

Variables lose their data when the program ends. Files allow us to save data and use it later.

---

## Topics

* `open()`
* File modes
* `with` context manager
* Reading and writing text files
* CSV files
* JSON files
* `csv` and `json` modules

---

---

# 1. Opening a File

Python uses `open()` to open files.

```python
file = open("notes.txt", "r")
```

Syntax:

```python
open("filename", "mode")
```

---

# 2. File Modes

| Mode  | Meaning           |
| ----- | ----------------- |
| `"r"` | Read              |
| `"w"` | Write / overwrite |
| `"a"` | Append            |
| `"x"` | Create new file   |

Examples:

```python
open("notes.txt", "r")  # Read
open("notes.txt", "w")  # Write
open("notes.txt", "a")  # Append
open("notes.txt", "x")  # Create
```

Important:

`"w"` removes the old content if the file already exists.

---

# 3. Reading a Text File

Suppose `notes.txt` contains:

```text
Python
Git
Linux
```

```python
file = open("notes.txt", "r")

content = file.read()

print(content)

file.close()
```

## `read()`

Reads the entire file.

```python
content = file.read()
```

## `readline()`

Reads one line.

```python
line = file.readline()
```

## `readlines()`

Reads all lines as a list.

```python
lines = file.readlines()
```

---

# 4. Writing to a File

```python
file = open("notes.txt", "w")

file.write("Python\n")
file.write("Git\n")
file.write("Linux\n")

file.close()
```

`\n` means new line.

---

# 5. `with` Context Manager

Instead of manually closing the file:

```python
file.close()
```

use `with`.

```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

Python automatically closes the file.


---

# 6. Append Data

Use `"a"` when you want to add data without deleting existing content.

```python
with open("notes.txt", "a") as file:
    file.write("File Operations\n")
```

If the file contains:

```text
Python
Git
```

It becomes:

```text
Python
Git
File Operations
```

---

# 7. CSV Files

CSV means **Comma-Separated Values**.

Example:

```csv
Name,Python,Git,Linux
Thomas,85,90,78
Shelby,92,88,95
```

CSV is useful for table-like data such as student marks.

## Writing CSV

```python
import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Python", "Git", "Linux"])
    writer.writerow(["Thomas", 85, 90, 78])
    writer.writerow(["Shelby", 92, 88, 95])
```

Important:

```python
newline=""
```

helps prevent unwanted blank lines when writing CSV files.

## Reading CSV

```python
import csv

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```text
['Name', 'Python', 'Git', 'Linux']
['Thomas', '85', '90', '78']
['Shelby', '92', '88', '95']
```

---

# 8. JSON Files

JSON is used to store structured data.

JSON looks similar to a Python dictionary.

```json
{
    "name": "Thomas",
    "age": 21,
    "marks": 85
}
```

Import JSON:

```python
import json
```

---

# 9. Python --> JSON File

Use `json.dump()`.

```python
import json

student = {
    "name": "Thomas",
    "age": 21,
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

Remember:

```text
json.dump() --> Python data to JSON file
```

`indent=4` makes the JSON easier to read.

---

# 10. JSON File --> Python

Use `json.load()`.

```python
import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student)
```

Output:

```python
{'name': 'Thomas', 'age': 21, 'marks': 85}
```

Remember:

```text
json.load() --> JSON file to Python data
```

---


---

# Day 3 Cheat Sheet

```text
open()       --> open a file

"r"          --> read
"w"          --> write / overwrite
"a"          --> append
"x"          --> create

read()       --> read entire file
readline()   --> read one line
readlines()  --> read all lines

write()      --> write text

with         --> automatically closes file

csv.reader() --> read CSV
csv.writer() --> write CSV

json.dump()  --> Python data to JSON file
json.load()  --> JSON file to Python data

json.dumps() --> Python data to JSON string
json.loads() --> JSON string to Python data
```

---

