Here is the solution for the problem:

```javascript
const sumProduct = (numbers) => {
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
};
```



Explanation:
The function takes a list of numbers as input and returns a tuple containing the sum and product of all the numbers in the list. If the input list is empty, it returns a tuple with sum as 0 and product as 1. Otherwise, it initializes sum and product to 0 and 1 respectively, then iterates over the list, adding each number to sum and multiplying each number to product. Finally, it returns the sum and product as a tuple.

Example:
```javascript
console.log(sumProduct([1, 2, 3, 4])); // Output: [10, 24]
console.log(sumProduct([])); // Output: [0, 1]
```



This function uses a simple for loop to iterate over the input list, and the built-in JavaScript operators for addition (+) and multiplication (*) to calculate the sum and product. The function returns the sum and product as a tuple using the return statement. The function works correctly even if the input list is empty, as it returns a tuple with sum as 0 and product as 1 in that case.