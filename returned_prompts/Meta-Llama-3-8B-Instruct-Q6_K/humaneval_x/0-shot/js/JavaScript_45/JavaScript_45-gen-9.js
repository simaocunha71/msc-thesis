```javascript
const triangleArea = (a, h) => (a * h) / 2;
```

Explanation:
The area of a triangle can be calculated using the formula `(base * height) / 2`, where `base` is the length of one side and `height` is the height of the triangle. In this case, we are given the length of a side (`a`) and the height (`h`), so we can plug these values into the formula and return the result. The `=>` symbol is used to define an arrow function, which is a shorthand for a function that takes one argument and returns a value. In this case, the function takes two arguments (`a` and `h`) and returns the result of the area calculation. The `triangleArea` function can be called with two arguments, like this: `triangleArea(5, 3)`, which would return the area of a triangle with a base of 5 and a height of 3.