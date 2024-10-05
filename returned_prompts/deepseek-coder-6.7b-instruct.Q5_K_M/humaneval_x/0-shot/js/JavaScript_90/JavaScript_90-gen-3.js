  if(lst.length < 2) return null;
  lst.sort((a, b) => a - b);
  let smallest = lst[0];
  for(let i = 1; i < lst.length; i++){
    if(lst[i] > smallest) return lst[i];
  }
  return null;
}

console.log(nextSmallest([1, 2, 3, 4, 5])) // 2
console.log(nextSmallest([5, 1, 4, 3, 2])) // 2
console.log(nextSmallest([])) // null
console.log(nextSmallest([1, 1])) // null
```

#### Solution Explanation:
First, we check if the length of the list is less than 2. If yes, we return null as there is no 2nd smallest element in such cases.

Then we sort the list in ascending order.

We initialize the smallest element to the first element in the list.

We then loop through the rest of the list, starting from the second element. For each element, if it is greater than the smallest element, we return it as the 2nd smallest element.

If we reach the end of the list without finding a greater element, we return null as there is no 2nd smallest element.

#### Complexity Analysis:
The time complexity of this solution is O(n log n) due to the sorting operation.
The space complexity is O(1), as we are not using any additional space that scales with the input size.

#### Note:
This solution assumes that the list contains distinct integers. If the list can contain duplicates, we would need to modify the solution to handle that case.

#### Solution:
If the list can contain duplicates, we can modify the solution as follows:

```javascript
const nextSmallest = (lst) => {
  if(lst.length < 2) return null;
  lst.sort((a, b) => a - b);
  let smallest = lst[0];
  for(let i = 1; i < lst.length; i++){
    if(lst[i] > smallest &&