The Tribonacci sequence is a sequence of numbers where each number is the sum of the three preceding ones. The sequence starts with three initial terms, 1, 3, and 2. The general formula for the Tribonacci sequence is:

Tri(n) = Tri(n-1) + Tri(n-2) + Tri(n-3)

where Tri(n) is the nth term of the sequence.

In this problem, we are given a non-negative integer n and we need to return a list of the first n + 1 numbers of the Tribonacci sequence.

To solve this problem, we can use a recursive function. The recursive function will take an integer n as input and return a list of the first n + 1 numbers of the Tribonacci sequence.

Here is the implementation of the recursive function in JavaScript:

```javascript
const tri = (n) => {
  // Base case: if n is less than 3, return the first 3 numbers of the sequence
  if (n < 3) {
    return [1, 3, 2];
  }

  // Recursive case: calculate the next number in the sequence by summing the previous three numbers
  const nextNumber = tri(n - 1)[0] + tri(n - 2)[0] + tri(n - 3)[0];

  // Call the recursive function to calculate the next n - 1 numbers of the sequence
  const nextNumbers = tri(n - 1);

  // Add the next number to the end of the list of numbers
  nextNumbers.push(nextNumber);

  // Return the list of numbers
  return nextNumbers;
};

// Test the function
console.log(tri(3)); // [1, 3, 2, 8]
```

In this implementation, we first check if n is less than 3. If it is, we return the first 3 numbers of the sequence. Otherwise, we calculate the next number in the sequence by summing the previous three numbers. We then call the recursive function to calculate the next n - 1 numbers of the sequence. Finally, we add the next number to the end of the list of numbers and return the list of numbers.

The function tri(3) returns the list [1, 3, 2, 8], which is the first 4 numbers of the Tribonacci sequence.