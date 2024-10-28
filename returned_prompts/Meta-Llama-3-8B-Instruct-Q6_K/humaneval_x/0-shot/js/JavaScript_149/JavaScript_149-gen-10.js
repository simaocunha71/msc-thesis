Here is a JavaScript solution for the problem:
```
const list_sort = (lst) => {
  return lst.filter(word => word.length % 2 === 0).sort((a, b) => {
    if (a.length === b.length) {
      return a.localeCompare(b);
    }
    return a.length - b.length;
  });
};
```
Here's an explanation of the code:

1. We use the `filter` method to create a new array that only includes the strings with even lengths. The callback function checks if the length of each string is even by using the modulo operator (`%`).
2. We use the `sort` method to sort the resulting array. The callback function is a comparison function that takes two strings as arguments, `a` and `b`.
3. The comparison function first checks if the lengths of the two strings are equal. If they are, it uses the `localeCompare` method to compare the strings alphabetically.
4. If the lengths are not equal, it returns the difference between the lengths, which will sort the strings by length in ascending order.
5. The `sort` method returns a new sorted array, which is the result of the `list_sort` function.

You can test this function with the examples you provided:
```
console.log(list_sort(["aa", "a", "aaa"])); // Output: ["aa"]
console.log(list_sort(["ab", "a", "aaa", "cd"])); // Output: ["ab", "cd"]
```