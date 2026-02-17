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
