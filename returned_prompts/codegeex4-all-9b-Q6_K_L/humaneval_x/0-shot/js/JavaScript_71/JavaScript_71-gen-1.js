To solve this problem, we need to first check if the given sides can form a valid triangle. If the sum of any two sides is greater than the third side, they can form a valid triangle. If not, we return -1.
If the sides can form a valid triangle, we can use Heron's formula to calculate the area of the triangle. Heron's formula states that the area of a triangle with sides of length a, b, and c is:
area = sqrt(s * (s - a) * (s - b) * (s - c))
where s is the semi-perimeter of the triangle, calculated as:
s = (a + b + c) / 2
Here is the complete implementation:
```javascript
const triangleArea = (a, b, c) => {
  // Check if the given sides can form a valid triangle
  if (a + b <= c || a + c <= b || b + c <= a) {
    return -1;
  }
  // Calculate the semi-perimeter
  const s = (a + b + c) / 2;
  // Calculate the area using Heron's formula
  const area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
  // Round the area to 2 decimal points
  return Math.round(area * 100) / 100;
};
```
Let's test the function with the given examples:
```javascript
console.log(triangleArea(3, 4, 5)); // 6.00
console.log(triangleArea(1, 2, 10)); // -1
```
The function should return the expected results.