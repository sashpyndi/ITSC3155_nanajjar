# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.

# Part A. odd_range
# Define a function odd_range(num1, num2) that takes a starting number (num1) and an ending number (num2)
# and returns all odd numbers as an array between num1 (inclusive) and num2 (exclusive)
def odd_range(num1, num2):
   my_arr = [] 
   my_arr2 = []
   for i in range(num1,num2):
     my_arr.append(i)
   for i in my_arr:
     if i % 2 == 1:
       my_arr2.append(i)
   return my_arr2



# Part B. has_lower_case
# Define a function has_lower_case(s) that takes a string s
# and checks if string s contains a lower case char.
# The function should return True indicating that string s has a lower case char
# otherwise return False
def has_lower_case(s):
  for i in range(0,len(s)):
    if ord(s[i:i+1]) >= ord('a') and ord(s[i:i+1])<= ord('z'):
      return True
   
  return False



# Part C. fizz_buzz
# Define a function fizz_buzz(num) that takes an integer num
# and returns a string based on the following criteria:

# if num is divisible by 3 return "Fizz"
# if num is divisible by 5 return "Buzz"
# if num is divisible by 3 and 5 return "FizzBuzz"

# if num is does not meet any of the above criteria or is less than
# or equal to 0 return the num as a string
def fizz_buzz(num):
  string = ""
  if num<0 or num ==0:
       string = str(num)
  elif num % 5 ==0 and num %3 ==0:
     string ="FizzBuzz"
  elif num % 3 == 0:
     string = "Fizz"
  elif num % 5 == 0:
      string = "Buzz"
  else:
      string = str(num)
  return string