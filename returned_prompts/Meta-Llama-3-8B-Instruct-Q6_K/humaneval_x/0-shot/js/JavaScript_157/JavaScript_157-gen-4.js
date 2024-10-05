```
  return Math.pow(a, 2) + Math.pow(b, 2) === Math.pow(c, 2) || 
         Math.pow(a, 2) + Math.pow(c, 2) === Math.pow(b, 2) || 
         Math.pow(b, 2) + Math.pow(c, 2) === Math.pow(a, 2);
```
This function checks if the three sides form a right-angled triangle by using the Pythagorean theorem. It checks if the sum of the squares of the two smaller sides is equal to the square of the largest side. If any of the conditions are true, it returns true, indicating that the three sides form a right-angled triangle. Otherwise, it returns false.