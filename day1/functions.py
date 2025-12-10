#def twoNumbers(num1, num2):
    #total = num1 + num2
    #product = num1 * num2
    #print("Sum:", total, "multiple:", product)
    

# Version that returns values instead of printing
# This way it is professional and reusable in other code

def twoNumberss(num1, num2):
    total = num1 + num2
    product = num1 * num2
    return total, product

# Call the function and store results

sum_result, product_result = twoNumberss(5,7)

# Print the results
print("Sum:", sum_result)
print("Product:", product_result)
"""
Advantages of this approach
Reusable — you can use twoNumbers in other programs without modifying it.
Testable — easier to write unit tests.
Flexible — you can print, log, or store the results however you like.
"""