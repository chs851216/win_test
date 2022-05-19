def solution(num_list, target):
    for i in range(len(num_list)):
        new_list = num_list.copy()
        a = num_list[i]
        b = target - a
        del new_list[i]
        if b in new_list:
            return [i, num_list.index(b, i+1)]

sample_target = 9
sample_input = [2, 7, 11, 15]
print("Output: {}".format(solution(sample_input, sample_target)))

sample_target = 6
sample_input = [3, 2, 4]
print("Output: {}".format(solution(sample_input, sample_target)))

sample_target = 6
sample_input = [3, 3]
print("Output: {}".format(solution(sample_input, sample_target)))