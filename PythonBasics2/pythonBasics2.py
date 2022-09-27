# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
 count = 0
 for i in range(0,n):
    if n<3:
      return 0
    if i%3 == 0:
       count = count+1

 return count



# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
   oldCount = 0
   character = ''
   newCount = 0
   for i in range(0,len(s)-1):

    for j in range(i+1,len(s)):
      if s[i] != s[j]:
         i = j
         break
      newCount +=1
      if newCount > oldCount:
        oldCount = newCount
        character = s[i]
   return character
          
   
     



# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
 r = s.strip()
 p = r.lower()
 t = p[0:len(p)//2]
 u = p[len(p)//2+1:len(p)]
 for i in range(0,len(t)):
   if t[0] == u[len(u)-1-i]:
      return True
   else:
      return False
