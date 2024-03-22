def calculate_sum_with_formatting(data):
 """Calculates the sum of a list of numbers with comma separators and two decimal places.

 Args:
     data: A list of integer numbers.

 Returns:
     A string representing the formatted sum.
 """

 total = sum(data)
 formatted_sum = "{:,.2f}".format(total)  # Use f-string formatting
 return formatted_sum

# Sample data (replace with actual data from your file)
data = [10, 1000, 20]

# Calculate and print the formatted sum
formatted_sum = calculate_sum_with_formatting(data)
print(formatted_sum)  # Output: 1,030.00
