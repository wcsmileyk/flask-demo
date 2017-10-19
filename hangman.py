# Forked from an MIT 6.0001 problem set. So no one sue me. Please.
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    word_guessed = True

    for letter in secret_word:
        if letter not in letters_guessed:
            word_guessed = False

    return word_guessed


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letter_count = len(secret_word)
    guessed_word_letters = ['_ ' for i in range(letter_count)]

    for i in range(letter_count):
        for letter in letters_guessed:
            if secret_word[i] == letter:
                guessed_word_letters[i] = letter

    guessed_word = ''
    for letter in guessed_word_letters:
        guessed_word = guessed_word + letter

    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    alpha_list = []

    for letter in alphabet:
        if letter not in letters_guessed:
            alpha_list.append(letter)

    left_letters = ''
    for letter in alpha_list:
        left_letters = left_letters + letter

    return left_letters


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * X At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.
      
    * X The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letter_count = len(secret_word)
    letters_guessed = []
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    guesses = 6

    print(f'Secret word has {letter_count} letters')
    print(guessed_word)
    print('*' * 10)

    playing = True


    while playing:
        availale_letters = get_available_letters(letters_guessed)
        print(f'You have {guesses} guesses left')
        print(f'Available letters: {availale_letters}')
        print(gallow_pic[6 - guesses])
        print(guessed_word)

        guess = input('Please guess a letter: ').lower()
        need_guess = True

        while need_guess:
            if guess.isalpha() and len(guess) == 1 and guess in availale_letters:
                need_guess = False

            if len(guess) != 1:
                guess = input('Sorry, guess exactly 1 letter: ').lower()
                continue
            if not guess.isalpha():
                guess = input('Sorry, only guess letters: ').lower()
                continue
            if guess not in availale_letters:
                guess = input('Sorry, you already guessed that. Guess again: ').lower()
                continue

        letters_guessed.append(guess)

        if guess not in secret_word:
            guesses -= 1
            print(f'Sorry, no {guess} in word')
        else:
            print(f'Good guess!')
        guessed_word = get_guessed_word(secret_word, letters_guessed)

        if is_word_guessed(secret_word, letters_guessed):
            print('You win!')
            print(guessed_word)
            playing = False

        if guesses == 0:
            print(gallow_pic[6 - guesses])
            print(guessed_word)
            print('You lose!')
            print('The secret word was: ', secret_word)
            playing = False


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)

