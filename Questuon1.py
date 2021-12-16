#sum of the first n numbers by Ziithe Ewen Hiwa
import time


def NSum(n):

    begin = time.time()
    #Initialise variable sum for the total sum as 0
    sum = 0

    #run loop to sum up the  numbers in the range of 1 to n
    for i in range(1, n+1):
        #add n to total sum
        sum +=i
    
    end = time.time()

    print("\nThe total sum of the first " , n, " numbers is : ", sum)
    print("Runtime of this program is ", end-begin)

#testing with given variable

NSum(10)
NSum(10000)
NSum(1000000)
NSum(1000000000)