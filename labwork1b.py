students = []
courses = []
marks = {}

def input_students():
    count = int(input("Enter number of students: "))
    for _ in range(count):
        students.append({"id": input("Student ID: "), "name": input("Name: "), "dob": input("DoB: ")})

def input_courses():
    count = int(input("Enter number of courses: "))
    for _ in range(count):
        cid = input("Course ID: ")
        courses.append({"id": cid, "name": input("Course Name: ")})
        marks[cid] = {}

def input_marks():
    cid = input("Enter Course ID to input marks: ")
    if cid in marks:
        for s in students:
            marks[cid][s['id']] = float(input(f"Mark for {s['name']} (ID: {s['id']}): "))
    else:
        print("Course not found!")

def list_courses():
    print("\n--- List of Courses ---")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

def list_students():
    print("\n--- List of Students ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def show_marks():
    cid = input("Enter Course ID to view marks: ")
    if cid in marks:
        print(f"\n--- Marks for Course: {cid} ---")
        for s in students:
            print(f"{s['name']} (ID: {s['id']}): {marks[cid].get(s['id'], 'N/A')}")
    else:
        print("Course not found!")

if __name__ == "__main__":
    input_students()
    input_courses()
    input_marks()
    list_courses()
    list_students()
    show_marks()