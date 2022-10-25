#Checks for valid course title
class InvalidCourse(Exception):
    def __str__(self):
        return 'Course not found!'

#Checks for valid instructor name
class InvalidInstructor(Exception):
    def __str__(self):
        return 'Instructor not found!'

#Checks for valid course level
class InvalidLevel(Exception):
    def __str__(self):
        return 'Course level not found!'

#Checks for valid user input option
class InvalidOption(Exception):
    def __str__(self):
        return 'Invalid option. Returning to main...'

#CourseList list class, builds and determines if the user input matches the contents of the list, and returns the matching information 
class CourseList(list):
    def search(self, key, search_criteria):
        matching_courses = []
        if search_criteria == 't':
            for x in self:
                if key in x.title:
                    matching_courses.append(x)
        elif search_criteria == 'i':
            for x in self:
                if key in x.instructor:
                    matching_courses.append(x)
        elif search_criteria == 'l':
            for x in self:
                if key == x.level:
                    matching_courses.append(x)
        return(matching_courses)

#Course object class, builds objects and adds to the CourseList list class
class Course(object):
    all_courses = CourseList()
    def __init__(self, level, course_id, title, instructor):
        self.level = level
        self.course_id = course_id
        self.title = title
        self.instructor = instructor
        Course.all_courses.append(self)

#Online subclass, adds additional information to the Course object
class Online(Course):
    all_courses = CourseList()
    def __init__(self, level, course_id, title, instructor, additional_information):
        super().__init__(level, course_id, title, instructor)
        self.additional_information = additional_information

#OInPerson subclass, adds additional information to the Course object
class InPerson(Course):
    all_courses = CourseList()
    def __init__(self, level, course_id, title, instructor, additional_information):
        super().__init__(level, course_id, title, instructor)
        self.additional_information = additional_information


#Main Class, displays text and takes user input
def main():
    print("--------------------------------")
    print ("Welcome to course database main menu:")
    print("--------------------------------")

    #File opening mechanism, creates either an online or in person course object
    with open ('courses.txt') as x:
        for line in x:
            line_list = line.strip('\n').split(',')
            if line_list[4] == ("Online"):
                Online(line_list[0],line_list[1],line_list[2],line_list[3],line_list[4])
            else:
                InPerson(line_list[0],line_list[1],line_list[2],line_list[3],line_list[4:])
            

    choice = ''
    menu = "\nSearch by course title[t]\nSearch by Instructor[i]\nSearch by Level[l]\nExit[e]:"
 
    while(choice!='e'):
        print (menu)
        choice = input("Enter choice (t/i/l/e): ")

        #Try except block to determine if the user input is valid
        try:
            if choice not in ("t","i","l","e"):
                raise InvalidOption
            if choice == 't':

                #Try except block to determine if the course is valid
                try:

                    #Titles list that is appended to from the courses.txt file, and is checked by the key to determine if the key is in the titles list, if not an exception is raised
                    titles = []
                    key = input("Enter course title: ")
                    with open ('courses.txt') as x:
                        for line in x:
                            line_list = line.strip('\n').split(',')
                            titles.append(line_list[2])
                    if key not in titles:
                        raise InvalidCourse

                    #Calls the search function to return the matching course information if there are no exceptions
                    for x in Course.all_courses.search(key, 't'):
                        if x.additional_information == ("Online"):
                            print("\nLevel #: ",x.level,"\nID: ",x.course_id,"\nTitle: ",x.title,"\nInstructor: ",x.instructor, "\nLocation: ",x.additional_information)
                        else:
                            print("\nLevel #: ",x.level,"\nID: ",x.course_id,"\nTitle: ",x.title,"\nInstructor: ",x.instructor, "\nCampus: ",x.additional_information[0], "\nLocation: ",x.additional_information[1])
                except InvalidCourse as x:
                    print(x)
            elif choice == 'i':

                #Try except block to determine if the instructor is valid
                try:

                    #instructors list that is appended to from the courses.txt file, and is checked by the key to determine if the key is in the instructors list, if not an exception is raised
                    instructors = []
                    key = input("Enter instructor: ")
                    with open ('courses.txt') as x:
                        for line in x:
                            line_list = line.strip('\n').split(',')
                            instructors.append(line_list[3])
                    if key not in instructors:
                        raise InvalidInstructor

                    #Calls the search function to return the matching course information if there are no exceptions
                    for x in Course.all_courses.search(key, 'i'):
                        if x.additional_information == ("Online"):
                            print("\nLevel #: ",x.level,"\nID: ",x.course_id,"\nTitle: ",x.title,"\nInstructor: ",x.instructor, "\nLocation: ",x.additional_information)
                        else:
                            print("\nLevel #: ",x.level,"\nID: ",x.course_id,"\nTitle: ",x.title,"\nInstructor: ",x.instructor, "\nCampus: ",x.additional_information[0], "\nLocation: ",x.additional_information[1])
                except InvalidInstructor as x:
                    print(x)
            elif choice == 'l':

                #Try except block to determine if the level is valid
                try:

                    #levels list that is appended to from the courses.txt file, and is checked by the key to determine if the key is in the levels list, if not an exception is raised
                    levels = []
                    key = input("Enter the level(UG/G): ")
                    with open ('courses.txt') as x:
                        for line in x:
                            line_list = line.strip('\n').split(',')
                            levels.append(line_list[0])
                    if key not in levels:
                        raise InvalidLevel

                    #Calls the search function to return the matching course information if there are no exceptions
                    for x in Course.all_courses.search(key, 'l'):
                        if x.additional_information == ("Online"):
                            print("\nLevel #: ",x.level,"\nID: ",x.course_id,"\nTitle: ",x.title,"\nInstructor: ",x.instructor, "\nLocation: ",x.additional_information)
                        else:
                            print("\nLevel #: ",x.level,"\nID: ",x.course_id,"\nTitle: ",x.title,"\nInstructor: ",x.instructor, "\nCampus: ",x.additional_information[0], "\nLocation: ",x.additional_information[1])
                except InvalidLevel as x:
                    print(x)
            elif choice == 'e':
                print("Exiting the database...")
                break
        except InvalidOption as x:
            print(x)

main()
