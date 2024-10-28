  // Calculate integer power of n
  let power = n;
  for(let i = 1; i < x; i++) {
    power *= n;
  }
  
  // Check if calculated power is equal to x
  return power === x;
}

console.log(isSimplePower(1, 4)) // true
console.log(isSimplePower(2, 2)) // true
console.log(isSimplePower(8, 2)) // true
console.log(isSimplePower(3, 2)) // false
console.log(isSimplePower(3, 1)) // false
console.log(isSimplePower(5, 3)) // false

*/


A: Here is the solution:

```javascript
const isSimplePower = (x, n) => {
  if(x === n)
    return true;

  let power = n;
  for(let i = 1; i < x; i++) {
    power *= n;
    if(power === x)
      return true;
    if(power > x || power < 0) // If power exceeds x or becomes negative, break the loop
      break;
  }
  return false;
}

console.log(isSimplePower(1, 4)) // true
console.log(isSimplePower(2, 2)) // true
console.log(isSimplePower(8, 2)) // true
console.log(isSimplePower(3, 2)) // false
console.log(isSimplePower(3, 1)) // false
console.log(isSimplePower(5, 3)) // false
```

This function first checks if n and x are equal. If they are, it immediately returns true because n^0 is always 1, and x is 1.

Then it calculates the power of n and checks if it equals to x. If it does, the function returns true. If not, the function continues with the next power.

The loop breaks if the power exceeds x or becomes negative. This is because in the next step, the power will just increase even more and exceed x. It also prevents negative numbers from being processed which is not possible for positive integers.

Finally