```
def unique_product(my_list):
    unique_elements = set(my_list)
    product = 1
    for element in unique_elements:
        product *= element
    return product
```

