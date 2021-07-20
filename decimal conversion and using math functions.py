print("you are required to enter any two numeric values of type integer")
num1 = int(input("Enter first numeric value"))
num2 = int(input("Enter seecond numeric value"))

#Now will used pre-defined methematical functions to performe the following 
print("from what what being entered the following are the absolute values")
absoluteNum1 = abs(num1)
print("First Number was:", absoluteNum1)
absoluteNum2 = abs(num2)
print("Second value was:", absoluteNum2)
#Now will show te maximum number between the values 
maximum = max(absoluteNum1,absoluteNum2)
print("The maximum value between the two values is: ", maximum)
#Now will use the power or exponential function to perform the following
power = pow(absoluteNum1,absoluteNum2)
print("The first value raised to the power of the second value is:", power)
print("***************************************************************************")
#Lastly will use the round of function 
print("You are required to enter two decimal numbers and the sum of both numbers are to be rounded off")
dec1 = float(input("Enter first decimal number "))
print(dec1)
dec2 = float(input("Enter second decimal number"))
print(dec2)
print(" ")
print("The following results show the rounded off average of the two decimal numbers ")
theSum = absoluteNum1 + absoluteNum2
average = theSum/2 
final = round(average)
print("The final results are:",final)