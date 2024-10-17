'''
6) Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
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

# Calculate the minimum value of the tuple elements
min_value = min(my_tuple)

# Output the minimum value
print(min_value)
