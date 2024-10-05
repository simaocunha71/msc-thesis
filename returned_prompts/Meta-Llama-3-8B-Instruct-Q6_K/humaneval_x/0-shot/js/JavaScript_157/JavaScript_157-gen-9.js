```
const rightAngleTriangle = (a, b, c) => {
  // Pythagorean theorem: a^2 + b^2 = c^2 for a right-angled triangle
  return Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2)) === c || 
         Math.sqrt(Math.pow(a, 2) + Math.pow(c, 2)) === b || 
         Math.sqrt(Math.pow(b, 2) + Math.pow(c, 2)) === a;
};
```


This function uses the Pythagorean theorem to check if the three sides form a right-angled triangle. The theorem states that for a right-angled triangle, the square of the hypotenuse side is equal to the sum of squares of the other two sides. The function checks all three combinations of the sides and returns true if any of them satisfy the theorem, and false otherwise. 

Please note that this solution assumes that the input values are valid (i.e., they form a valid triangle). In a real-world application, you would need to add error checking to handle invalid inputs. 

Also, the function uses the `Math.pow` and `Math.sqrt` functions to perform the calculations. The `Math.pow` function raises its first argument to the power of its second argument, and the `Math.sqrt` function returns the square root of its argument. 

You can test this function with the examples provided in the problem statement:
```
console.log(rightAngleTriangle(3, 4, 5)); // true
console.log(rightAngleTriangle(1, 2, 3)); // false
```


This solution has a time complexity of O(1) because it performs a constant number of operations regardless of the input size. It also has a space complexity of O(1) because it only uses a constant amount of space to store the function's variables and the result. 