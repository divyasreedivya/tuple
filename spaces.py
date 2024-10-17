'''
8) Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
'''
# Input the tuple elements in a single line
elements = input().split()  # Read elements as a space-separated string

# Create a tuple from the list of elements
my_tuple = tuple(int(element) for element in elements)

# Initialize a variable to hold the sum
total_sum = 0

# Loop through the tuple and add each element to the total sum
for value in my_tuple:
    total_sum += value
