import pytest

def compare_numbers(a, b):
    return a == b

def test_compare_numbers_equal():
    assert compare_numbers(5, 5) == True

def test_compare_numbers_not_equal():
    assert compare_numbers(5, 10) == False

if __name__ == "__main__":
    pytest.main()
