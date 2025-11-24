print("===== STUDENT RESULT ANALYZER =====")

# Taking subject names
subjects = input("Enter subject names separated by comma (for example: Maths,Science,Computer): ").split(",")

# Clean subject names (remove extra spaces)
subjects = [s.strip() for s in subjects]

# Number of students
n = int(input("Enter number of students: "))

students = []

# Taking marks for each student
for i in range(n):
    print(f"\n--- Enter data for student {i+1} ---")
    name = input("Name: ")
    marks = []

    for sub in subjects:
        m = float(input(f"Marks in {sub} (out of 100): "))
        # Validation
        if m < 0 or m > 100:
            print("Invalid marks! Enter again (0–100)")
            m = float(input(f"Marks in {sub} (out of 100): "))
        marks.append(m)

    total = sum(marks)
    percent = total / (100 * len(subjects)) * 100

    # Grade calculation
    if percent >= 90:
        grade = "A+"
    elif percent >= 80:
        grade = "A"
    elif percent >= 70:
        grade = "B"
    elif percent >= 60:
        grade = "C"
    elif percent >= 50:
        grade = "D"
    else:
        grade = "F"

    students.append({
        "name": name,
        "marks": marks,
        "total": total,
        "percent": percent,
        "grade": grade
    })

# Printing final result
print("\n===== FINAL RESULT =====")
print("Subjects:", ", ".join(subjects))
print("-" * 70)
print(f"{'Name':<15}{'Total':<10}{'%':<10}{'Grade':<10}")
print("-" * 70)

# Finding topper
topper = None

for s in students:
    print(f"{s['name']:<15}{s['total']:<10.2f}{s['percent']:<10.2f}{s['grade']:<10}")

    if topper is None or s['percent'] > topper['percent']:
        topper = s

print("-" * 70)
print(f"\nClass Topper: {topper['name']}")
print(f"Topper Percentage: {topper['percent']:.2f}")
print(f"Topper Grade: {topper['grade']}")
print("\nProgram completed.")