'''
7) Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
'''
# Input the tuple values in a single line
elements = input().split()  # Read elements as a space-separated string

# Create a tuple from the list of elements
my_tuple = tuple(int(element) for element in elements)

# Input the value to count
x = int(input())

# Count the occurrences of x in the tuple
count = my_tuple.count(x)

# Output the count
print(count)
