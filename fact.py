'''
10) Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
'''
# Input the tuple values in a single line
elements = input().split()  # Read elements as a space-separated string

# Create a tuple from the list of elements
my_tuple = tuple(int(element) for element in elements)

# Input the value to count
x = int(input())

# Count the occurrences of x in the tuple
count = my_tuple.count(x)

# Function to calculate factorial without using factorial() method
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

# Calculate the factorial of the count
factorial_value = calculate_factorial(count)

# Output the factorial value
print(factorial_value)
