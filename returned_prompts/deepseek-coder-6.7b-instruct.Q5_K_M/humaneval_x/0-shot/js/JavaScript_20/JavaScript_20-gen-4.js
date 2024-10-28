  let sorted = numbers.slice().sort((a, b) => a - b);
  let minDifference = Infinity;
  let result = [];

  for (let i = 0; i < sorted.length - 1; i++) {
    let difference = sorted[i + 1] - sorted[i];

    if (difference < minDifference) {
      minDifference = difference;
      result = [sorted[i], sorted[i + 1]];
    }
  }

  return result;
};

console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

In this script, we are sorting the array of numbers in ascending order and then iterating through the array to find the smallest difference between two consecutive numbers. The pair of numbers with this smallest difference are returned.

The sort method is used to sort the numbers in ascending order. Then, a for loop is used to iterate through the sorted array. Inside the loop, the difference between the current number and the next number is calculated and compared with the current minimum difference. If the difference is smaller, the minimum difference is updated and the pair of numbers is updated as well. Finally, the pair of numbers with the smallest difference is returned.

The complexity of this script is O(n log n) because of the sorting, where n is the length of the array.

The script is written in JavaScript.
































































































































