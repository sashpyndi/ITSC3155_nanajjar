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
 
  multipleOfThrees = {
    "multiple3" : '3',
    "multiple6" : '6',
    "multiple9" : '9'
   }
 
  count = 0
  count2 = 0
  count3 = 0
  for i in range(0, len(n)):
   if n[i] == multipleOfThrees.get("multiple3"):
    count+=1
    
   if n[i] == multipleOfThrees.get("multiple6"):
    count2+=1
    
   if n[i] == multipleOfThrees.get("multiple9"):
    count3+=1
    
  three = int(multipleOfThrees.get("multiple3"))
  six = int(multipleOfThrees.get("multiple6"))
  nine = int(multipleOfThrees.get("multiple9"))
  if count>count2 and count>count3:
     x = three
  if count2>count and count2>count3:
     x = six
  if count3>count2 and count3>count: 
     x = nine
  return x


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  # those 4 lines initiate the variable
  repeatingCharacters = {}
  myList = []
  maximumCount = 0
  char = ''
  # add the number of previous consecutive character 
  for  i in s:
    #checks if the first letter of String s is equal to the previous letter which obviously its not in the first time 
    if char == i: 
      #because they are 2 consecutive characters the repeating characters value is increasing by one.
      repeatingCharacters[i] = repeatingCharacters[i] +1
   #if not consecutive characters, the repeating Characters value is set to one, because there is no consecutive characters
    else:
      repeatingCharacters[i] = 1
    #sets char to the value of i to compare in the next round
    char = i   
    #sets maximum count equal to the repeating characters if it is less than it
    if maximumCount < repeatingCharacters[i]:
      maximumCount = repeatingCharacters[i]
 #for loops that adds the values in the list
  for (key,value) in repeatingCharacters.items():
    #while iterating over the repeatingCharacters dictionary, it checks if the for the value that is equal to the maximum count
    if value == maximumCount:
      # it adds the key to a list
       myList.append(key)
  # it returns the list
  return myList

      

  

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
