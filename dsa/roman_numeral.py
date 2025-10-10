roman_numerals = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}


def to_roman(number):
    result = ""
    for key in roman_numerals:
        if number >= key:
            result += (number // key) * roman_numerals[key]
            number %= key
    return result


if __name__ == "__main__":
    test_cases = {
        39: "XXXIX",
        246: "CCXLVI",
        789: "DCCLXXXIX",
        2421: "MMCDXXI",
        3999: "MMMCMXCIX"
    }

    for num, expected in test_cases.items():
        assert to_roman(num) == expected, f"Wrong at {num}"
    print("All tests passed!")