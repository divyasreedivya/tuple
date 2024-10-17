'''
4) Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
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

# Calculate the sum of the tuple elements
total_sum = sum(my_tuple)

# Output the sum
print(total_sum)
