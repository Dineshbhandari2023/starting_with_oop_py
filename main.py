class Student:

    def __init__(self, dateofbirth, studentname, courseduration, tuitionfee):

        self.enrollmentId = 0
        self.studentName = ""
        self.dateOfBirth = ""
        self.courseName = ""
        self.dateOfEnrollment = ""
        self.courseDuration = courseduration
        self.tuitionFee = tuitionfee

    def get_enrollmentid(self):
        return self.enrollmentId

    def get_studentname(self):
        return self.studentName

    def get_dateofbirth(self):
        return self.dateOfBirth

    def get_coursename(self):
        return self.courseName

    def get_dateofenrollment(self):
        return self.dateOfEnrollment

    def get_courseduration(self):
        return self.courseDuration

    def get_tuitionfee(self):
        return self.tuitionFee

    def set_coursename(self, coursename):
        coursename = self.courseName
        return coursename

    def set_enrollmentid(self, enrollmentid):
        enrollmentid = self.enrollmentId
        return enrollmentid

    def set_dateofenrollment(self, dateofenrollment):
        dateofenrollment = self.dateOfEnrollment
        return  dateofenrollment

    def display(self):
        if self.enrollmentId == 0 or not self.dateOfBirth or not self.courseName or not self.studentName or not self.dateOfEnrollment or self.courseDuration == 0:
            print("Unable to display, fill in all the parameters!")
        else:
            print("Enrollment ID:", self.enrollmentId)
            print("Date of Birth:", self.dateOfBirth)
            print("Course Name:", self.courseName)
            print("Student Name:", self.studentName)
            print("Years of Enrollment:", self.dateOfEnrollment)
            print("Course Duration:", self.courseDuration)
            print("Tuition Fee: $", self.tuitionFee)


class Regular(Student):

    def __init__(self, enrollmentid, dateofbirth, coursename, studentname, dateofenrollement, courseduration, tuitionfee, numofmodules, numofcredithours, dayspresent):

        self.numOfModules = numofmodules
        self.numOfCreditHours = numofcredithours
        self.daysPresent = dayspresent
        self.isGrantedScholarship = bool


        super().__init__(self, dateofbirth, studentname, courseduration, tuitionfee)
        self.set_coursename(coursename)
        self.set_enrollmentid(enrollmentid)
        self.set_dateofenrollment(dateofenrollement)

        
        
