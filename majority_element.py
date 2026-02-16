def majority_element_hash(nums):
    countNums = {}
    ans, maxCount = 0, 0

    for n in nums:
        countNums[n] = 1 + countNums.get(n, 0)
        ans = n if countNums[n] > maxCount else ans
        maxCount = max(countNums[n], maxCount)

    return ans

def majority_element_boyer_moore(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

# test cases
nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]
print(majority_element_hash(nums1))  # Output: 3
print(majority_element_hash(nums2))  # Output: 2
print(majority_element_boyer_moore(nums1))  # Output: 3
print(majority_element_boyer_moore(nums2))  # Output: 2 