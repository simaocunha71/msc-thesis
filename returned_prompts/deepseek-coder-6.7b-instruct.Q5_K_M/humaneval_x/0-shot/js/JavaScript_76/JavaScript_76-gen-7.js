  if(n == 1 && x != 1) return false;
  if(n == 0 && x != 0) return false;
  if(n == 1 && x == 1) return true;
  if(x == 0) return true;
  
  while(x > 1){
    if(x % n != 0) return false;
    x /= n;
  }
  return true;
}

console.log(isSimplePower(1, 4)); // true
console.log(isSimplePower(2, 2)); // true
console.log(isSimplePower(8, 2)); // true
console.log(isSimplePower(3, 2)); // false
console.log(isSimplePower(3, 1)); // false
console.log(isSimplePower(5, 3)); // false

//Explanation:
//1. The first four tests are for positive integers. 
//2. In the first test, 4 is a simple power of 2 because 2^2 = 4.
//3. In the second test, 2 is a simple power of 2 because 2^1 = 2.
//4. In the third test, 8 is a simple power of 2 because 2^3 = 8.
//5. In the fourth test, 3 is not a simple power of 2 because there is no integer n such that 2^n = 3.
//6. In the fifth test, 1 is a simple power of any number because any number to the power of 0 is 1.
//7. In the sixth test, 5 is not a simple power of 3 because there is no integer n such that 3^n = 5.

//So, the function isSimplePower(x, n) returns true if x is a simple power of n and false otherwise.
```

## 3. 
```javascript
