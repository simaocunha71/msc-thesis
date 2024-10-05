  const collatz = num => {
    const sequence = [num];
    while (num !== 1) {
      num = num % 2 === 0 ? num / 2 : num * 3 + 1;
      sequence.push(num);
    }
    return sequence;
  };

  const collatzSequence = collatz(n);
  const oddNumbers = collatzSequence.filter(num => num % 2 !== 0);
  return oddNumbers.sort((a, b) => a - b);
};

console.log(getOddCollatz(5));

```

## Solution:
```javascript
function getOddCollatz(n) {
  const collatz = num => {
    const sequence = [num];
    while (num !== 1) {
      num = num % 2 === 0 ? num / 2 : num * 3 + 1;
      sequence.push(num);
    }
    return sequence;
  };

  const collatzSequence = collatz(n);
  const oddNumbers = collatzSequence.filter(num => num % 2 !== 0);
  return oddNumbers.sort((a, b) => a - b);
}

console.log(getOddCollatz(5)); // [1, 5]
```

## Explanation:
The solution includes the `getOddCollatz()` function, which takes a positive integer `n` as its argument. 

Within this function, we define another function `collatz()`. This function, given a number `num`, constructs a Collatz sequence starting from `num`. It does this by iteratively applying the Collatz function (defined within a ternary conditional statement) until reaching 1.

The `getOddCollatz()` function then generates the Collatz sequence for `n` using the `collatz()` function, and filters out the even numbers using the `filter()` method.

Finally, it sorts the remaining numbers in increasing order and returns the sorted array.

The console.log statement at the end tests the `getOddCollatz()` function with the input `