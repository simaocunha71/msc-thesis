```
const getOddCollatz = (n) => {
  const sequence = [n];
  while (n !== 1) {
    if (n % 2 === 0) {
      n = Math.floor(n / 2);
    } else {
      n = n * 3 + 1;
    }
    sequence.push(n);
  }
  return sequence.filter((num) => num % 2 !== 0).sort((a, b) => a - b);
};
```


The solution iterates through the Collatz sequence, filtering out the even numbers and returning the odd numbers sorted in ascending order. 

The function starts by initializing an array `sequence` with the input number `n`. It then enters a while loop that continues until `n` reaches 1. In each iteration, it checks if `n` is even or odd, and updates `n` accordingly. The updated `n` is then pushed onto the `sequence` array.

After the loop, the function filters the `sequence` array to keep only the odd numbers using the `filter` method with a callback function that checks if a number is odd (i.e., `num % 2 !== 0`). The resulting array of odd numbers is then sorted in ascending order using the `sort` method with a callback function that compares two numbers (`a - b`).

The final sorted array of odd numbers is returned as the result. For example, if the input is `5`, the function will return `[1, 5]` as the Collatz sequence for `5` is `[5, 16, 8, 4, 2, 1]`, and the odd numbers in the sequence are `1` and `5`.