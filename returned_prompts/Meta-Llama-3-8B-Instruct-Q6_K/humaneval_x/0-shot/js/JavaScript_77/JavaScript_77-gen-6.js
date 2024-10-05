```javascript
const iscube = (a) => {
  for (let i = 1; Math.pow(i, 3) <= a; i++) {
    if (Math.pow(i, 3) === a) {
      return true;
    }
  }
  return false;
};
```
This function iterates through all possible cube numbers (i^3) starting from 1 and checks if it is equal to the input number a. If it finds a match, it returns true. If it doesn't find a match after checking all possible cube numbers, it returns false.

Note: This function has a time complexity of O(sqrt(n)) due to the calculation of i^3 and Math.pow(i, 3). This is because the number of iterations is proportional to the square root of the input number a. For large input numbers, this function may be slow. If you need a more efficient solution, you can use a different approach, such as using a hash table to store the cube numbers and checking if the input number is in the hash table.