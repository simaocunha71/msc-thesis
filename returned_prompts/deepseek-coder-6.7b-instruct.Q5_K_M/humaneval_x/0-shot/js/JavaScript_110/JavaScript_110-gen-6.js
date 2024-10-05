  // Create a boolean to check if all elements in lst1 are even
  let allEven = lst1.every(num => num % 2 === 0);

  // If all elements in lst1 are even, return "YES"
  if (allEven) {
    return "YES";
  }

  // If not, check each element in lst1 and lst2
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 !== 0) {
      for (let j = 0; j < lst2.length; j++) {
        // If lst2 has an even element, exchange them and break the loop
        if (lst2[j] % 2 === 0) {
          let temp = lst1[i];
          lst1[i] = lst2[j];
          lst2[j] = temp;
          break;
        }
      }
    }
  }

  // After the exchange, check if all elements in lst1 are even
  allEven = lst1.every(num => num % 2 === 0);

  // If all elements in lst1 are even, return "YES". Otherwise, return "NO".
  return allEven ? "YES" : "NO";
};

// Test cases
console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])); // "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])); // "NO"

```

## 2. Array Reduce

```javascript

// Define an array of numbers
let nums = [1, 2, 3, 4, 5];

// Use the reduce method to sum all the numbers in the array
let sum = nums.reduce((total, num) => {
  return total + num;
}, 0);

// Print the sum
console.log(sum); // Outputs: 15

```

## 