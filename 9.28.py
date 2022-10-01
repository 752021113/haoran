# create class course
class course:
    def __init__(self, name):
        self.name = name
        self.student = []

    def add_student(self,student):
        self.student.append(student)
        return True
    def delete_student(self,student):
        self.student.remove(student)
        return True


    def show_course_name(self):      #display function
        print(self.name)
    def show_course_student(self):      #display function
        for i in self.student:
            print(i.name)



class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_grade(self):
        return self.grade
    def delete_student(self):
        del self

# add course
lst = []
def add_course():
    i=0
    while i<100:                      # could add 100 courses at most
        ans = input("please type the course code you want to add: ")
        if ans == "*" :
            print("finish adding\nthe course are as following")
            for i in lst:
                print(i.name)
            break
        else:
            lst.append(course(ans))
            i = i+1
def delete_course():
    print("the course list: ")
    for i in lst:
        print(i.name)

    while True:
        ans = input("type the course you would delete: ")
        if ans == "*":
            break
        else:
            lst[:] = [course for course in lst if course.name != ans]

    print("delete successfully\nthe remaining list: ")
    for i in lst:
        print(i.name)

# enrol student to course

def contains(list, filter):     #one function from stackflow:https://stackoverflow.com/questions/598398/searching-a-list-of-objects-in-python
    for x in list:
        if filter(x):
            return True
    return False

# need to create a dictionary to save course:student                                                                                                                                     天啊？！你连注释都没删就拷贝过来了吗（code by haorao nie）
course_student = {}
def enrol_student():
    select_course = course(input("select the course: "))
    if contains(lst,lambda x:x.name == select_course.name):
        print(select_course.name + " was chosen")
        while True:
            name = input("enter the student's name: ")
            grade = input("enter the student grade of this course: ")
            if name == "*":
                break
            else:
                s1 = student(name,grade)
                course_student.setdefault(str(select_course.name),[])
                course_student[str(select_course.name)].append(s1)
        print(str(select_course.name) + ' enrolled student: ')
        for i in course_student[str(select_course.name)]:
            print(i.name)

    else:
        return print("error")

# unenrol student to course
def unenroll_student():
    select_course = course(input("select the course: "))
    if str(select_course.name) in course_student:
        print(select_course.name + " was chosen")
        while True:
            n = 1
            for i in course_student[str(select_course.name)]:
                print(str(n) + ': ' + i.name + ' grade is ' + i.grade)
                n = n+1
            x = int(input('enter 999 to quit\nenter student number delete student: '))
            if x == 999:
                break
            else:
                del course_student[str(select_course.name)][x-1]

        print(select_course.name)
        for i in course_student[str(select_course.name)]:
            print('the remaining student: ' + str(i.name) + ": " + str(i.grade))
    else:
        return print("error")

# add student to a list(just a STUDENT list, no connection with course)
lst_student = []
def add_student():
    print('please enter the student information\nenter * to end this function')
    while True:
        student_name = input('please enter the student name')
        if student_name == "*":
            print("end adding\nstudent list: ")
            for i in lst_student:
                print(i.name)
            break
        else:
            s2 = student(student_name, 59)
            lst_student.append(s2)


def delete_student():
    while True:
        ans = input("type the student you would delete: ")
        if ans == "*":
            break
        else:
            lst_student[:] = [student for student in lst_student if student.name != ans]
    print("delete successfully\nthe remaining student list: ")
    for i in lst_student:
        print(i.name)


# test function
# user menu
while True:
    print("choose your identification:\n1.admin\n2.user\n")
    ans = input("please enter your identification: ")
    if ans == '1':
        print("you selected admin")
        ans_2 = input("please choose the function:\n1.add course\n2.delete course\n")
        if ans_2 == '1':
            print("running add course\nenter * to end this function")
            add_course()
        elif ans_2 == '2':
            print("running delete course\nenter * to end this function")
            delete_course()

    elif ans == '2':
        print("you selected teacher")
        while True:
            sec_opt = input("please choose the function:\n"
                         "1.add student\n"
                         "2.delete student\n"
                         "3.add student to one course\n"
                         "4.delete one student from a course\n"
                         "5.quit\n")
            if sec_opt == '1':
                add_student()

            elif sec_opt == '2':
                # while True:
                #     ans = input("type the student you would delete: ")
                #     if ans == "*":
                #         break
                #     else:
                #         lst_student[:] = [student for student in lst_student if student.name != ans]
                # print("delete successfully")
                # for i in lst_student:
                #     print(i.name)
                delete_student()

            elif sec_opt == '3':
                enrol_student()

            elif sec_opt == '4':
                unenroll_student()

            elif sec_opt == '5':
                break
        break
    else:
        print("unknown option selected")

##############################################
# test_course = course("TEST001")
# print(test_course.show_course_name())
#
# s1 = student()
# s2 = student()
#
# test_course.add_student(s1)
# test_course.add_student(s2)
# print(test_course.show_course_student())

