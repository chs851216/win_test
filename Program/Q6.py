def solution(num):
    while num > 4:
        num /= 4
    if num % 4 == 0 or num % 4 == 1:
        return True
    return False


sample_input = 16
print("Output: {}".format(solution(sample_input)))

sample_input = 5
print("Output: {}".format(solution(sample_input)))

sample_input = 1
print("Output: {}".format(solution(sample_input)))
