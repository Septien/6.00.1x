Problem set 4.
Implementing two versions of a word game. Files are within the wordgame folder.

-Problem 1.
implement some code that allows us to calculate the score for a single word. The 
function getWordScore should accept as input a string of lowercase letters (a word) 
and return the integer score for that word, using the game's scoring rules. 

Scoring

        The score for the hand is the sum of the scores for each word formed.

        The score for a word is the sum of the points for letters in the word, 
        multiplied by the length of the word, plus 50 points if all n letters 
        are used on the first word created.

        Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 
        3, D is worth 2, E is worth 1, and so on. We have defined the dictionary 
        SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble 
        letter value.

        For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, 
        then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that 
        the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!

        As another example, if n=7 and you make the word 'waybill' on the first try, 
        it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, 
        plus an additional 50 point bonus for using all n letters).

-Problem 2.
The player starts with a hand, a set of letters. As the player spells out words, letters 
from this set are used up. For example, the player could start out with the following hand: 
a, q, l, m, u, i, l. The player could choose to spell the word quail . This would leave the 
following letters in the player's hand: l, m. Your task is to implement the function 
updateHand, which takes in two inputs - a hand and a word (string). updateHand uses letters 
from the hand to spell the word, and then returns a copy of the hand, containing only the 
letters remaining.

-Problem 3.
A valid word is in the word list; and it is composed entirely of letters from the current 
hand. Implement the isValidWord function.

-Problem 4.
Implement the function 'calculateHandlen(hand)'. Return the length (number of letters)
in the current hand.

-Problem 5.
Implement the function 'playHand'. In ps4a.py, note that in the function playHand, there 
is a bunch of pseudocode. This pseudocode is provided to help guide you in writing your 
function. Check out the Why Pseudocode? resource to learn more about the What and Why of 
Pseudocode before you start coding your solution.

-Problem 6.
A game consists of playing multiple hands. We need to implement one final function to 
complete our word-game program. Write the code that implements the playGame function. 
You should remove the code that is currently uncommented in the playGame body. Read through 
the specification and make sure you understand what this function accomplishes. For the 
game, you should use the HAND_SIZE constant to determine the number of cards in a hand.
