#File ini berisi kelas Course
class Course:
    #Parameter
    def __init__(self, courseIDAndPrereqsID): 
        #Parameter constructor-nya adalah list yang berisi courseID dan ID-ID prereqsnya
        #Contoh: [IF2120, MA1101, MA1201]: IF2120 adalah ID mata kulah tersebut dan MA1101 dan MA1201 adalah ID dari prereqs
        self.courseID = courseIDAndPrereqsID[0]
        self.prereqs = courseIDAndPrereqsID[1:len(courseIDAndPrereqsID)]

    #Mengecek apakah suatu mata kuliah dengan ID courseID merupakan prereq dari mata kuliah self
    def hasPrereq (self, courseID):
        for prereq in self.prereqs:
            if courseID == prereq:
                return True
        return False
        
    # Mencetak Info mengenai mata kuliah
    def printInfo(self):
        print("course ID: " + self.courseID)

        if(len(self.prereqs) == 0):
            print("Prereq: none")
        else:
            print("Prereq:")

        for prereq in self.prereqs:
            print("- " + prereq)
        
        print()
