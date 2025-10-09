"""
Problem: Convert interger to roman numerals


Planning:


Candidate Solution:
- Use dict because roman numerals are deterministic.
- 

Criticism:
- General refactoring

"""

def to_roman(number):
    # TO DO

    pass













if __name__ == "__main__":
    test_cases = {
        39: "XXXIX",
        246: "CCXLVI",
        789: "DCCLXXXIX",
        2421: "MMCDXXI"
    }

    for num, expected in test_cases.items():
        assert(num) == expected, f"Wrong at {num}"

    print("All tests passed!")