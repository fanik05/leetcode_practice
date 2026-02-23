class MyhashMap:
    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]
    
    def remove(self, key: int) -> None:
        self.map[key] = -1

# test cases
hashMap = MyhashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
print(hashMap.get(1))  # Output: 1
print(hashMap.get(3))  # Output: -1
hashMap.put(2, 1)
print(hashMap.get(2))  # Output: 1
hashMap.remove(2)
print(hashMap.get(2))  # Output: -1     