def main():
 students = []
 courses = []
 marks = {}
def input_students():
    n = int(input("Enter the number of students: "))
    for _ in range(n):
        s_id = input("ID:")
        name = input("Name:")
        dob  = input("Day of birth:")
        students.append({'id':s_id , 'name':name , 'dob' : dob})
        return students

def input_courses():
    n = int(input("Enter the number of courses:"))
    for _ in range(n) :
        c_id = input("Course ID:")
        name = input("Course name:")
        courses.append({'course id':c_id , 'course name':name})
        return courses

def input_marks(courses, students , marks) :
    c_id = input("Enter course ID to enter marks:")
    if any(c['id'] == c_id for c in courses):
        for s in students:
            score = float(input(f"Enter mark for {s['name']} (ID: {s['id']}): "))
            marks[(c_id, s['id'])] = score
    else:
        print("Course ID does not exist!")
def list_courses(courses):
    print("\n--- COURSES LIST ---")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

def show_marks(students, marks):
    course_id = input("Enter course ID to view marks: ")
    print(f"\n--- MARKSHEET FOR COURSE {course_id} ---")
    for s in students:
        score = marks.get((course_id, s['id']), "N/A")
        print(f"ID: {s['id']} | Name: {s['name']} | Mark: {score}")
main()






