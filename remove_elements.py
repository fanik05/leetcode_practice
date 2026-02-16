def remove_elements(nums, val):
    tmp = []
    for num in nums:
        if num == val:
            continue
        tmp.append(num)
    for i in range(len(tmp)):
        nums[i] = tmp[i]
    return len(tmp)

def remove_elements_optimized(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

# test cases    
nums1 = [3, 2, 2, 3]
val1 = 3
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
print(remove_elements(nums1, val1))  # Output: 2
print(nums1[:2])  # Output: [2, 2]
print(remove_elements(nums2, val2))  # Output: 5
print(nums2[:5])  # Output: [0, 1, 3, 0, 4]
print(remove_elements_optimized(nums1, val1))  # Output: 2
print(nums1[:2])  # Output: [2, 2]
print(remove_elements_optimized(nums2, val2))  # Output: 5
print(nums2[:5])  # Output: [0, 1, 3, 0, 4]
    