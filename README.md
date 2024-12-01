# Python Data Collections: List, Tuple, Dictionary, and Set

This README file introduces four fundamental data collection types in Python: **List**, **Tuple**, **Dictionary**, and **Set**. Each data type serves specific use cases, providing flexibility in managing and manipulating data.

---

## 1. **List**

A **list** is a mutable, ordered collection that allows duplicate elements. Lists are widely used for storing and managing a sequence of items.

### **Key Features**
- Ordered: Items have a defined order.
- Mutable: Elements can be changed.
- Duplicates: Allows duplicate values.

### **Examples**
```python
# Create a list
fruits = ["apple", "banana", "cherry"]

# Access elements
print(fruits[0])  # Output: apple

# Modify elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Add elements
fruits.append("orange")

# Remove elements
fruits.remove("apple")
```

### **Common Methods**
| Method         | Description                    |
|----------------|--------------------------------|
| `append()`     | Adds an element to the end.    |
| `remove()`     | Removes the first occurrence. |
| `sort()`       | Sorts the list.               |
| `pop()`        | Removes and returns an item.  |

---

## 2. **Tuple**

A **tuple** is an immutable, ordered collection. Tuples are ideal for storing data that should not change.

### **Key Features**
- Ordered: Items have a defined order.
- Immutable: Cannot be changed after creation.
- Duplicates: Allows duplicate values.

### **Examples**
```python
# Create a tuple
coordinates = (10, 20, 30)

# Access elements
print(coordinates[1])  # Output: 20

# Attempt to modify (raises an error)
# coordinates[1] = 50  # TypeError: 'tuple' object does not support item assignment
```

### **Use Cases**
- Representing fixed collections of items (e.g., geographical coordinates).

---

## 3. **Dictionary**

A **dictionary** is an unordered, mutable collection of key-value pairs. Keys must be unique and immutable.

### **Key Features**
- Key-Value Pairs: Data is stored in pairs.
- Mutable: Values can be changed.
- Unique Keys: Keys must be unique.

### **Examples**
```python
# Create a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

# Access values
print(person["name"])  # Output: Alice

# Modify values
person["age"] = 26

# Add new key-value pairs
person["job"] = "Engineer"

# Remove key-value pairs
person.pop("city")
```

### **Common Methods**
| Method        | Description                    |
|---------------|--------------------------------|
| `get()`       | Retrieves a value by key.     |
| `keys()`      | Returns all keys.             |
| `values()`    | Returns all values.           |
| `items()`     | Returns key-value pairs.      |
| `pop()`       | Removes an item by key.       |

---

## 4. **Set**

A **set** is an unordered, mutable collection of unique elements. Sets are useful for removing duplicates and performing mathematical operations.

### **Key Features**
- Unordered: No defined order.
- Mutable: Elements can be added or removed.
- Unique: Does not allow duplicates.

### **Examples**
```python
# Create a set
numbers = {1, 2, 3, 4, 5}

# Add elements
numbers.add(6)

# Remove elements
numbers.remove(3)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))        # Output: {1, 2, 3, 4, 5}
print(set_a.intersection(set_b)) # Output: {3}
```

### **Common Methods**
| Method           | Description                    |
|------------------|--------------------------------|
| `add()`          | Adds an element.              |
| `remove()`       | Removes an element.           |
| `union()`        | Returns the union of sets.    |
| `intersection()` | Returns the intersection.     |

---

## Comparison Table
| Property        | List          | Tuple         | Dictionary       | Set            |
|-----------------|---------------|---------------|------------------|----------------|
| Ordered         | Yes           | Yes           | No               | No             |
| Mutable         | Yes           | No            | Yes              | Yes            |
| Allows Duplicates | Yes          | Yes           | Keys: No, Values: Yes | No         |

---

## Conclusion
Understanding these data collection types will help you choose the most suitable structure for your needs. Experiment with each to gain familiarity and apply them effectively in your Python projects!
