Here is the solution for the problem:
```
function sumProduct(numbers) {
    if (numbers.length === 0) {
        return [0, 1];
    }
    let sum = 0;
    let product = 1;
    for (let num of numbers) {
        sum += num;
        product *= num;
    }
    return [sum, product];
}
```
Explanation:
The function `sumProduct` takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list.

If the list is empty, the function returns a tuple with `0` as the sum and `1` as the product. This is because the sum of an empty list is `0` and the product of an empty list is `1`.

If the list is not empty, the function initializes two variables, `sum` and `product`, to `0` and `1`, respectively. Then, it iterates over the list, adding each number to the `sum` and multiplying each number by the current `product`. Finally, it returns a tuple containing the `sum` and `product`.

The function is tested with the examples provided in the problem statement, and it returns the expected results.