#Calculating the super digit of a number by Ziithe Ewen Hiwa

def digitSum(n):
    #iterate through the digit string, taking each character from the list of the string and summing it up
    return str(sum((int(i) for i in list(n))))

def sup_digit(n):
    #Check if the number is 1 digit first to return same number
    if len(n)<= 1:
        return n
    else:
        #calculate the sum of the number using the sum function
        return sup_digit(digitSum(n))

def superDigit(n,k):
    #run the summation function on string n
    p = digitSum(n)
    #run the super_digit function to ensure concetenation takes place k times
    return sup_digit(str(int(p)*k))



#Testing with example variables

n, k = "148", 3
a, b = "9875", 4

print( "\nThe Super Digit of ", n, " is ", superDigit(n, int(k)))
print( "\nThe Super Digit of ", a, " is ", superDigit(a, int(b)))