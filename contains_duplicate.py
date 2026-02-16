def has_duplicate_brute_force(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def has_duplicate_sorted(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

def has_duplicate_optimized(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# test cases
nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 3, 1]        
print(has_duplicate_brute_force(nums1))  # Output: False
print(has_duplicate_brute_force(nums2))  # Output: True
print(has_duplicate_optimized(nums1))  # Output: False
print(has_duplicate_optimized(nums2))  # Output: True
print(has_duplicate_sorted(nums1))  # Output: False
print(has_duplicate_sorted(nums2))  # Output: True