import random

COLORS = ['R', 'O', 'Y', 'G', 'B', 'P']

# Wave 1
def generate_code():
# takes no arguments
# generate random 4 digits code using R, O, Y, G, B, P
# letters can be repeated
# use for-loop to generate 4 digits
    
    code = []
    for _ in range(4):
        code.append(random.choice(COLORS))
    return code

def validate_guess(guess):
    if len(guess) != 4:
        return False
    for color in guess:
        if color.upper() not in COLORS:
            return False
    return True


def check_code_guessed(code, guess):
    # Normalize both lists to uppercase and compare
    if not isinstance(code, list) or not isinstance(guess, list):
        return False
    if len(code) != len(guess):
        return False
    normalized_code = [c.upper() for c in code]
    normalized_guess = [g.upper() for g in guess]
    return normalized_code == normalized_guess

# Wave 2
# Add your Wave 2 functions here

# Wave 3
# Add your Wave 3 functions here
