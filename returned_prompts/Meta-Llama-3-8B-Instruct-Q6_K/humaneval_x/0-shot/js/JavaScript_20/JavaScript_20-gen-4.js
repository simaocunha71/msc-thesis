```javascript
const findClosestElements = (numbers) => {
    let minDiff = Infinity;
    let closestElements = [];
    numbers.forEach((num1, i) => {
        numbers.forEach((num2, j) => {
            if (i !== j) {
                let diff = Math.abs(num1 - num2);
                if (diff < minDiff) {
                    minDiff = diff;
                    closestElements = [num1, num2].sort((a, b) => a - b);
                }
            }
        });
    });
    return closestElements;
};

// Test cases
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])); // Output: (2.0, 2.2)
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])); // Output: (2.0, 2.0)
```


This solution works by iterating over each pair of numbers in the list and calculating their difference. It keeps track of the pair with the smallest difference and returns those two numbers. If there are multiple pairs with the same smallest difference, it returns the first one it finds.

This solution has a time complexity of O(n^2), where n is the length of the input list. This is because it has a nested loop structure, where the outer loop iterates over each number in the list and the inner loop iterates over each other number in the list.

The space complexity is O(1), because it only uses a constant amount of space to store the minimum difference and the closest elements. It does not use any data structures that scale with the size of the input.