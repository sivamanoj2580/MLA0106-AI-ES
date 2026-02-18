# List Operations

list1 = [1, 2, [3, 4], 5]
list2 = [6, 7]

# Nested List
print("Nested List:", list1)

# Length
print("Length:", len(list1))

# Concatenation
print("Concatenation:", list1 + list2)

# Membership
print("Is 2 in list1?", 2 in list1)

# Iteration
print("Iteration:")
for item in list1:
    print(item)

# Indexing
print("Indexing:", list1[2])

# Slicing
print("Slicing:", list1[1:4])
