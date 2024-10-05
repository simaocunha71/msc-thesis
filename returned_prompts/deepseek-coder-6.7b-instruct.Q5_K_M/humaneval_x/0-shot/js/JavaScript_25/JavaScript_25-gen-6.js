  let factors = [];
  let divisor = 2;

  while(divisor <= n) {
    if(n % divisor === 0) {
      factors.push(divisor);
      n = n / divisor;
    } else {
      divisor++;
    }
  }

  return factors;
}

console.log(factorize(8)); // [2, 2, 2]
console.log(factorize(25)); // [5, 5]
console.log(factorize(70)); // [2, 5, 7]

/* Explanation:
  The function 'factorize' takes a number 'n' as input and initializes an empty array 'factors' and a variable 'divisor' with a value of 2.
  Then it enters into a loop which continues as long as 'divisor' is less than or equal to 'n'.
  Inside the loop, it checks if 'n' is divisible by 'divisor' with the remainder equal to 0. If it is, it pushes 'divisor' to 'factors' and updates 'n' by dividing it by 'divisor'.
  If 'n' is not divisible by 'divisor', it increments 'divisor' by 1.
  Once the loop is finished, it returns 'factors' array.
*/

module.exports = factorize;

// Time complexity is O(n) because in the worst case scenario it has to iterate through all numbers up to 'n'.
// Space complexity is O(n) because in the worst case scenario it can store 'n' number of factors in 'factors' array.


// Run with Node: node factorize.js
```


## Python Solution

```python
# Python Solution

def factorize(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1

    return factors

print(factorize(8))  # [2, 2, 2]
print(factorize(25