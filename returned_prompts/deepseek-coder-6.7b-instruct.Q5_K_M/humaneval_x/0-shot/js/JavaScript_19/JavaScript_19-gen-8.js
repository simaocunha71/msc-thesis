  const words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
  return numbers.split(' ').sort((a, b) => words.indexOf(a) - words.indexOf(b)).join(' ');
}

console.log(sortNumbers('three one five')); // 'one three five'

// This solution splits the input string into an array of words, then sorts it using an indexOf comparison to get the order from the words array. Finally it joins it back into a string.


// An alternative solution that uses a dictionary to map the words to their corresponding numbers, and then sorts based on those numbers:

const sortNumbersAlt = (numbers) => {
  const words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
  const numbersDict = words.reduce((acc, word, idx) => ({ ...acc, [word]: idx }), {});
  return numbers.split(' ').sort((a, b) => numbersDict[a] - numbersDict[b]).join(' ');
}

console.log(sortNumbersAlt('three one five')); // 'one three five'

// Both solutions have the same time complexity O(n log n) due to the sort operation.
```

</div>
</div>

<div class="slide">
<div class="content">

# JavaScript: Map, Filter, Reduce

## Map

`Array.prototype.map()` is a high-order function that returns a new array with the results of calling a provided function on every element in the calling array.

```js
const numbers = [1, 2, 3, 4, 5];
const squares = numbers.map(number => number * number);
console.log(squares); // [1, 4, 9, 16, 25]
```

## Filter

`Array.prototype.filter()` is a high-order function that returns a new array with all elements that pass the test implemented by the provided function.

