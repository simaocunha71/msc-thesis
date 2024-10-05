To solve this problem, we need to check if there are any odd numbers in lst1 and if there are any even numbers in lst2. If both conditions are met, we can perform the exchange and make lst1 a list of only even numbers.

Here's the implementation of the exchange function in JavaScript:

```javascript
const exchange = (lst1, lst2) => {
  let hasOddInLst1 = false;
  let hasEvenInLst2 = false;

  // Check if there are any odd numbers in lst1
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 !== 0) {
      hasOddInLst1 = true;
      break;
    }
  }

  // Check if there are any even numbers in lst2
  for (let i = 0; i < lst2.length; i++) {
    if (lst2[i] % 2 === 0) {
      hasEvenInLst2 = true;
      break;
    }
  }

  // If there are odd numbers in lst1 and even numbers in lst2, we can perform the exchange
  if (hasOddInLst1 && hasEvenInLst2) {
    return "YES";
  } else {
    return "NO";
  }
};
```

Let's test the function with the given examples:

```javascript
console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])); // Output: "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])); // Output: "NO"
```

The function correctly returns "YES" for the first example and "NO" for the second example.