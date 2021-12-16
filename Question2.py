#Grading Rounding Process by Ziithe Ewen Hiwa

#pass number of students to be graded as n
def gradingStudents(n):
    #set constraints for n
    if 1<=n<=60:
        #run loop to receive students grades n times
        for i in range(n):
            grade = int(input("Please enter students grade: ").strip())
            #constraint for grades
            if grade > 100:
                print("Grade cannot be more than 100")

            #check if grade is in range for rounding
            elif 38<=grade<=100:
                #round up grade by calculating modulus to find if diff is greater than 3
                diff = grade % 5
                #if modulus is greater than 3, grade will be rounded to nearest 5th
                if diff >= 3:
                    grade = grade + (5 - diff)
            #else, return grade as is, or print new grade
            print("Final grade is: ",grade)
    else:
        print("Cannot grade more than 60 students")
            


gradingStudents(int(input("Please enter the number of students you'd like to grade: ")))