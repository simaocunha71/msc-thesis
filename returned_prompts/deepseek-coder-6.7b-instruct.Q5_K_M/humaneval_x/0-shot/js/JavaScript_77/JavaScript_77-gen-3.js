  let result = false;
  let start = 0;
  let end = Math.abs(a);

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    let cube = mid * mid * mid;

    if (cube === Math.abs(a)) {
      result = true;
      break;
    } else if (cube < Math.abs(a)) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }

  return result;
};

console.log(iscube(1)); // true
console.log(iscube(2)); // false
console.log(iscube(-1)); // true
console.log(iscube(64)); // true
console.log(iscube(0)); // true
console.log(iscube(180)); // false

```

#### Explanation

This function uses the binary search approach to solve the problem. It starts by calculating the cube of the mid value between start and end. If this cube is equal to the absolute value of the input number a, then it returns true. If the cube is less than a, it adjusts the start value to be one more than the mid value. If the cube is greater than a, it adjusts the end value to be one less than the mid value. The process continues until the start value is greater than the end value, which means the number a is not a cube of any integer.

In the end, if the function has not returned true, it means that a is not a cube of any integer, so it returns false.

This function works for negative numbers as well, because it takes the absolute value of the input number before calculating the cube.

The time complexity of this function is O(log(n)) because it uses binary search, where n is the absolute value of the input number.

The space complexity of this function is O(1) because it uses a constant amount of space to store the start, end, mid, and cube values.

This function is useful for checking if a given number is a cube of some integer.

```

```

```

```

