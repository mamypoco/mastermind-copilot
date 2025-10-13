from app.game import generate_code, validate_guess, check_code_guessed

# --------------------------test generate_code------------------------------------

def test_generate_code_length_four():
    # Arrange/Act
    result = generate_code()

    # Assert
    assert len(result) == 4


def test_generate_code_uses_valid_letters():
    # Arrange
    valid_letters = {'R', 'O', 'Y', 'G', 'B', 'P'}

    # Act
    result = generate_code()

    # Assert
    for letter in result:
        assert letter in valid_letters

# added with chatGPT
def test_generate_code_half_or_less_duplicates_over_10_runs():
    # Run generate_code multiple times and check for at least half as many different codes as runs
    num_runs = 10
    codes = {tuple(generate_code()) for _ in range(num_runs)}
    assert len(codes) >= num_runs // 2

# --------------------------test validate_guess------------------------------------

def test_validate_guess_false_length_greater_than_four():
    # Arrange
    guess = ['R', 'R', 'R', 'R', 'R']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_true_valid_letters_rygp():
    # Arrange
    guess = ['R', 'Y', 'G', 'P']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is True


def test_validate_guess_true_valid_letters_bp():
    # Arrange
    guess = ['B', 'B', 'P', 'P']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is True


def test_validate_guess_false_invalid_letters():
    # Arrange
    guess = ['R', 'S', 'Y', 'P']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_true_lowercase_letters():
    # Arrange
    guess = ['b', 'b', 'p', 'p']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is True

# --------------------------test check_win_or_lose------------------------------------

def test_check_code_guessed_true():
    # Arrange
    guess = ['R', 'B', 'B', 'P']
    code = ['R', 'B', 'B', 'P']

    # Act
    result = check_code_guessed(guess, code)

    # Assert
    assert result is True


def test_check_code_guessed_no_match_false():
    # Arrange
    guess = ['R', 'B', 'B', 'P']
    code = ['R', 'B', 'B', 'O']

    # Act
    result = check_code_guessed(guess, code)

    # Assert
    assert result is False

# added with chatGPT
def test_validate_guess_accepts_mixed_case():
    guess = ['r', 'G', 'b', 'p']
    assert validate_guess(guess) is True

# added with chatGPT
def test_check_code_guessed_different_lengths():
    from app.game import check_code_guessed
    assert check_code_guessed(['R', 'G', 'B', 'P'], ['R', 'G', 'B']) is False

# added with chatGPT
def test_check_code_guessed_order_sensitivity_and_duplicates():
    from app.game import check_code_guessed
    # order matters for exact match
    code = ['R', 'R', 'G', 'B']
    guess_same = ['R', 'R', 'G', 'B']
    guess_diff_order = ['R', 'G', 'R', 'B']
    assert check_code_guessed(code, guess_same) is True
    assert check_code_guessed(code, guess_diff_order) is False