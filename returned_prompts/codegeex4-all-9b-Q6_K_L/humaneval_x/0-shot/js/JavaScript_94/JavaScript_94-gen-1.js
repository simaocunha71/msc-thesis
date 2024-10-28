Here is a JavaScript solution for the problem:

```javascript
function isPrime(n) {
    for(let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++)
        if(n % i === 0) return false; 
    return n > 1;
}

function sumDigits(n) {
    return n.toString().split('').reduce((a, b) => a + Number(b), 0);
}

const skjkasdkd = (lst) => {
    let maxPrime = -1;
    for(let i = 0; i < lst.length; i++) {
        if(isPrime(lst[i]) && lst[i] > maxPrime) {
            maxPrime = lst[i];
        }
    }
    return maxPrime === -1 ? -1 : sumDigits(maxPrime);
}
```
In this code, we first define a helper function `isPrime` to check whether a number is prime or not. Then we define another helper function `sumDigits` to calculate the sum of digits of a number. 

In the main function `skjkasdkd`, we initialize `maxPrime` to -1. Then we iterate over the given list. For each number, if it is prime and greater than `maxPrime`, we update `maxPrime`. After the loop, if `maxPrime` is still -1, it means no prime number was found in the list, so we return -1. Otherwise, we return the sum of digits of `maxPrime`.