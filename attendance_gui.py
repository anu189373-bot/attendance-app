students = ["Anusha","Rahul","Nuthana","Appu"]
attendance = {}
for student in students:
    status = input(f" {student} (P=Present,A=Absent): ").upper()
    if status == "P":
        attendance[student] = "Present"
    else:
        attendance[student] = "Absent"

print("\nToday's Attendance")
print("-" * 25)
for name, status in attendance.items():
    print(f"{name}: {status}")
