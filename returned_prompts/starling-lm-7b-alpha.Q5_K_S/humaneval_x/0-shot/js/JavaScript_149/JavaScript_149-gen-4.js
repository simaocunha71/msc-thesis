function list_sort(lst) {
  return lst.filter(str => str.length % 2 === 0).sort((a, b) => a.length - b.length || a.localeCompare(b));
}

console.assert(list_sort(["aa", "a", "aaa"]) === ["aa"], "Test Case 1 Failed");
console.assert(list_sort(["ab", "a", "aaa", "cd"]) === ["ab", "cd"], "Test Case 2 Failed");


// The filter() method creates a new array with all elements that pass the test implemented by the provided function.

// The sort() method sorts the array in place and returns the sorted array.

// The localeCompare() method compares two strings, locales are optional and return -1, 0, or 1.

// The filter() method returns a new array with all the elements that pass the test implemented by the provided function, and the original array is not modified.

// The filter() method creates a new array with all elements that pass the test implemented by the provided function.

// The sort() method sorts the array in place and returns the sorted array.

// The localeCompare() method compares two strings, locales are optional and return -1, 0, or 1.


// The filter() method returns a new array with all the elements that pass the test implemented by the provided function, and the original array is not modified.

// The filter() method creates a new array with all elements that pass the test implemented by the provided function.

// The sort() method sorts the array in place and returns the sorted array.

// The localeCompare() method compares two strings, locales are optional and return -1, 0, or 1.



// The filter() method returns a new array with all the elements that pass the test implemented by the provided function, and the original array is not modified.

// The filter() method creates a new array with all elements that pass the test implemented by the provided function.

// The sort() method sorts the array in place and returns the sorted array.

// The localeCompare() method compares two strings, locales are optional and return -1, 0, or 1.



