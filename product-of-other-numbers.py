# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.
# Do not use division.

test_input =   [2, 7, 3, 4]


# Naive answer: O(n^2) time and O(n) space
def get_products_of_all_ints_except_at_index_1(input):
    output = [1]*len(input)
    if len(input) <= 1:
        return input
    for index_current, value_current in enumerate(input):
        for index_other, value_other in enumerate(input):
            if index_other is index_current:
                continue
            output[index_current] = output[index_current] * value_other
    return output

print get_products_of_all_ints_except_at_index_1(test_input)

# Answer: O(n) time and O(n) space
def get_products_of_all_ints_except_at_index_2(input):
    length = len(input)
    output = [1]*length
    values_before_index = [1]*length
    values_after_index = [1]*length

    if length <= 1:
        return input

    for i, value_current in enumerate(input):
        if i is 0:
            values_before_index[i] = 1
        else:
            values_before_index[i] = values_before_index[i-1]*input[i-1]

    for i, value_current in reversed(list(enumerate(input))):
        if i is length-1:
            values_after_index[i] = 1
        else:
            values_after_index[i] = values_after_index[i+1]*input[i+1]
        output[i] = values_after_index[i]*values_before_index[i]

    return output

print get_products_of_all_ints_except_at_index_2(test_input)
