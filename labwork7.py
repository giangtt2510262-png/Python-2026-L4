class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def input(self):
        self.__id = input("Enter student ID: ")
        self.__name = input("Enter student name: ")
        self.__dob = input("Enter student DoB (DD/MM/YYYY): ")

    def list(self):
        print(f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob}")


class Course:
    def __init__(self, course_id, name):
        self.__id = course_id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def input(self):
        self.__id = input("Enter course ID: ")
        self.__name = input("Enter course name: ")

    def list(self):
        print(f"Course ID: {self.__id} | Course Name: {self.__name}")


class SchoolManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}  # Format: {course_id: {student_id: mark}}

    def input_students(self):
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            print(f"\n--- Student {len(self.__students) + 1} ---")
            student = Student("", "", "")
            student.input()
            self.__students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            print(f"\n--- Course {len(self.__courses) + 1} ---")
            course = Course("", "")
            course.input()
            self.__courses.append(course)

    def list_students(self):
        if not self.__students:
            print("No students available.")
            return
        print("\n--- Student List ---")
        for student in self.__students:
            student.list()

    def list_courses(self):
        if not self.__courses:
            print("No courses available.")
            return
        print("\n--- Course List ---")
        for course in self.__courses:
            course.list()

    def input_marks(self):
        if not self.__courses or not self.__students:
            print("Please add students and courses first.")
            return

        self.list_courses()
        course_id = input("\nSelect course ID to enter marks: ")
        
        # Verify course exists
        if not any(c.get_id() == course_id for c in self.__courses):
            print("Course ID not found.")
            return

        if course_id not in self.__marks:
            self.__marks[course_id] = {}

        for student in self.__students:
            mark = float(input(f"Enter mark for student {student.get_name()} (ID: {student.get_id()}): "))
            self.__marks[course_id][student.get_id()] = mark

    def show_marks(self):
        self.list_courses()
        course_id = input("\nSelect course ID to view marks: ")

        if course_id not in self.__marks:
            print("No marks recorded for this course.")
            return

        print(f"\n--- Marks for Course {course_id} ---")
        for student in self.__students:
            s_id = student.get_id()
            if s_id in self.__marks[course_id]:
                print(f"Student: {student.get_name()} (ID: {s_id}) -> Mark: {self.__marks[course_id][s_id]}")


def main():
    manager = SchoolManagement()

    while True:
        print("\n" + "=" * 35)
        print(" STUDENT MARK MANAGEMENT SYSTEM ")
        print("=" * 35)
        print("1. Input Students")
        print("2. Input Courses")
        print("3. List Students")
        print("4. List Courses")
        print("5. Input Marks for a Course")
        print("6. Show Marks for a Course")
        print("0. Exit")

        choice = input("Select an option (0-6): ")

        if choice == "1":
            manager.input_students()
        elif choice == "2":
            manager.input_courses()
        elif choice == "3":
            manager.list_students()
        elif choice == "4":
            manager.list_courses()
        elif choice == "5":
            manager.input_marks()
        elif choice == "6":
            manager.show_marks()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()