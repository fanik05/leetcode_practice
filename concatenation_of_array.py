# bruteforce approach

def concatenate_array_brute(arr):
    result = []
    for i in range(2):
        for j in range(len(arr)):
            result.append(arr[j])
    return result

# optimized approach
def concatenate_array_optimized(arr):
    n = len(arr)
    result = [0] * (2 * n)

    for i in range(n):
        result[i] = arr[i]
        result[i + n] = arr[i]
    
    return result


# test cases
arr1 = [1, 2, 3]
print(concatenate_array_brute(arr1))  # Output: [1, 2, 3, 1, 2, 3]
print(concatenate_array_optimized(arr1))  # Output: [1, 2, 3, 1, 2, 3]  