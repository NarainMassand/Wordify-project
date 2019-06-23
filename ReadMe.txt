The project aims to wordify or de-wordify an entered phone number depending
upon its type and user task selection. For faster computation, the approach of
converting the English dictionary provided by the ‘NLTK’ library to
corresponding numbers using keypad mapping and then using the converted
dictionary for different task proves out to be efficient.

The project file wordify_proj.py has 3 major functions which can be used to
perform corresponding tasks:
1. number_to_words()
   Runs when user selects option 1 in the menu. It accepts a string with
   numbers and ‘-‘s and uses the dictionary converted to numbers to find the
   longest sub-number present in the entered number and replaces it with
   corresponding word to return a string with a word or numbers and word that
   replaces whole or part of it. The function just places 1 word in the phone
   number. Any other input other than numbers and ‘-‘’s are considered invalid
   and will take the user back to the menu.

2. words_to_number()
   Runs when the user selects option 2 in the menu. It accepts a string with
   numbers, alphabet and ‘-‘’s. Any other character other than these are
   considered invalid and the user will be taken back to the menu. The alphabet
   in the string are then converted to corresponding numbers using keypad
   mapping and the non-alphabet stay as they were resulting in a string with
   just numbers and ‘-‘’s.

3. all_wordifications()
   Runs when the user selects option 3 in the menu. It accepts a string with
   numbers and ‘-’’s and uses the dictionary converted to numbers list to find
   all of those which are a substring for the entered number and if found in
   the number, replaces them with corresponding words giving out all the
   possible English words in a given number.

Apart from above functions, Following are other helper functions which make
the program modular and hence coder-friendly.
-> remove_dash()
   Removes ‘-’s from the number to get a continuous string.

-> add_dash()
   Adds the ‘-‘s back to the final output in previous locations without
   breaking a word.

-> findnum()
   Takes in a character and returns the corresponding number using keypad
   mapping.

-> dictionary_to_nums()
   Converts the dictionary to numbers in the starting of the run and saves a
   lot of computation time.

-> user_interface()
   Displays the menu and takes input from the user for the action to be
   performed. Accordingly, takes number or words as input and displays the
   output.
   Menu:
   1. Convert a number to wordified form
   2. Convert a wordified form to corresponding number
   3. Get all the possible wordified forms of a phone number
   4. Quit
   Use option 4. to exit the program.

Return Values:
-> The functions return -1 if the input is invalid.
-> all_wordifications and number_to_words functions return -2 if no words are
   found for the input number.

Assumptions:
-> All the words that replace numbers come from an English dictionary from a
   python library. It is assumed to be a credible source.
-> The default length of words in the given program is taken to be 2 or more
   but it is adjustable.
-> It is assumed that a user gives in a fit input otherwise the function
   terminates and user has to start from the menu agains.
-> While ‘-‘ is placed back in result, it isn’t inserted between a word or
   after that.
-> The fitness for function 1 is decided by placing the longest possible
   string in the number.
-> If a number has to be converted to words, it won’t accept any string
   containing alphabet already.

Limitations:
-> To get all wordifications for a number using all_wordifications function,
   the minimum length of number should be 2 and maximum can be 12. However,
   these parameters can be modified in the function.

Test Setup
The file test_wordify_proj.py is used to test number_to_words() function and
words_to_number() function using unittest library. The input values for the
test scenarios were chosen for positive, negative and no output. Invalid input
yeilds -1 and no output (no words found) yeilds -2. The test scenario is said
to be passed if the output matches the expected value provided.

Reference: http://pythontesting.net/framework/unittest/unittest-introduction/

Pre-requisites:
-> NLTK python library
-> Unittest library

Steps to install and use NLTK Library:
^^ Open python in command line or whichever IDE you are using and type the
   following commands:
   -> Import nltk
   -> Nltk.download()
   -> Depending upon your IDE, one of this will happen
      ** A dialogue box appears, Select the Corpora tab and look for
         identifier ‘words’ and install that particular file.
      OR
      ** A menu will come up with an option of download and so on.
      ** Select Download and put in ‘words’ as the identifier when it asks for
         it.
      ** Install it and quit

^^ For this particular project, we just need the word list from nltk library.

Once this is done, the program is all set to run.

Use whatever IDE you are comfortable with. I did run it in a few different
software’s and the implementation was smooth.

Enjoy unraveling the hidden words in your number!
