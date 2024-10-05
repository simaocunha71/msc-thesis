You can solve this problem using a for loop to iterate over the list and check if each number is less than the threshold. Here's the implementation:
```
const belowThreshold = (l, t) => {
  for (let num of l) {
    if (num >= t) {
      return false;
    }
  }
  return true;
};
```
This function iterates over the list `l` using a for...of loop, and for each number `num` in the list, it checks if `num` is greater than or equal to the threshold `t`. If it finds a number that is greater than or equal to the threshold, it immediately returns `false`. If it iterates over the entire list without finding a number that is greater than or equal to the threshold, it returns `true`.

You can test this function with the examples you provided:
```
console.log(belowThreshold([1, 2, 4, 10], 100)); // true
console.log(belowThreshold([1, 20, 4, 10], 5)); // false
```
This function has a time complexity of O(n), where n is the length of the input list, because it iterates over the entire list once. It has a space complexity of O(1), because it only uses a constant amount of space to store the loop variable and the threshold.