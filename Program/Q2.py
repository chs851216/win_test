roman_table = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

def solution(roman_string):
    value = 0
    for i in range(len(roman_string)):
        value += roman_table[roman_string[i]]
        if i+1 < len(roman_string):
            if roman_table[roman_string[i]] < roman_table[roman_string[i+1]]:
                value -= (2 * roman_table[roman_string[i]])
    return value


sample_input = "III"
print("Output: {}".format(solution(sample_input)))

sample_input = "IV"
print("Output: {}".format(solution(sample_input)))

sample_input = "IX"
print("Output: {}".format(solution(sample_input)))

sample_input = "LVIII"
print("Output: {}".format(solution(sample_input)))

sample_input = "MCMXCIV"
print("Output: {}".format(solution(sample_input)))