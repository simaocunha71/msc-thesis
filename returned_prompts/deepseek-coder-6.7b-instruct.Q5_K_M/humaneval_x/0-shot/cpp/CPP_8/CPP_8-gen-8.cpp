    int sum = 0;
    int product = 1;
    for(int i=0; i<numbers.size(); i++){
        sum += numbers[i];
        product *= numbers[i];
    }
    return {sum, product};

The function sum_product takes a vector of integers as an argument. It then iterates over the vector, adding each element to the sum and multiplying the product by the current element. Finally, it returns a vector containing the sum and product.

