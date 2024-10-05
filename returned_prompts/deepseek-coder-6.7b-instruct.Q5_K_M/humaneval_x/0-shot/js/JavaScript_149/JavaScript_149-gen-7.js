  let result = lst.filter(word => word.length % 2 === 0);
  result = result.sort((a, b) => a.length - b.length || a.localeCompare(b));
  return result;
};

console.log(sortedListSum(["aa", "a", "aaa"])); //["aa"]
console.log(sortedListSum(["ab", "a", "aaa", "cd"])); //["ab", "cd"]

/*In this function, we first filter out the elements of the list that have an odd length. 
Then we sort the elements of the list. If two elements have the same length, 
we sort them alphabetically using the 'localeCompare' function. 
Finally, we return the sorted list.
*/
```

## Task 2

```python
