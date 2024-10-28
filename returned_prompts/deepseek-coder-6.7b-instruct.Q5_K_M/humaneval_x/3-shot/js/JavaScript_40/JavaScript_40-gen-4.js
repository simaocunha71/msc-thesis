  for  (let i  in l) {
    for  (let j  in l) {
      for  (let k  in l) {
        if  (i  !=  j  && j  !=  k  && k  !=  i) {
          if  (l[i]  +  l[j]  +  l[k]  == 0) {
            return true;
           }
         }
       }
     }
   }

  return false;
}
```

## 5.16.2

```javascript
/*
  Given a list of integers, find out if the sum of any two numbers in the list
  is divisible by 5.
  If it is, return the sum. If not, return an empty list.

  Example:
  sumDivisibleByFive([1, 2, 3, 4, 5]) => [5]
  sumDivisibleByFive([1, 2, 3, 4, 6]) => []
  sumDivisibleByFive([10, 20, 30]) => [30]
  sumDivisibleByFive([1, 2, 3, 4, 10]) => [10]
*/

const sumDivisibleByFive = (nums) => {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if ((nums[i] + nums[j]) % 5 === 0) {
        return [nums[i] + nums[j]];
      }
    }
  }
  return [];
};

console.log(sumDivisibleByFive([1, 2, 3, 4, 5])); // [5]
console.log(sumDivisibleByFive([1, 2, 3, 4, 6])); // []
console.log(sumDivisibleByFive([10, 20, 30])); // [30]
console.log(sumDivisibleByFive([1, 2,