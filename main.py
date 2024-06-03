def sort_descending(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage:
arr = [3, 2, 7, 4, 6, 9]
print(sort_descending(arr)) 


def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

# Example usage:
print(is_palindrome("madam")) 
print(is_palindrome("doctor"))


def sum_of_two_largest(arr):
    max1, max2 = float('-inf'), float('-inf')
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    return max1 + max2

# Example usage:
arr = [3, 7, 1, 5, 11, 19]
print(sum_of_two_largest(arr)) 


def find_missing_elements(arr):
    max_val = max(arr)
    missing_elements = []
    for i in range(max_val + 1):
        if i not in arr:
            missing_elements.append(i)
    return missing_elements

# Example usage:
arr = [3, 4, 9, 1, 7, 3, 2, 6]
print(find_missing_elements(arr))  


def most_repeated_element(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    max_count = max(count_dict.values())
    for num, count in count_dict.items():
        if count == max_count:
            return f"{num} is repeated {max_count} times"

# Example usage:
arr = [4, 3, 5, 6, 4, 7, 9, 2, 4, 6, 3, 4, 6, 3, 4, 8, 5, 1, 5]
print(most_repeated_element(arr)) 


def rotate_array(arr):
    return [arr[-1]] + arr[:-1]

# Example usage:
arr = [3, 8, 9, 7, 6]
print(rotate_array(arr))  