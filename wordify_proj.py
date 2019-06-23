'''
 wordify_proj.py

 Revision : V1.0

 Last Modified Date    Author

 22-Jun-2019           Narain Massand
'''

# Libraries used in the program
from nltk.corpus import words as words
import re

# Maps the alphabets to corresponding numbers as per the keypad
keypad = [
            ' ',                 #0
            ' ',                 #1
            ('a','b','c'),       #2
            ('d','e','f'),       #3
            ('g','h','i'),       #4
            ('j','k','l'),       #5
            ('m','n','o'),       #6
            ('p','q','r','s'),   #7
            ('t','u','v'),       #8
            ('w','x','y','z')    #9
         ]

'''
function name: remove_dash
Brief Desc: Removes dashes or any unwanted characters from given string and converts it into a num/char/num-char string
Param[in]: to_convert - Number to remove dashes from
Return: no_dash - Number with removed dash
'''
def remove_dash(to_convert):

  only_num_char = []

  for iterate in range(len(to_convert)):
    if True == to_convert[iterate].isdigit() or True == to_convert[iterate].isalpha():
      only_num_char.append(to_convert[iterate])
    else:
      pass

  no_dash = ''.join(str(x) for x in only_num_char)

  return no_dash

'''
function name: add_dash
Brief Desc.: Adds dashes at locations corrsponding to those entered by user
                without breaking the word
Param[in]: User entered Input(to_convert) and generated output without dashes(no_dash)
Return: outputstr - Generated output with dashes(outputstr)
'''
def add_dash(to_convert, no_dash):

  idx_dash = [pos for pos, char in enumerate(to_convert) if '-' == char]
  output = []

  iter_idx = 0

  for iterate in range(len(to_convert)):
    if no_dash[iter_idx].isalpha() and no_dash[iter_idx-1].isalpha():
      output.append(no_dash[-(len(no_dash)-iter_idx):])
      break
    if (iterate in idx_dash):
      output.append('-')
    else:
      output.append(no_dash[iter_idx])
      iter_idx = iter_idx + 1

  outputstr=''.join(str(x) for x in output)

  return outputstr

'''
function name: findnum
Brief Desc.: Takes in an alphabet and returns number according to keypad
Param[in]: char - an alphabet on keypad
Return: num - Number mapped to the alphabet on keypad
'''
def findnum(char):
  for idx,value in enumerate(keypad):
    for alpha in range(len(value)):
      if char == value[alpha]:
        num = idx
  return num

# Used to detect unwanted characters in a string
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

'''
function name: words_to_number
Brief Desc.: Takes in a string (phone number) which contains words and
                replaces the alphabets with corresponding numbers
Param[in]: word_number - string with alphabets and numbers
Return: numstr - string with only numbers
'''
def words_to_number(word_number):

  numlist = []

  no_dash = remove_dash(word_number)
  if (None == regex.search(word_number)):
    for i in range(len(word_number)):
      if '1' == word_number[i]:
        numlist.append('1')
      elif '-' == word_number[i]:
        numlist.append('-')
      elif True == (word_number[i].isalpha()):
        numlist.append(findnum(word_number[i].lower()))
      elif True == (word_number[i].isdigit()):
        numlist.append(word_number[i])

    numstr=''.join(str(x) for x in numlist)

    return numstr

  else:
    return -1

'''
function name: dictionary_to_nums
Brief Desc.: Maps english dictionary into numbers using keypad
Param[in]: NA
Return: all_num_words - all dictionary words in numbers
        all_words - all dictionary words
'''
def dictionary_to_nums():
  all_num_words = []
  all_words = []
  print('\n\nLoading Dictionary...')

  for a_word in words.words():
    if len(a_word) > 12 or 2 > len(a_word):
      continue
    word = a_word.lower()
    phone = words_to_number(word)
    all_num_words.append(phone)
    all_words.append(word)

  return all_num_words, all_words

# Saves time by saving converted dictionary as a list
all_num_words, all_words = dictionary_to_nums()

'''
function name: number_to_words
Brief Desc.: Converts the whole number or part of it to the longest string
Param[in]: number_to_convert - string with numbers
Return: out - string with numbers and alphabets
'''
def number_to_words(number_to_convert):

  no_dash = remove_dash(number_to_convert)

  if True == no_dash.isdigit():

    len_num = len(number_to_convert)
    all_num_words.sort(key = len)
    all_num_words_rev = all_num_words[::-1]
    all_words.sort(key = len)
    all_words_rev = all_words[::-1]

    for i in range(len(all_num_words_rev)):
      if (all_num_words_rev[i] in no_dash):
        out = no_dash.replace(all_num_words_rev[i], all_words_rev[i])
        break
      else:
        pass

    output = add_dash(number_to_convert, out)
    return output.upper()
  else:
    return -1

'''
function name: all_wordifications
Brief Desc.: Takes in a number and returns all variants of it with possible
             english words
Param[in]: main_number - string with numbers
Return: all_possible - string with numbers and alphabets
'''
def all_wordifications(main_number):

  all_possible = []
  output = []

  no_dash = remove_dash(main_number)

  if True == no_dash.isdigit():
    for i in range(len(all_num_words)):
      if all_num_words[i] in no_dash:
        all_possible.append(no_dash.replace(all_num_words[i], all_words[i]))

    for idx in range(len(all_possible)):
      output.append(add_dash(main_number, all_possible[idx].upper()))

    return output

  else:
     return -1

'''
function name: user_interface()
Brief Desc.: Acts as the main module of the program by communicating with
             user about the task performed, corresponding input-output
             operations and function calls
Param[in]: NA
Return: Prints Output or Exits (returns)
'''
def user_interface():

  option = input("\n Select the task to be performed (1-4):\n\
          1. Convert a number to wordified form \n\
          2. Convert a wordified form to corresponding number \n\
          3. Get all the possible wordified forms of a phone number\n\
          4. Quit \n")

  if '1' == option:

    to_convert = input('\nEnter the number to be converted to words : ')

    output = number_to_words(to_convert)

    if -1 == output:
      print('\nInvalid Entry!')

    else:
      print('\nThe Resulting number is : ')
      print(output)


  elif '2' == option:

    to_convert = input('\nEnter the num-word to be converted to number : ')
    output = words_to_number(to_convert)

    if -1 == output:
      print('\nInvalid Entry!')

    else:
      print('\nThe Resulting number is : ')
      print(output)

  elif option == '3':

    to_convert=input('\n Enter the number to be converted into all possible \
word forms possible : ')
    output = all_wordifications(to_convert)

    if -1 == output:
      print('\nInvalid Entry!')

    else:
      print('\nYour Options : ')
      print("\n".join(output))

  elif '4' == option:
    print('\nSee ya later')
    return

  else:
    print('\nInvalid Choice')

if __name__ == '__main__':
    user_interface()
