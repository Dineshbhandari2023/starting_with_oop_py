# from tkinter import *
#
# root = Tk()
# root.mainloop()
# root.title('Registration Form')
# root.iconbitmap('favicon.ico')


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

        self.dateofenrollment = None
        self.enrollmentid = None
        self.numOfModules = numofmodules
        self.numOfCreditHours = numofcredithours
        self.daysPresent = dayspresent
        self.isGrantedScholarship = bool

        super().__init__(dateofbirth, studentname, courseduration, tuitionfee)
        self.set_coursename(coursename)
        self.set_enrollmentid(enrollmentid)
        self.set_dateofenrollment(dateofenrollement)

    def get_numofmodules(self):
        return self.numOfModules

    def get_numofcreditHours(self):
        return self.numOfCreditHours

    def get_dayspresent(self):
        return self.daysPresent

    def get_isgrantedscholarship(self):
        return self.isGrantedScholarship

    def presentpercentage(self, dayspresent):

        present_percentage = (self.daysPresent / self.courseDuration) * 100

        if 80 <= present_percentage <= 100:
            is_granted_scholarship = True
            print("Grade: A")
        elif 60 <= present_percentage <= 79:
            is_granted_scholarship = False
            print("Grade: B")
        elif 40 <= present_percentage <= 59:
            is_granted_scholarship = False
            print("Grade: C")
        elif 20 <= present_percentage <= 39:
            is_granted_scholarship = False
            print("Grade: D")
        elif 0 <= present_percentage < 20:
            is_granted_scholarship = False
            print("Grade: E")
        else:
            print("Invalid Number")

    def grantcertificate (self,  coursename, enrollmentid, dateofenrollement ):
        print(self.get_studentname() + "has been graduated!")
        print("Course Name: " + self.coursename)
        print("Enrollment ID: " + self.enrollmentid)
        print("Date of Enrollment ID: " + self.dateofenrollment)

        if self.isGrantedScholarship:
            print("The Scholarship has been Granted!!")

    def display(self):
        super().display()
        print("Total number of Modules: " + self.numOfModules)
        print("Total Credit Hours: " + self.numOfCreditHours)
        print("Total num of days present: " + self.daysPresent)

class Dropout(Student):

    def __init__(self, dateofbirth, studentname, courseduration, tuitionfee, numofremainingmodules,
                 numofmonthsattended, dateofdropout, coursename, enrollmentid, dateofenrollement):

        self.numOfRemainingModules = numofremainingmodules
        self.numOfMonthsAttended = numofmonthsattended
        self.dateOfDropout = dateofdropout
        self.remainingAmount = 0
        self.hasPaid = bool

        super().__init__(self, dateofbirth, studentname, courseduration, tuitionfee)
        self.set_coursename(coursename)
        self.set_enrollmentid(enrollmentid)
        self.set_dateofenrollment(dateofenrollement)

    def get_numofremainingmodules(self):
        return self.numOfRemainingModules

    def get_numofmonthsattended(self):
        return self.numOfMonthsAttended

    def get_dateofdropout(self):
        return self.dateOfDropout

    def get_remainingamount(self):
        return self.remainingAmount

    def get_haspaid(self):
        return self.hasPaid

    def billspayable(self):
        self.remainingAmount = (self.courseDuration - self.numOfMonthsAttended) * self.tuitionFee
        self.hasPaid = True








