  if (lst.length <= 1) {
    return null;
  }

  let smallest = Number.MAX_SAFE_INTEGER;
  let secondSmallest = Number.MAX_SAFE_INTEGER;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < smallest) {
      secondSmallest = smallest;
      smallest = lst[i];
    } else if (lst[i] < secondSmallest && lst[i] > smallest) {
      secondSmallest = lst[i];
    }
  }

  return secondSmallest === Number.MAX_SAFE_INTEGER ? null : secondSmallest;
}

console.log(nextSmallest([1, 2, 3, 4, 5])) // 2
console.log(nextSmallest([5, 1, 4, 3, 2])) // 2
console.log(nextSmallest([])) // null
console.log(nextSmallest([1, 1])) // null


This is a JavaScript solution.
The function first checks if the length of the list is less than or equal to 1. If it is, it returns null as there is no second smallest element in this case.
Then, it initializes two variables smallest and secondSmallest with a large number. These will hold the smallest and the second smallest elements found in the list.
Then, it iterates through the list. If it finds an element that is smaller than the current smallest, it updates the second smallest to be the current smallest and updates the smallest to be the new element.
If it finds an element that is between the smallest and second smallest, it updates the second smallest to be this new element.
Finally, it returns the second smallest element. If it never found a second smallest element, it returns null.
*/

/*
Time complexity: O(n)
Space complexity: O(1)
*/




























































