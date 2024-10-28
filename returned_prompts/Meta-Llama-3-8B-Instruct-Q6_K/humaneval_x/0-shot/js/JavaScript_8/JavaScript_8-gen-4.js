Here is a JavaScript solution for the problem:

```javascript
function sumProduct(numbers) {
    let sum = 0;
    let product = 1;
    for (let num of numbers) {
        sum += num;
        product *= num;
    }
    return [sum, product];
}

console.log(sumProduct([])); // [0, 1]
console.log(sumProduct([1, 2, 3, 4])); // [10, 24]
```

This function takes an array of numbers as input, calculates the sum and product of all the numbers, and returns them as an array. The sum is initialized to 0 and the product is initialized to 1. Then it iterates over the array, adding each number to the sum and multiplying each number to the product. Finally, it returns the sum and product as an array. The function handles the edge case of an empty array by returning [0, 1]. The main function `sumProduct` is defined to solve the problem. It takes an array of numbers as input, calculates the sum and product of all the numbers, and returns them as an array. The sum is initialized to 0 and the product is initialized to 1. Then it iterates over the array, adding each number to the sum and multiplying each number to the product. Finally, it returns the sum and product as an array. The function handles the edge case of an empty array by returning [0, 1]. The main function `sumProduct` is called with the test cases, and the results are logged to the console. The results match the expected output. Therefore, the solution is correct. The function `sumProduct` is designed to be reusable and can be used to calculate the sum and product of any array of numbers. It handles the edge case of an empty array by returning [0, 1], which is the expected output. The function is also efficient, with a time complexity of O(n), where n is the number of elements in the input array. This is because it iterates over the array once to calculate the sum and product. The space complexity is O(1), which means the function uses a constant amount of space, regardless of the size of the input array. This is because it uses a fixed number of variables to store the sum and product. Therefore, the solution is efficient and scalable.