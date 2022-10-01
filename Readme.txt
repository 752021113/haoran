this document is the README file for 9.28.py

"9.28" is a course enrollment simulation code written by python

the requirement is as follows:

********************************************************************************************************************************
Instructions
Code an Object Oriented "Python" Student and Course Management Program supports the following functionalities:

>Allows Adding/ Modifying/ Deleting Courses (2 Points)
	>>Think of and implement the attributes and actions of a student
>Only the program admin is allowed to do the above operations (1 Point)
>Allows Adding/ Modifying/ Deleting Students (2 Points)
	>>Think of and implement the attributes and actions of a student
>Allows to Enrol and unenroll Students in a Course (3 Points)
>Allows submitting grades for the students (2 Points)


It's not a group assignment; every student should submit the code independently. You can work with your group to discuss the requirements; however, every submission should be unique. 
************************************************************************************************************************************



 menu: 
  1>admin:   could jump to the "add course" function, enter the course code (ex.  GNG5300,ECE1234,CSI****) and which will be saved in one list( lst = [] ). enter * to end this def.
             go back to the identify choose menu
             "delete course" will print all the object(course) in list( lst = [] ) firstly, then enter the course code to delete it, and will print the new course list after deleting(NOTE: the delete course code needs to be in the list, or will ERROR)
  2>user:  1>"add student": enter student name to add them in one list ( lst_student = [] ) (NOTE: the list ( lst_student = [] ) has no connection with any course), enter * to end this def function
           2>"delete student" : enter one name to remove this student from ( lst_student = [] )(NOTE: the removed student need be in the lst_student = [], or will ERROR)
           3>"enrol student" : created dictionary (course_student = {}), key: the course, value: student info (type: class  ex.  peter 88, john 94....),(NOTE: when print: select the course: , the course code entered need to be one course code in lst = [],Put another way need be the course you add in "add course" ),then enter student name and student grade.
           4> "unrnrol studnet": like "enrol student", when "select the course: ", you need to enter the course code already exists or will print: ERROR. Enter 999 to end this function. enter the No. of one student to delete this student(value) from this course(key)
           5>"end": just end...
