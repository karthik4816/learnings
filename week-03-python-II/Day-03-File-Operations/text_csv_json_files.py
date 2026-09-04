##read
file = open("week-03-python-II/Day-02-Dictionaries-Sets/student.py", "r")

content = file.read()

print(content)

file.close()
##write
file = open("week-03-python-II/Day-02-Dictionaries-Sets/student.py", "w")

file.write("Learning Python")

file.close()

##with-context manager
with open("week-03-python-II/Day-02-Dictionaries-Sets/student.py","r") as file:
    content = file.read()
    print(content)

##line-by-line
with open("D:/521/learnings/week-03-python-II/Day-02-Dictionaries-Sets/student.py", "r") as file:

    for line in file:
        print(line)

##CSV Files(writing)
import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Python", "Git", "Linux"])
    writer.writerow(["Thomas", 85, 90, 78])
    writer.writerow(["Shelby", 92, 88, 95])
    
##Reading CSV
import csv

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

##json-dump(python file -->json file)
import json

student={
    "name":"thomas",
    "age" : 14,
    "color":"blue"
}
with open("student.json","w") as file:
    json.dump(student, file, indent=4)

##json-load(json--->python file)
import json

with open("student.json","w") as file:
    student=json.load(file)
    
print(student)
    