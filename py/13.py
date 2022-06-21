def roman_to_integer(roman: str) -> int:
    dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    int_val = 0
    for index in range(len(roman) - 1):
        curr_alph = roman[index]
        next_alph = roman[index + 1]
        if dictionary[curr_alph] >= dictionary[next_alph]:
            int_val += dictionary[curr_alph]
        else:
            int_val -= dictionary[curr_alph]
    return int_val + dictionary[roman[-1]]


print(roman_to_integer("MCMXCIV"))  # 1994
print(roman_to_integer("VII"))  # 7
print(roman_to_integer("LVIII"))  # 58
print(roman_to_integer("III"))  # 3
