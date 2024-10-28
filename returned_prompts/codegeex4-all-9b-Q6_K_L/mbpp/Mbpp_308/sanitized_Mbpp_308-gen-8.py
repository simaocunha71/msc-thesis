def large_product(list1, list2, num):
    # Initialize a list to store the products
    products = []
    
    # Iterate through each element in list1
    for i in list1:
        # Iterate through each element in list2
        for j in list2:
            # Calculate the product of the two elements
            product = i * j
            # Add the product to the list
            products.append(product)
    
    # Sort the list of products in descending order
    products.sort(reverse=True)
    
    # Return the specified number of largest products
    return products[:num]