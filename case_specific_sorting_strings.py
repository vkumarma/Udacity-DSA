def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list
    
    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """
    inp_list = list(string)
    output = []
    def merge_sort(chars):
        if len(chars) <= 1:
            return chars
        mid = len(chars) // 2
        left = chars[:mid]
        right = chars[mid:]
        
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left,right)
    
    def merge(left,right):
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
    
    
    sorted_list = merge_sort(inp_list)
    if sorted_list[0].islower():
        output += sorted_list
        print("asdg")
    elif sorted_list[len(sorted_list)-1].isupper():
        output += sorted_list
        print("asdg")
    else:
        upper = 0 # upper is a pointer, which points to the first upper case character
        index = 0
        while index < len(sorted_list):
            if sorted_list[index].islower():
                lower = index # lower is a pointer, pointing to the first lower case character
                break
            index += 1
       
        for i in range(len(string)):
            if string[i].islower():
                output.append(sorted_list[lower])
                lower += 1
            else:
                output.append(sorted_list[upper])
                upper += 1
   
    return "".join(output)
            


print(case_sort("fedRTSersUXJ")) # "deeJRSfrsTUX"
print(case_sort("defRTSersUXI"))
    