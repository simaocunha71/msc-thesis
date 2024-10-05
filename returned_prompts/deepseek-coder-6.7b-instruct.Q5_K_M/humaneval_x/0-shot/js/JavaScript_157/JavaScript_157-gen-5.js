  let sides = [a, b, c].sort((a, b) => a - b);
  return Math.pow(sides[0], 2) + Math.pow(sides[1], 2) === Math.pow(sides[2], 2);
};

console.log(rightAngleTriangle(3, 4, 5)); // true
console.log(rightAngleTriangle(1, 2, 3)); // false

/*
  The function sorts the sides and then checks if the square of the smallest side
  (which is sides[0]) plus the square of the middle side (sides[1]) is equal to the
  square of the largest side (sides[2]). This is the Pythagorean theorem.
  If it is, then we have a right-angled triangle.
 */
```

**Solution 2:**

```javascript
