  if (lst.length < 2) return null;
  let smallest = Infinity;
  let secondSmallest = Infinity;
  
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < smallest) {
      secondSmallest = smallest;
      smallest = lst[i];
    } else if (lst[i] < secondSmallest && lst[i] > smallest) {
      secondSmallest = lst[i];
    }
  }
  
  return (secondSmallest == Infinity) ? null : secondSmallest;
}

console.log(nextSmallest([1, 2, 3, 4, 5])); // 2
console.log(nextSmallest([5, 1, 4, 3, 2])); // 2
console.log(nextSmallest([])); // null
console.log(nextSmallest([1, 1])); // null
```

## Code Explaination:

This code defines a function called `nextSmallest()` which takes a list of integers as an argument. If the list has less than 2 elements, the function returns `null`.

The function initializes two variables: `smallest` and `secondSmallest`, which are used to track the smallest and second smallest numbers in the list.

The function then loops through each element in the list. If the current element is smaller than the current `smallest`, it updates `secondSmallest` to be the current `smallest` and sets `smallest` to be the current element. If the current element is not smaller than `smallest` but is smaller than `secondSmallest`, it updates `secondSmallest` to be the current element.

Finally, the function returns `secondSmallest` if it is not `Infinity` (which means it was updated), and `null` otherwise. This is the second smallest element in the list.

The function is then tested with the provided examples.


# The Code Challenge:

Write a function named `nextLargest()` that returns the 2nd largest element of the list. Return null if there is no such element.


##