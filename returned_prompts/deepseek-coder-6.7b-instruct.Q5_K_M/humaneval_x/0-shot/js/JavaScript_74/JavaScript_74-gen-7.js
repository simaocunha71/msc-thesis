  let totalCharsInLst1 = lst1.reduce((total, word) => total + word.length, 0);
  let totalCharsInLst2 = lst2.reduce((total, word) => total + word.length, 0);
  
  return totalCharsInLst1 < totalCharsInLst2 ? lst1 : lst2;
}

console.log(totalMatch([], [])); // ➞ []
console.log(totalMatch(['hi', 'admin'], ['hI', 'Hi'])); // ➞ ['hI', 'Hi']
console.log(totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])); // ➞ ['hi', 'admin']
console.log(totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi'])); // ➞ ['hI', 'hi', 'hi']
console.log(totalMatch(['4'], ['1', '2', '3', '4', '5'])); // ➞ ['4']

```


This function works by first calculating the total number of characters in each list by reducing the list to the total sum of character counts. Then it returns the list with the smaller total character count. If the two lists have the same total character count, it returns the first list.

It uses the `reduce()` method to calculate the total character count for each list. The `reduce()` method takes a callback function that is called for each element in the array, and a starting value (in this case 0). The callback function takes the accumulated total and the current element, and returns the new total. This process is repeated for all elements in the array, resulting in the total character count for the list.

Finally, it compares the total character counts and returns the list with the smaller count. If the counts are equal, it returns the first list.
*/

```

































































