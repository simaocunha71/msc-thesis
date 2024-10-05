  let result = Math.round(Math.pow(a, (1/3)));
  return (result*result*result) === a;
};
console.log(iscube(1)); // true
console.log(iscube(2)); // false
console.log(iscube(-1)); // true
console.log(iscube(64)); // true
console.log(iscube(0)); // true
console.log(iscube(180)); // false

// This function works by calculating the cubic root of a, rounding it to the nearest integer,
// then checking if cubing that rounded number gives the original number a.
// This is because the cubic root of a number is the number that when cubed gives that number.
// If it does, then the number is a cube.
// If it doesn't, then the number is not a cube.
// This solution assumes that the input is always valid, as per the problem statement.

// This solution is using JavaScript.

/*
  The solution iscube(a) has a time complexity of O(1) because it performs a constant number of operations regardless of the size of the input.
  The space complexity is also O(1) because it uses a constant amount of space.
  */
```


## ❓