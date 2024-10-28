Here is one way to approach this problem:

1. Create an empty Set called seen. This set will be used to store all the unique elements we find.
2. Use a for loop to iterate through the list l. For each element in the list, check if it is already in the seen set.
  * If the element is already in the seen set, it means we've seen it before, so we skip it.
  * If the element is not in the seen set, it means it's unique, so we add it to the set using the add() method.
3. After iterating through the entire list, the seen set will contain all the unique elements in the list.
4. Convert the seen set back to an array using the spread syntax (...seen) and sort the array in ascending order using the sort() method.
5. Return the sorted array.

Here's the code that implements this approach:

```javascript
const unique = (l) => {
  const seen = new Set();
  l.forEach(el => {
    seen.add(el);
  });
  return [...seen].sort((a, b) => a - b);
};
```

In this code, we define a function called `unique` that takes in a list `l` as its parameter. We create a new Set called `seen` to store all the unique elements.

Next, we use the `forEach` method to iterate through each element in the list. For each element, we use the `add` method to add it to the `seen` set. Since a Set only allows unique values, duplicate elements will be automatically ignored.

After iterating through the entire list, we convert the `seen` set back to an array using the spread syntax (`[...seen]`). This creates a new array containing all the unique elements in the original list.

Finally, we sort the array in ascending order using the `sort` method and a simple comparison function `(a, b) => a - b`. This function compares two elements `a` and `b` and returns a negative value if `a` should be sorted before `b`, a positive value if `a` should be sorted after `b`, or 0 if `a` and `b` are equal.

Overall, this