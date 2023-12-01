class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # A simple hash function using the length of the key
        return len(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        # Collision resolution using chaining (each slot contains a linked list of key-value pairs)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            # Check if the key already exists, and update the value if it does
            for i, (existing_key, existing_value) in enumerate(self.table[index]):
                if existing_key == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                # Key doesn't exist, add a new key-value pair
                self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)

        # Search for the key in the linked list at the calculated index
        if self.table[index] is not None:
            for existing_key, value in self.table[index]:
                if existing_key == key:
                    return value

        # Key not found
        raise KeyError(f"Key '{key}' not found in the hash table")

# Example usage:
hash_table = HashTable()

hash_table.insert("name", "John")
hash_table.insert("age", 25)

print("Value for 'name':", hash_table.get("name"))
print("Value for 'age':", hash_table.get("age"))