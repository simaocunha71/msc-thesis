  if(lst.length < 2){
    return null;
  }
  let min = Infinity;
  let secondMin = Infinity;

  for(let i = 0; i < lst.length; i++){
    if(lst[i] < min){
      secondMin = min;
      min = lst[i];
    } else if(lst[i] > min && lst[i] < secondMin){
      secondMin = lst[i];
    }
  }

  return secondMin === Infinity ? null : secondMin;
}

console.log(nextSmallest([1, 2, 3, 4, 5])); // 2
console.log(nextSmallest([5, 1, 4, 3, 2])); // 2
console.log(nextSmallest([])); // null
console.log(nextSmallest([1, 1])); // null

```

## Code Explanation:

This code is a function `nextSmallest()` that returns the 2nd smallest element of the list. If there is no such element, the function returns `null`.

The function works by first checking if the list has less than 2 elements. If it does, the function immediately returns `null`.

If the list has 2 or more elements, the function initializes two variables `min` and `secondMin` to `Infinity`. `min` will store the smallest value found so far, and `secondMin` will store the second smallest value found so far.

The function then loops through each element in the list. If it encounters a value that is smaller than the current `min`, it updates `secondMin` to be the current `min`, and then updates `min` to be the new smaller value.

If the function encounters a value that is in between `min` and `secondMin`, it updates `secondMin` to be that new value.

Finally, the function returns `secondMin` if it was updated (i.e., it found a second smallest value), otherwise it returns `null`.

This function works by only checking the list once, making it very efficient.

## Test