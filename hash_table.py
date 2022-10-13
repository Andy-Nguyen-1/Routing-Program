class HashTableEntry:
    def __init__(self, key, item):
        self.key = key
        self.item = item
# Chaining hash table
class HashMap:
    #Constructor with initial capacity of 10
    #Space-Time Complexity = O(1)
    def __init__(self, capacity=10):
        self.map = []
        for i in range(capacity):
            self.map.append([])

    # getter to create hash key
    # Space-Time Complexity = O(1)
    def get_bucket(self, key):
        bucket = int(key) % len(self.map)
        return bucket

    # Inserts a new item into the hash map.
    # Time-Space Complexity O(n)
    def insert(self, key, value):
        key_hash = self.get_bucket(key)
        key_value = [key, value]

        if self.map[key_hash] == None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Updates packages in hash table
    # Space-Time Complexity O(n)
    def update(self, key, value):
        key_hash = self.get_bucket(key)
        if self.map[key_hash] != None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True

    # Retrieves value from hash table.
    # Space-Time Complexity = O(n)
    def search(self, key):
        key_hash = self.get_bucket(key)
        if self.map[key_hash] != None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Delete a value from hash table -> O(n)
    def delete(self, key):
        key_hash = self.get_bucket(key)

        if self.map[key_hash] == None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False
