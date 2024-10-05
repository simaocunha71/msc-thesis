  if(arr.length === 0) return true;
  
  let count = 0;
  
  for(let i = 0; i < arr.length - 1; i++) {
    if(arr[i] > arr[i + 1]) count++;
  }
  
  if(arr[arr.length - 1] > arr[0]) count++;
  
  return count <= 1;
};

console.log(moveOneBall([3, 4, 5, 1, 2])) // true
console.log(moveOneBall([3, 5, 4, 1, 2])) // false
console.log(moveOneBall([])) // true

/*
  This function works by counting the number of places where the array is not 
  in non-decreasing order. If the number of such places is more than 1, it 
  returns false. If the array is already in non-decreasing order, it returns true. 
  If the last element of the array is larger than the first one, it is counted as 
  a violation as well. In all cases, the function returns whether the number of 
  violations is less than or equal to 1.
*/
```

**Explanation:**

In the first example, by performing 2 right shift operations, we can get the array sorted in non-decreasing order.
In the second example, no matter how many right shift operations we perform, we cannot get the array sorted in non-decreasing order.
In the third example, the array is already sorted, so we return true.

**Time Complexity:**

O(N)

**Space Complexity:**

O(1)

**Test Cases:**

```javascript
console.log(moveOneBall([3, 4, 5, 1, 2])) // true
console.log(moveOneBall([3, 5, 4, 1, 2])) // false
console.log(moveOneBall([])) // true
console.log(moveOneBall([1, 2, 3, 4, 5])) // true
console.