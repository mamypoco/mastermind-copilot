from app.game import generate_code, validate_guess


def test_generate_code_returns_list():
    result = generate_code()
    assert isinstance(result, list)


def test_generate_code_items_uppercase():
    # generate_code should return uppercase letters from COLORS
    result = generate_code()
    for item in result:
        assert item == item.upper()


def test_validate_guess_false_length_less_than_four():
    guess = ['R', 'G', 'B']
    assert validate_guess(guess) is False


def test_validate_guess_accepts_mixed_case():
    guess = ['r', 'G', 'b', 'p']
    assert validate_guess(guess) is True


def test_check_code_guessed_case_insensitive():
    code = ['r', 'g', 'b', 'p']
    guess = ['R', 'G', 'B', 'P']
    from app.game import check_code_guessed
    assert check_code_guessed(code, guess) is True


def test_check_code_guessed_non_list_inputs():
    from app.game import check_code_guessed
    # non-list inputs should return False
    assert check_code_guessed('RGBP', ['R', 'G', 'B', 'P']) is False
    assert check_code_guessed(['R', 'G', 'B', 'P'], 'RGBP') is False


def test_check_code_guessed_different_lengths():
    from app.game import check_code_guessed
    assert check_code_guessed(['R', 'G', 'B', 'P'], ['R', 'G', 'B']) is False


def test_check_code_guessed_order_sensitivity_and_duplicates():
    from app.game import check_code_guessed
    # order matters for exact match
    code = ['R', 'R', 'G', 'B']
    guess_same = ['R', 'R', 'G', 'B']
    guess_diff_order = ['R', 'G', 'R', 'B']
    assert check_code_guessed(code, guess_same) is True
    assert check_code_guessed(code, guess_diff_order) is False
