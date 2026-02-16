def valid_anagram_sort(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)

def valid_anagram_hashmap(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count_s = {}
    count_t = {}

    for i in range(len(s)):
        count_s[s[i]] = count_s.get(s[i], 0) + 1
        count_t[t[i]] = count_t.get(t[i], 0) + 1

    return count_s == count_t


def valid_anagram_using_array(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count = [0] * 26

    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for c in count:
        if c != 0:
            return False

    return True

# test cases
s1 = "anagram"
t1 = "nagaram"
s2 = "rat"
t2 = "car"
print(valid_anagram_sort(s1, t1))  # Output: True
print(valid_anagram_sort(s2, t2))  # Output: False
print(valid_anagram_hashmap(s1, t1))  # Output: True
print(valid_anagram_hashmap(s2, t2))  # Output: False
print(valid_anagram_using_array(s1, t1))  # Output: True
print(valid_anagram_using_array(s2, t2))  # Output: False