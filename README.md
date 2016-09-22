Problem set 3.
For this problem, you will implement a variation of the classic wordgame Hangman.
In this problem, the second player will always be the computer, who will be picking 
a word at random.

Note: Problem solved on file Hangman/ps3_hangman.py

Problem 1.
implement the function isWordGuessed that takes in two parameters - a string, 
secretWord, and a list of letters, lettersGuessed. This function returns a boolean - 
True if secretWord has been guessed (ie, all the letters of secretWord are in 
lettersGuessed) and False otherwise.

Problem 2.
Implement the function getGuessedWord that takes in two parameters - a string, 
secretWord, and a list of letters, lettersGuessed. This function returns a string 
that is comprised of letters and underscores, based on what letters in lettersGuessed 
are in secretWord. This shouldn't be too different from isWordGuessed!