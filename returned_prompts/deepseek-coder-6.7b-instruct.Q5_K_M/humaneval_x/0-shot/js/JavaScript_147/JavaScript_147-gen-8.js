  let count = 0;
  let arr = [];

  //calculate the values of a[i]
  for(let i = 1; i <= n; i++){
      arr.push(i*i - i + 1);
  }

  //check for triples and count where sum is divisible by 3
  for(let i = 0; i < n; i++){
      for(let j = i+1; j < n; j++){
          for(let k = j+1; k < n; k++){
              if((arr[i] + arr[j] + arr[k]) % 3 === 0){
                  count++;
              }
          }
      }
  }

  return count;
};

console.log(getMaxTriples(5)); // 1
```

The time complexity of this code is O(n^3), because there are three nested loops each running n times. 

This is not efficient for large values of n, but it is simple and easy to understand. 

The space complexity is O(n), because we are storing the values of a[i] in an array of size n.

Note: This code assumes that the input is always a positive integer and that n is not too large, as it may not be efficient for large inputs.


## Solution 2:

This solution reduces the time complexity to O(n^2) by keeping track of the frequency of the modulus of the array values when divided by 3. 

```javascript
const getMaxTriples = (n) => {
  let count = 0;
  let freq = [0, 0, 0];

  for(let i = 1; i <= n; i++){
      let val = i*i - i + 1;
      count += freq[(3 - val % 3) % 3];
      freq[val % 3]++;
  }

  return count;
};

console.log(getMaxTriples(5)); // 1
```

The time complexity of this code is O(n), because we are iterating through the array only once. 

The space complexity is O(1),