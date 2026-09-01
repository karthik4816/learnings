students = {
    "\nThomas": {
        "Python": 85,
        "Git": 90,
        "Linux": 78,
        
    },

    "\nShelby": {
        "Python": 92,
        "Git": 88,
        "Linux": 95
    }
}
for key, value in students.items():
    print(key)
    print(value)
    total = sum(value.values())
    average= total / len(value)
    print("Total:",total)
    print("Average:",average)