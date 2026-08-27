class StudentProfile:
    platform = "KodNest"
    total_students = 0

    def __init__(self, student_id, name, branch, score):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.__score = score
        StudentProfile.total_students += 1 


    @property
    def score(self):
        return self.__score


    @score.setter
    def score(self, new_score):
        if StudentProfile.is_valid_score(new_score):
            self.__score = new_score
        else:
            print("Invalid score. Score must be between 0 and 100.")


    @staticmethod
    def is_valid_score(score):
        if score >= 0 and score <= 100:
            return True
        return False


    @staticmethod
    def normalize_name(name):
        return name.strip().title()


    def get_placement_status(self):
        if self.__score >= 80 and self.__score <= 100:
            return "Placement Ready"
        elif self.__score >= 60 and self.__score <= 79:
            return "Needs More Practice"
        else:
            return "Not Ready"

    def display_profile(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Branch: {self.branch}")
        print(f"Mock Score: {self.score}")              # goes through the property getter
        print(f"Placement Status: {self.get_placement_status()}")
        print(f"Platform: {StudentProfile.platform}")    # studentprofile is class variable


    @classmethod
    def from_string(cls, data):
        student_id, name, branch, score = data.split(",")   # split "K101,aarav sharma,CSE,85" into 4 parts
        return cls(student_id, name, branch, int(score))  

    @classmethod
    def change_platform(cls, new_platform):
        cls.platform = new_platform     #changing platform name which is a class variable

    @classmethod
    def show_total_students(cls):
        print(f"Total Students: {cls.total_students}")


# List to store all StudentProfile objects created so far
students = []

while True:
    print("\n===== Student Placement Tracker =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Score")
    print("4. Change Platform")
    print("5. Show Total Students")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        data = input("Enter student details (id,name,branch,score): ").strip()
        student_id = data.split(",")[0]   # seeing the id part, before creating the object

        # Loop for existing students to check for a duplicate ID.
        # If we find a match: print error and break out of the loop.
        # If the loop finishes WITHOUT breaking (no duplicate found),
        # the "else" block on the for-loop runs, and we add the student.
        for s in students:
            if s.student_id == student_id:
                print("Student ID already exists.")
                break
        else:
            new_student = StudentProfile.from_string(data)
            students.append(new_student)
            print("Student added successfully.")

    elif choice == "2":
        if len(students) >= 1:
            for s in students:
                print("--------------------")
                s.display_profile()
                print("--------------------")
        else:
            print("No students found.")

    elif choice == "3":
        stud_id = input("Enter Student ID: ").strip()
        new_score = input("Enter New Score: ").strip()

        # Same for-else pattern: search for the student with matching ID.
        # Found -> update their score (through the property, so it gets validated) and break.
        # Not found -> the for-loop's else runs, and we print "Student not found."
        for s in students:
            if s.student_id == stud_id:
                s.score = int(new_score)     # goes through @score.setter, which checks 0-100
                print("Score updated successfully.")
                print(f"Updated Score: {s.score}")
                print(f"Updated Status: {s.get_placement_status()}")
                break
        else:
            print("Student not found.")

    elif choice == "4":
        new_platform = input("Enter the new platform name: ").strip()
        StudentProfile.change_platform(new_platform)   # updates platform for ALL students at once
        print("Platform changed successfully.")

    elif choice == "5":
        StudentProfile.show_total_students()   # uses the class variable counter, not len(students)

    elif choice == "6":
        print("Thank you for using the Student Placement Tracker.")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 6.")