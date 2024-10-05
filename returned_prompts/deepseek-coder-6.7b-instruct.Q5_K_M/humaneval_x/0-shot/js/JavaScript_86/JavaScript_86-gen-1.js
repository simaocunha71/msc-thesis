  return s.split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('');
}

console.log(antiShuffle("Hello World!!!"));

// This function works by first splitting the input string into an array of characters,
// then sorting those characters based on their ASCII values,
// and finally joining the sorted characters back together into a string.

// The sort function is using a custom comparator that subtracts the ASCII value of the second character from the ASCII value of the first.
// If the result is negative, the first character should come before the second in the sorted array.
// If the result is positive, the first character should come after the second in the sorted array.
// If the result is zero, the order of the characters doesn't change.

// This sorting is done in-place, meaning that no new arrays are created and the original array is modified.

// Finally, the sorted string is returned.

// The time complexity of this function is O(n log n), where n is the length of the string.
// The space complexity is O(n), because the function creates a new array of characters to sort.
// This is because JavaScript's built-in sort function uses a sorting algorithm called Timsort, which has a worst-case time complexity of O(n log n).
// The space complexity of Timsort is O(n), so we need to account for that when calculating the space complexity of our function.
// The function also has a constant space complexity of O(1), as it only creates a few variables and doesn't use any data structures that grow with the size of the input.
// Thus, the space complexity of our function is O(1) + O(n) = O(n).

// Here is the javascript version of the code:

const antiShuffle = (s) => {
  return s.split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('');
}

console.log(antiShuffle("Hello World!!!")); // outputs: 'Hello  !!!!Wdlor'
*/

// The function splits the string into an array of characters, sorts the array