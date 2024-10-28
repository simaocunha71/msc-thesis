  let result = false;
  let i = 0;

  while (!result && i <= Math.abs(a)) {
    if (i * i * i === Math.abs(a)) {
      result = true;
    }
    i++;
  }

  return result;
};

console.log(iscube(1)); // true
console.log(iscube(2)); // false
console.log(iscube(-1)); // true
console.log(iscube(64)); // true
console.log(iscube(0)); // true
console.log(iscube(180)); // false

module.exports = iscube;
```


## Answer Key

```javascript
const iscube = (a) => {
  let low = 0;
  let high = Math.abs(a);

  while (low <= high) {
    let mid = Math.floor((low + high) / 2);
    let cubed = mid * mid * mid;

    if (cubed === Math.abs(a)) {
      return true;
    } else if (cubed < Math.abs(a)) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return false;
};

console.log(iscube(1)); // true
console.log(iscube(2)); // false
console.log(iscube(-1)); // true
console.log(iscube(64)); // true
console.log(iscube(0)); // true
console.log(iscube(180)); // false

module.exports = iscube;
```

This solution uses binary search method to solve the problem. It starts with low = 0 and high = abs(a). Then it calculates the mid value and cube of the mid value. If the cube of the mid value is equal to abs(a), it means a is a cube, so it returns true. If the cube of the mid value is less than abs(a), it means a is still not a cube, so it sets low = mid + 1. If the cube of the mid value is