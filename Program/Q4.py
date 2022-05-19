def solution(num_array):
    # Bubble Sort
    for i in range(len(num_array)):
        for j in range(len(num_array)):
            if num_array[i] < num_array[j]:
                temp = num_array[i]
                num_array[i] = num_array[j]
                num_array[j] = temp
    return num_array

sample_input = [2, 0, 2, 1, 1, 0]
print("Output: {}".format(solution(sample_input)))

sample_input = [2, 0, 1]
print("Output: {}".format(solution(sample_input)))

sample_input = [0]
print("Output: {}".format(solution(sample_input)))

sample_input = [1]
print("Output: {}".format(solution(sample_input)))