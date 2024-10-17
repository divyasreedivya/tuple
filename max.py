'''
5) Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
'''
# Input the number of elements in the tuple
n = int(input())

# Initialize an empty list to collect the elements
elements = []

# Input the tuple elements in separate lines
for _ in range(n):
    element = int(input())
    elements.append(element)

# Create a tuple from the list of elements
my_tuple = tuple(elements)

# Calculate the maximum value of the tuple elements
max_value = max(my_tuple)

# Output the maximum value
print(max_value)
