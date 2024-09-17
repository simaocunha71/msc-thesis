def max_Product(input_array):
    max_product = 0
    max_pair = ()
    for i in range(len(input_array)):
        for j in range(i+1, len(input_array)):
            product = input_array[i] * input_array[j]
            if product > max_product:
                max_product = product
                max_pair = (input_array[i], input_array[j])
    return max_pair