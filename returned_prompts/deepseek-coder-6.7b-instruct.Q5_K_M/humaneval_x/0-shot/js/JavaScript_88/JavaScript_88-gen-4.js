  const sum = array[0] + array[array.length - 1];
  const sortedArray = [...array].sort((a, b) => a - b);

  return (sum % 2 === 0) ? sortedArray.reverse() : sortedArray;
};

console.log(sortArray([])); // []
console.log(sortArray([5])); // [5]
console.log(sortArray([2, 4, 3, 0, 1, 5])); // [0, 1, 2, 3, 4, 5]
console.log(sortArray([2, 4, 3, 0, 1, 5, 6])); // [6, 5, 4, 3, 2, 1, 0]

/*
  The function works by first calculating the sum of the first and last elements of the input array.
  It then sorts a copy of the array in ascending order.
  If the sum is even, it reverses the sorted array to get a descending order, otherwise it returns the sorted array as is.
*/
```

## Credits

Found on Edabit: [Sort an Array According to the Sum of its First and Last Elements](https://edabit.com/challenge/K7KFkA6h3vJL52R7H)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

[@devanshbatham](https://github.com/devanshbatham)

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/devanshbatham)
