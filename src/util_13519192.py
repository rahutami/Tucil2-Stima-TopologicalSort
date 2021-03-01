import course_13519192 as course

# Fungsi untuk mengubah data dari file fileName ke sebuah graph
def getCoursesData(fileName):
    courseData = open(fileName, 'r')

    courseList = []

    for line in courseData:
        courseAndPrereq = []
        courseID = ""
        for c in line:
            if(c == ',' or c == ' ' or c == '.'):
                if(courseID != ''):
                    courseAndPrereq.append(courseID)
                courseID = ""
            else:
                courseID += c

        courses = course.Course(courseAndPrereq)
        courseList.append(courses)
    
    return courseList

# Prosedur untuk mencetak hasil topological sort
def printResult(coursesPlan):
    print("Berikut adalah rencana studi yang bisa Anda ambil:\n")
    for i in range (len(coursesPlan)):
        print("Semester " + str(i+1) + ":")

        for course in coursesPlan[i]:
            print("- " + course)

        print()


def saveResult(fileName, coursesPlan, inputFile):
    saveFile = open(fileName, "w")
    
    saveFile.write("Sumber data: " + inputFile + "\n\n")
    saveFile.write("Berikut adalah rencana studi yang bisa Anda ambil:\n\n")
    for i in range (len(coursesPlan)):
        saveFile.write("Semester " + str(i+1) + ":\n")

        for course in coursesPlan[i]:
            saveFile.write("- " + course + "\n")

        saveFile.write("\n")
    
    saveFile.close()

    print("Rencana studi telah tersimpan.")