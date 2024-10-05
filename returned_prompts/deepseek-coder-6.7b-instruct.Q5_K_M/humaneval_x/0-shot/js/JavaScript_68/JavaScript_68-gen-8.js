  if (arr.length === 0) return [];

  let smallestEvenVal = Infinity;
  let smallestEvenIndex = -1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < smallestEvenVal && arr[i] % 2 === 0) {
      smallestEvenVal = arr[i];
      smallestEvenIndex = i;
    }
  }

  return smallestEvenIndex !== -1 ? [smallestEvenVal, smallestEvenIndex] : [];
};

console.log(pluck([4, 2, 3])); // [2, 1]
console.log(pluck([1, 2, 3])); // [2, 1]
console.log(pluck([])); // []
console.log(pluck([5, 0, 3, 0, 4, 2])); // [0, 1]

//Time complexity O(n) where n is the length of the array because we loop through the array once.
//Space complexity is O(1) as we are using a constant amount of space to store our variables.
```

### 15. [Unique Elements](https://www.codewars.com/kata/59f11118a5e129e591000134/train/javascript)

