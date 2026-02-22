class MyHashSet:
    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)
    
    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.data
    
class MyHashsetWithBooleanArray:
    def __init__(self):
        self.data = [False] * 1000001

    def add(self, key: int) -> None:
        self.data[key] = True
    
    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]

class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None
    
class MyHashSetWithLinkedList:
    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False

# test cases
hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))  # Output: True
print(hashSet.contains(3))  # Output: False
hashSet.add(2)
print(hashSet.contains(2))  # Output: True
hashSet.remove(2)
print(hashSet.contains(2))  # Output: False
hashSet2 = MyHashsetWithBooleanArray()
hashSet2.add(1)
hashSet2.add(2)
print(hashSet2.contains(1))  # Output: True
print(hashSet2.contains(3))  # Output: False
hashSet2.add(2)
print(hashSet2.contains(2))  # Output: True
hashSet2.remove(2)
print(hashSet2.contains(2))  # Output: False
hashSet3 = MyHashSetWithLinkedList()
hashSet3.add(1)
hashSet3.add(2)
print(hashSet3.contains(1))  # Output: True
print(hashSet3.contains(3))  # Output: False
hashSet3.add(2)
print(hashSet3.contains(2))  # Output: True
hashSet3.remove(2)
print(hashSet3.contains(2)) # Output: False
