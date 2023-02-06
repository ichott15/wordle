#github.com/ichott15/wordle

from wordle_utils import *
from random import *
import doctest




#define global variables
WORDLE_WORD_LENGTH = 5
MAX_NUM_OF_GUESSES = 6
CHAR_GREEN = '\x1b[6;30;42m'
CHAR_YELLOW = '\x1b[6;30;43m'
CHAR_GRAY = '\x1b[6;30;47m'
CHAR_END = '\x1b[0m'



#checks to see if word inputed is in the list of VALID_WORDS
def is_valid_word(word_input, list_words):
    ''' str, list -> Bool
    This function takes word_input and checks to see if it is in
    the list of valid wordle words
    
    >>> is_valid_word('elder', valid_words)
    True
    
    >>> is_valid_word('tomato', valid_words)
    >>> True
    
    >>> is_valid_word('100', valid_words)
    False
    
    '''
    if word_input in list_words:
        return True
    else:
        return False


#takes a list of strings and prints each strin on a new line
def print_string_list (my_list):
    ''' list -> None
    takes a list of strings and prints each string in the list on a new line.
    
    >>> print_string_list(['abounds', 'about', 'abouts', 'aboveboard', 'abovedeck'])
    abounds
    about
    abouts
    aboveboard
    abovedeck
    
    >>> print_string_list(['a', 'b', 'c', 'd', 'e'])
    a
    b
    c
    d
    e
    
    >>> print_string_list(['im', 'blue', 'da', 'bu', 'de'])
    im
    blue
    da
    bu
    de
    
    '''
    
    for element in my_list:
        print(element)
        
        
#define new color string function

def color_string(word, color):
    ''' string, string -> string
    Takes two strings: a word to be colored, and a color.
    The function should return the “colored” string, meaning,
    it returns a new string where the word to be colored is concatenated in between
    the corresponding ANSI code of the color and CHAR_END.
    The color string can be either 'green', 'yellow' or 'gray'.
    If the color string is none of the above, the function prints 'Invalid color.'
    and returns the original word string (the first parameter).
    
    >>> s = color_string('about', 'green')
    >>> print(s)
    about
    
    >>> color_string('elder', 'yellow')
    '\x1b[6;30;43melder\x1b[0m'
    
    >>> color_string('smile', 'gold')
    Invalid Color
    'smile'
    '''
    #check to see if 'color' is acceptaple color
    if color in ['yellow', 'green', 'gray']:
        if color== 'yellow':
            return str(CHAR_YELLOW+word+CHAR_END)
        elif color == 'green':
            return str(CHAR_GREEN+word+CHAR_END)
        else:
            return str(CHAR_GRAY+word+CHAR_END)
    else:
        print('Invalid color.')
        return word
    
#defining another helper function
def get_all_5_letter_words(my_list):
    ''' list -> list
    Takes a list of strings representing a list of words and returns a new
    list consists of only WORDLE_WORD_LENGTH length words.
    
    >>> get_all_5_letter_words(['abs', 'about', 'abouts', 'above',
    'aboveboard', 'aloft'])
    ['about', 'above', 'aloft']
    
    >>> get_all_5_letter_words(['amazing', 'brother', 'pop', 'out', 'only', 'on'])
    []
    
    >>> get_all_5_letter_words(['woke', 'up', '10005', 'a', 'teety', 'across',
    'my'])
    ['10005', 'teety']
    '''
    new_list= []
    for element in my_list:
        if len(element)== WORDLE_WORD_LENGTH:
            new_list.append(element)
         
    return new_list
        

#define main function that will be used to play wordle

def main():
    ''' () -> None
    takes no parameters and returns nothing.
    The function first loads the list of all words by calling the function
    load_words
    from the wordle_utils module. Then, from that list it filters and keeps only
    5 letter words using helper functions. Then finally it calls the function
    play passing
    as parameter the list of 5 letter words. prints everything that play prints
    because it calls it
    '''
    
    valid_words = get_all_5_letter_words(load_words())

    
    play(valid_words)


# this function chooses a random worlde word
def generate_random_wordle(list_of_strings):
    ''' list -> string
    takes a list of strings as input which represents the list of all words.
    The function picks a random string from the list and returns it.

    
    >>> generate_random_wordle(['potato', 'toe', 'cricket', 'snowboard'])
    'potato'
    
    >>> generate_random_wordle(['about', 'above', 'aloft', 'aeons'])
    'aloft'
    
    >>> generate_random_wordle(['im', 'amazing', 'yeah', 'im', 'all', 'that'])
    'yeah'
    '''
    ran_number=randint(0, (len(list_of_strings)-1))
    return list_of_strings[ran_number]


def input_wordle(string_list):
    ''' list -> string
    takes a list of strings as input which represents the list of all words and
    returns the wordle.
    Asks the user to input a word with the message "Input today's word:
    and checks that it’s a valid word. If it’s not a valid word,
    the function should print 'Not a valid word, please enter a new one.
    and should continue to ask the user until it’s a valid word.
    If the input is valid, then it should get erased from the shell immediately.
    '''
    
    entered_word = input_and_hide("Input today's word: ")
    entered_word =  entered_word.lower()
    
    while entered_word not in string_list:
        print('Not a valid word, please enter a new one.')
        entered_word= input_and_hide("Input today's word: ")
        entered_word =  entered_word.lower()
    
    return entered_word
    
def play(list_of_words):
    ''' list -> None
    takes a list of strings as input which represents the list of all words.
    The function must choose the play mode and get the wordle. Upon getting the
    wordle, it should call
    the function play_with_word with respective parameters,
    and finally it should the print the final message to indicate whether
    the user won
    or lost using the function print_final_message.
    '''
    
    wordle=choose_mode_and_wordle(list_of_words)
    
    guesses = play_with_word(wordle, list_of_words)
    
    print_final_message(guesses, wordle)
    
def choose_mode_and_wordle(list_of_strings):
    ''' list -> string
    takes a list of strings as input which represents the list of all words and
    returns the wordle
    choose_mode_and_wordle() asks the user which mode of playing they would like.
    asks the user to input the mode with the prompt message
    "Enter the number of players: ".
    The user should enter 1 for ’1 player mode’ and 2 for ’2 player mode’.
    If the user’s input is not 1 or 2, then the function should print
    "Wordle can be played with 1 or 2 players.
    Please only enter 1 or 2." and should ask the user to input again.
    If the user chooses the 1 player mode, then the function generates the wordle
    randomly from the given list of words.
    If the user chooses the 2 player mode, then the function prints
    "\n***** Player 1's turn. ***** \n" and ask the Player 1 to input the wordle,
    then print "\n***** Player 2's turn. ***** \n".
    
    >>> choose_mode_and_wordle(valid_words)
    Enter the number of players: 1
    'snaky'
    
    >>> choose_mode_and_wordle(valid_words)
    3
    Wordle can be played with 1 or 2 players. Please only enter 1 or 2.
    2
    'plead'
    
    >>> choose_mode_and_wordle(['about', 'above', 'aloft', 'aeons'])
    Enter the number of players: 2
    ***** Player 1's turn. *****
    
    ***** Player 2's turn. *****
    'aeons'
    
    '''
    
    num_players= int(input("Enter the number of players: "))

    #make sure that the player only inputs one or two players
    
    while num_players not in [1, 2]:
        print("Wordle can be played with 1 or 2 players. Please only enter 1 or 2.")
        num_players=int(input("Enter the number of players: "))

    # then either create wordle

    if num_players ==1:
        worlde= generate_random_wordle(list_of_strings)
        return worlde
    else:
        print("\n***** Player 1's turn. ***** \n")
        wordle = input_wordle(list_of_strings)
        print("\n***** Player 2's turn. ***** \n")
        return wordle
        
def play_with_word( correct_word, string_list):
    ''' string, list -> int
    takes the solution word as string and a list of words as a list of strings.
    The function asks the player to input a guess word with a prompt message
    'Enter a guess:', then colors the guess respective to the solution word.
    After each guess the function prints the colored guesses so far
    using the helper functions.
    The function keeps doing this for at most MAX_NUM_OF_GUESSES times;
    it interrupts early if the player guesses the solution. The
    function returns the number of words the
    player entered to guess the solution. If the player didn’t guess the wordle
    in MAX_NUM_OF_GUESSES tries,
    then return MAX_NUM_OF_GUESSES + 1.
    
    >>> play_with_word('caper', ['cable', 'cater', 'crane', 'carve',
    'caper', 'calls'])
    Enter a guess: crane
    c ra n e
    Enter a guess: carve
    c ra n e
    ca r v e
    Enter a guess: cater
    c ra n e
    ca r v e
    ca t er
    Enter a guess: caper
    c ra n e
    ca r v e
    ca t er
    caper
    4
    
    >>> play_with_word('amaze', 'valid_words')
    Enter a guess: amaze
    amaze
    1
    >>> play_with_word('frame', 'valid_words')
    Enter a guess: crate
    crate
    Enter a guess: frame
    frame
    2
    '''
    # define local variables
    guess_word = input('Enter a guess:')
    guess_word= guess_word.lower()
    
    while not is_valid_word(guess_word, string_list):
        print('Not a valid word, please enter a new one.')
        guess_word=input('Enter a guess:')
        guess_word= guess_word.lower()
    
    guesses=1
    words_to_print=''
    words_to_print+=compare_and_color_word(guess_word, correct_word)

    
    while correct_word != guess_word:
        
        #create a while loop to make sure input is a valid wordle word
        #invalid guesses do not count as 'guesses'
        while not is_valid_word(guess_word, string_list):
            print('Not a valid word, please enter a new one.')
            guess_word=input('Enter a guess:')
            guess_word= guess_word.lower()


        # create loop variable to diplay guesses each time
        if guesses>1:
            words_to_print+= '\n'
            words_to_print+=compare_and_color_word(guess_word, correct_word)
        
        # print wordle guess and ask for another input
        print(words_to_print)
        guess_word=input('Enter a guess:')
        guess_word= guess_word.lower()
    
        # increase loop counter by one

        guesses+=1
        
        #should interrupt if they hit the max nurmber of guesses
        if guesses == MAX_NUM_OF_GUESSES:
            words_to_print+= '\n'
            words_to_print+=compare_and_color_word(guess_word, correct_word)
            print(words_to_print)
            return MAX_NUM_OF_GUESSES+1

        # before entering another guess check to see if word entered is the correct word        
        if guess_word==correct_word:
            print(words_to_print)
            print(compare_and_color_word(guess_word, correct_word))
            return guesses
    
    # this would only work if the max number of guesses is hit
    return guesses

def compare_and_color_word(guess, correct_word):
    ''' string, string -> string
    takes two strings, the first one is the guessed word and the second one
    the solution word.
    The function must compare the guessed word to the solution word letter by
    letter
    and color each letter accordingly. If a letter from the guessed word doesn’t
    appear in the solution, then color it gray. If the letter appears
    in the solution word in the same position then color it green,
    otherwise if it appears but not in the same position color it yellow.
    To color the letters use the helper functions. The function returns
    the colored string.
    
    >>> compare_and_color_word('mount', 'about')
    '\x1b[6;30;47mm\x1b[0m\x1b[6;30;43mo\x1b[0m\x1b[6;30;43mu\x1b[0m\x1b
    [6;30;47mn\x1b[0m\x1b[6;30;42mt\x1b[0m'
   
    >>> compare_and_color_word('crate', 'frame')
    '\x1b[6;30;47mc\x1b[0m\x1b[6;30;42mr\x1b[0m\x1b[6;30;42ma\x1b[0m\x1b
    [6;30;47mt\x1b[0m\x1b[6;30;42me\x1b[0m'
    
    >>> compare_and_color_word('elder', 'elder')
    '\x1b[6;30;42me\x1b[0m\x1b[6;30;42ml\x1b[0m\x1b[6;30;42md\x1b[0m\x1b
    [6;30;42me\x1b[0m\x1b[6;30;42mr\x1b[0m'
    '''
    word_to_return= ''
    for element in range(len(guess)):
        if guess[element]==correct_word[element]:
            word_to_return += color_string(guess[element], 'green')
        elif guess[element] in correct_word:
            word_to_return += color_string(guess[element], 'yellow')
        else:
            word_to_return += color_string(guess[element], 'gray')
            
    return word_to_return

def print_final_message(numb_tries, correct_word):
    ''' int, string -> None
     It prints the final message of the game indicating whether the player has
     lost or won.
     The function decides whether the player has won or lost according to the
     correct_word if numb_tries = 7
     then the player lost.
     If the player lost the function should print "You lost!" and it should
     print the correct word colored in green.
     Otherwise, the player won, so the function should print "You won!".
     In this case the function should print the number of words it took the
     player to win.
     
     >>> print_final_message(7, 'about')
     You lost! The word was about
     
     >>> print_final_message(4, 'crate')
     You won! It took you 4 guesses.
     
     >>> print_final_message(1, 'frame')
     You won! It took you 1 guess.
     '''

    if int(numb_tries) >= MAX_NUM_OF_GUESSES+1 :
        print("You lost! The word was "+color_string(correct_word, 'green'))
    
    else:
        if numb_tries==1:
            print("You won! It took you 1 guess.")
        else:
            print('You won! It took you '+str(numb_tries)+' guesses.')
            
            
if __name__ == '__main__':
    #doctest.testmod()
    valid_words = get_all_5_letter_words(load_words())
    main()

