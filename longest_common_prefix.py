def longest_common_prefix_horizontal(strs):
    prefix = strs[0]
    for i in range(1, len(strs)):
        j = 0
        while j < min(len(prefix), len(strs[i])):
            if prefix[j] != strs[i][j]:
                break
            j += 1
        prefix = prefix[:j]
    return prefix

def longest_common_prefix_vertical(strs):
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return s[:i]
    return strs[0]

# test cases
strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
print(longest_common_prefix_horizontal(strs1))  # Output: "fl"
print(longest_common_prefix_horizontal(strs2))  # Output: ""
print(longest_common_prefix_vertical(strs1))  # Output: "fl"
print(longest_common_prefix_vertical(strs2))  # Output: ""
    