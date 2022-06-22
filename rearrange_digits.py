def rearrange_digits(input_list):
    max_sub = ""
    min_sub = ""
    sorted_list = merge_sort(input_list)
    for i in range(0, len(sorted_list), 2):
        if i + 1 < len(sorted_list):
            maxi = max(sorted_list[i], sorted_list[i+1])
            mini = min(sorted_list[i], sorted_list[i+1])

            max_sub += str(maxi)
            min_sub += str(mini)

    if len(sorted_list) % 2 != 0:
        max_sub += str(sorted_list[-1])

    return int(max_sub[::-1]), int(min_sub[::-1])

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    print(output)
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 3, 4, 5], [53, 41]])
