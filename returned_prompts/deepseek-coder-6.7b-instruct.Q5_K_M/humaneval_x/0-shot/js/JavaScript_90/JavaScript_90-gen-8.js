  if (lst.length < 2) {
    return null;
  }

  let min = Infinity;
  let secondMin = Infinity;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < min) {
      secondMin = min;
      min = lst[i];
    } else if (lst[i] > min && lst[i] < secondMin) {
      secondMin = lst[i];
    }
  }

  return (secondMin == Infinity) ? null : secondMin;
};

console.log(nextSmallest([1, 2, 3, 4, 5]));
console.log(nextSmallest([5, 1, 4, 3, 2]));
console.log(nextSmallest([]));
console.log(nextSmallest([1, 1]));
```

This solution works by iterating through the input list and maintaining two variables, min and secondMin. The min variable stores the smallest number found so far, and the secondMin stores the second smallest number found so far. 

If the current number in the iteration is smaller than min, we update secondMin to be the old min and update min to be the new number. If the current number is not smaller than min, but is smaller than secondMin, we update secondMin. 

Finally, we return secondMin. If we never found a second smallest number (i.e., all numbers are the same), secondMin remains as Infinity and we return null.

The time complexity of this solution is O(n), as we are scanning through the list once. The space complexity is O(1), as we are using a constant amount of space to store min and secondMin.

This solution is efficient and works for all cases.
*/



/*
  TEST CASES
  
  nextSmallest([1, 2, 3, 4, 5]) == 2
  nextSmallest([5, 1, 4, 3, 2]) == 2
  nextSmallest([]) == null
  nextSmallest([1, 1]) == null
*/
