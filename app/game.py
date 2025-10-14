import random

# Wave 1
VALID_LETTERS = {'R', 'O', 'Y', 'G', 'B', 'P'}

def generate_code():
    # Generate a code of 4 random letters from valid_letters      
    letters_list = list(VALID_LETTERS)
    return [random.choice(letters_list) for _ in range(4)]


def validate_guess(guess):
    # Exit early if guess is not exactly 4 elements long
    if len(guess) != 4:
        return False
    
    # Convert guess to uppercase for case-insensitive comparison
    uppercased_guess = normalize_code(guess)

    # Return False if we find an invalid element of guess
    return all(letter in VALID_LETTERS for letter in uppercased_guess)
    # for letter in uppercased_guess:
    #     if letter not in VALID_LETTERS:
    #         return False
    # return True

def check_code_guessed(guess, code):
    # Convert guess to uppercase for case-insensitive comparison
    uppercased_guess = normalize_code(guess)

    # Check if the guess and code are identical (win condition)
    return code == uppercased_guess
    

def normalize_code(code):
    """
    Normalize the casing for a code by converting the list of characters to uppercase.
    """
    return [str(letter).upper() for letter in code]

# Wave 2
def color_count(guess, code):
    # returns an integer representing the number of pegs that are the correct color (letter), regardless of whether they are in the correct position or not

    # if no pegs are the correct color, return 0

    # A letter that appears more times in guess than it appears in code is counted the number of times it appears in code

    # A letter that appears fewer times in guess than it appears in code is counted the number of times it appears in guess

    count = 0
    # Count the number of times each color appears in both guess and code, and sum the minimum for each color
    for letter in set(guess):
        count += min(guess.count(letter), code.count(letter))
    return count

guess = ['R', 'R', 'G', 'P']
code = ['R', 'R', 'O', 'B']
print(color_count(guess, code))


def correct_pos_and_color(guess, code):
    count = 0
    for i in range(len(guess)):
        if guess[i] == code[i]:
            count += 1
    # for i, peg in enumerate(guess):
    #     if peg == code[i]:
    #         count += 1

    return count

def generate_hint(guess, code):
    correct_pos = correct_pos_and_color(guess, code)
    correct_color = color_count(guess, code) - correct_pos
    return (correct_pos, correct_color)


# Wave 3
# Add your Wave 3 functions here
