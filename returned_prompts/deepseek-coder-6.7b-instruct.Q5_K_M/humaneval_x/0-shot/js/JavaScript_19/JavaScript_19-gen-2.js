  const words = numbers.split(' ');
  const map = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
  };

  return words.sort((a, b) => map[a] - map[b]).join(' ');
};

console.log(sortNumbers('three one five'));
```

This code works by splitting the input string into an array of words, then mapping each word to its corresponding numerical value. It sorts the array of words based on these values, and finally joins the sorted array back into a string.

The `sort()` function takes a comparator function as an argument that defines the sort order. In this case, the function compares the numerical values of the words by subtracting the numerical value of `b` from the numerical value of `a`.

This will sort the words from smallest to largest numerical value.

Finally, the `join()` function is used to combine the words back into a single string, with each word separated by a space.

This code will output: `one three five`.

It's worth noting that this code assumes the input string is correctly formatted and contains only valid words. If this is not the case, you may want to add some error checking to handle invalid inputs.
