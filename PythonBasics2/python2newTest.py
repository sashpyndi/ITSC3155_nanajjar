import unittest

import python2new

class TestPythonBasicsTwo(unittest.TestCase):

    def test_count_threes(self):

       self.assertEqual(python2new.count_threes('033'), 3)

       self.assertEqual(python2new.count_threes('9369'), 9)
        
       self.assertEqual(python2new.count_threes('999'), 9)

       self.assertEqual(python2new.count_threes('30669636'), 6)

       self.assertEqual(python2new.count_threes('7542189'), 9)
       


    def test_longest_consecutive_repeating_char(self):

        # Default cases

        self.assertEqual(python2new.longest_consecutive_repeating_char('aaa'), ['a']) 

        self.assertEqual(python2new.longest_consecutive_repeating_char('abba'), ['b']) 

        self.assertEqual(python2new.longest_consecutive_repeating_char('caaddda'), ['d']) 

        self.assertEqual(python2new.longest_consecutive_repeating_char('aaaffftttt'), ['t']) 

        self.assertEqual(python2new.longest_consecutive_repeating_char('aaababbacccca'), ['c']) 

        self.assertEqual(python2new.longest_consecutive_repeating_char('ddabab'), ['d']) 

        self.assertEqual(python2new.longest_consecutive_repeating_char('caac'), ['a']) 

        # Multiple outputs

        self.assertEqual(set(python2new.longest_consecutive_repeating_char('caacc')), set(['a', 'c'])) 

        
        self.assertEqual(set(python2new.longest_consecutive_repeating_char('bbbaaaceeef')), set(['a', 'b', 'e'])) 

        self.assertEqual(set(python2new.longest_consecutive_repeating_char('abcddefgghij')), set(['d', 'g'])) 

        self.assertEqual(set(python2new.longest_consecutive_repeating_char('aabbbccddddefggghhhh')), set(['d', 'h'])) 

    def test_is_palindrome(self):

        self.assertEqual(python2new.is_palindrome("Hello"), False)

        self.assertEqual(python2new.is_palindrome("civic"), True)

        self.assertEqual(python2new.is_palindrome("Civic"), True)

        self.assertEqual(python2new.is_palindrome("Racecar"), True)

        self.assertEqual(python2new.is_palindrome("Dont nod"), True)

        self.assertEqual(python2new.is_palindrome("was it a cat I saw"), True)

        self.assertEqual(python2new.is_palindrome("It was not a cat"), False)

if __name__ == '__main__':

  unittest.main(verbosity=1)