
def max_product_tuple(numbers):
    products = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            products.append(numbers[i][0] * numbers[i][1] * numbers[j][0] * numbers[j][1])
    return max(products)


