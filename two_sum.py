def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_sorted(nums, target):
    A = []
    for i, num in enumerate(nums):
        A.append([num, i])

    A.sort()
    i, j = 0, len(nums) - 1
    while i < j:
        cur = A[i][0] + A[j][0]
        if cur == target:
            return [min(A[i][1], A[j][1]),
                    max(A[i][1], A[j][1])]
        elif cur < target:
            i += 1
        else:
            j -= 1
    return []

def two_sum_hashmap(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []

# test cases
nums1 = [2, 7, 11, 15]
target1 = 9
nums2 = [3, 2, 4]
target2 = 6
print(two_sum_brute_force(nums1, target1))  # Output: [0, 1]
print(two_sum_brute_force(nums2, target2))  # Output: [1, 2]
print(two_sum_sorted(nums1, target1))  # Output: [0, 1]
print(two_sum_sorted(nums2, target2))  # Output: [1, 2]
print(two_sum_hashmap(nums1, target1))  # Output: [0, 1]
print(two_sum_hashmap(nums2, target2))  # Output: [1, 2]        