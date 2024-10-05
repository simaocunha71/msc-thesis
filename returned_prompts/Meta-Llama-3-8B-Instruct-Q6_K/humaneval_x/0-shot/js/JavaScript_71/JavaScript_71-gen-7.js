```
const triangleArea = (a, b, c) => {
  if (a + b > c && a + c > b && b + c > a) {
    const s = (a + b + c) / 2;
    return (Math.sqrt(s * (s - a) * (s - b) * (s - c))).toFixed(2);
  } else {
    return -1;
  }
};
```

Explanation:

* We first check if the three sides form a valid triangle by checking if the sum of any two sides is greater than the third side.
* If the sides form a valid triangle, we use Heron's formula to calculate the area of the triangle.
* We calculate the semi-perimeter `s` as the average of the three sides.
* We then calculate the area as the square root of `s` times the product of `s` minus each side.
* We use the `toFixed(2)` method to round the area to 2 decimal points.
* If the sides do not form a valid triangle, we return -1.