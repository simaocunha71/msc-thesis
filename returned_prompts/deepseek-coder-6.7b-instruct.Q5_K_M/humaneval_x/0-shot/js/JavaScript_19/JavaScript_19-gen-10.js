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
  }

  return numbers.split(' ').sort((a, b) => map[a] - map[b]).join(' ');
}

console.log(sortNumbers('three one five')); // 'one three five'

*/

// Solution:
const sortNumbers = (numbers) => {
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
  }

  return numbers.split(' ').sort((a, b) => map[a] - map[b]).join(' ');
}

console.log(sortNumbers('three one five')); // 'one three five'

// Explanation:
// We create an object map which maps the words to their corresponding numbers.
// We split the string of numbers into an array of words.
// We sort this array based on the numbers corresponding to the words using the sort function.
// We join the sorted array back into a string.
// Finally, we return this string.
// This will sort the words in the string from smallest to largest.
// We do this by subtracting the number corresponding to the word b from the number corresponding to the word a, which results in a sorted array.
// We then join the sorted array back into a string and return this string.

// This solution has a time complexity of O(n log n) due to the sort function.
// The space complexity is O(n) because we are creating a new array of words.


// If the words are all lowercase, you can make the sort function case-insensitive by converting