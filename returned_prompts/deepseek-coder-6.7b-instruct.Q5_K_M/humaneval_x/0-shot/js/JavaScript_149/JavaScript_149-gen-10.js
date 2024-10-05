  const list_sort = lst.filter(el => el.length % 2 === 0).sort((a, b) => a.length - b.length || a.localeCompare(b));
  return list_sort;
}

console.log(sortedListSum(["aa", "a", "aaa"])) // => ["aa"]
console.log(sortedListSum(["ab", "a", "aaa", "cd"])) // => ["ab", "cd"]

// Time Complexity: O(n log n) because of sorting, where n is the number of elements in the list.
// Space Complexity: O(n) because we are storing the result in a new array.
// The function works by first filtering out strings of odd length, then sorting the remaining strings by length, and then by alphabetical order if the lengths are the same.
// The sort function takes a comparator function that returns a negative, zero, or positive value depending on whether a is less than, equal to, or greater than b.

// The localeCompare method is used here to compare strings in a case-insensitive manner.
// It compares two strings lexicographically and returns a number indicating whether the string in the first parameter is less than, equal to, or greater than the string in the second parameter.
// It's a built-in method in JavaScript for string objects.
// If the reference string comes before or is the same as the given string in sort order, it returns a negative number.
// If the reference string comes after the given string in sort order, it returns a positive number.
// If the two strings are identical, it returns zero.
// This is how we handle the case when two strings have the same length.

// The function then returns the sorted list.

// The function is case sensitive, meaning it will consider 'A' and 'a' as different characters.
// The function will also sort strings of the same length in lexicographic order (dictionary order).
// If the words are of even length, they will be sorted based on their length and then alphabetically.
// If the words are of odd length, they will be ignored.
// The function will return a list of the words sorted based on the criteria mentioned.

// The function uses the