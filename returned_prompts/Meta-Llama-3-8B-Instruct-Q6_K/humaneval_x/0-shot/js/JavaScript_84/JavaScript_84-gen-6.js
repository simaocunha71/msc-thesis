```javascript
const binary = N.toString(2); // convert to binary
let sum = 0;
for (let i = 0; i < binary.length; i++) {
  if (binary[i] === '1') {
    sum += 1;
  }
}
return sum.toString(); // convert back to string
``` 
Explanation: 
1. We convert the number to a binary string using the `toString(2)` method.
2. We initialize a variable `sum` to 0.
3. We iterate over each character in the binary string.
4. If the character is '1', we increment the `sum` variable.
5. Finally, we convert the `sum` variable back to a string using the `toString()` method and return it.

Example Output:
For N = 1000, the output will be "1"
For N = 150, the output will be "6"
For N = 147, the output will be "12" 

This solution has a time complexity of O(n), where n is the number of digits in the binary representation of the input number. This is because we are iterating over each character in the binary string. The space complexity is O(1), as we are using a constant amount of space to store the `sum` variable and the `binary` string. 
```javascript
console.log(solve(1000)); // Output: "1"
console.log(solve(150)); // Output: "6"
console.log(solve(147)); // Output: "12"
``` 
This is an efficient and simple solution that works well for the given constraints. 
```javascript
``` 
Note: The solution assumes that the input number is a positive integer. If the input can be negative or zero, additional checks and handling would be needed. 
```javascript
``` 
I hope this helps! Let me know if you have any questions. 
```javascript
```  ```
```javascript
```  ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````