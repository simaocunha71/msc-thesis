The problem requires checking if it is possible to exchange elements between two lists such that all elements of the first list (lst1) become even. The solution involves iterating through the elements of lst1 and checking if they are odd. If an element is odd, we then check if there is an even number available in lst2 to replace it. If such an even number exists, we replace the odd number with the even number and remove the even number from lst2. If at the end of the process, all elements in lst1 are even, we return "YES". Otherwise, we return "NO".

Here is the implementation:

```javascript
const exchange = (lst1, lst2) => {
    for (let i = 0; i < lst1.length; i++) {
        if (lst1[i] % 2 !== 0) {
            // Check if there is an even number available in lst2
            if (lst2.some(num => num % 2 === 0)) {
                // Find the first even number in lst2
                let evenIndex = lst2.findIndex(num => num % 2 === 0);
                // Replace the odd number in lst1 with the even number from lst2
                lst1[i] = lst2[evenIndex];
                // Remove the even number from lst2
                lst2.splice(evenIndex, 1);
            } else {
                // If there is no even number in lst2 to replace the odd number, return "NO"
                return "NO";
            }
        }
    }
    // If all elements in lst1 are even, return "YES"
    return "YES";
}
```

We can test the function with the provided examples:

```javascript
console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])); // "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])); // "NO"
```

The output should be:

```
YES
NO
```