# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.

list_of_ints = [2, -5, -1, -17, -8 , 1, 21, 200]

def highest_product_of_3(input):
    selected = [input[0],input[1],input[2]]
    product = selected[0] * selected[1] * selected [2]
    i = 3

    while i < len(input):
        if input[i] * selected[1] * selected [2] > product:
            selected[0] = input[i]
        elif selected[0] * input[i] * selected [2] > product:
            selected[1] = input[i]
        elif selected[0] * selected [1] * input[i] > product:
            selected[2] = input[i]
        product = selected[0] * selected[1] * selected [2]
        i += 1

    print selected
    return product


print highest_product_of_3(list_of_ints)

# Same as above, but with k integers instead of 3
"""
def highest_product_of_k(input, k):

    return product
"""