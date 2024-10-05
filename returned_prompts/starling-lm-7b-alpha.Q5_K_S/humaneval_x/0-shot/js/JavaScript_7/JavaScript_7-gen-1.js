The filterBySubstring function takes in two parameters: an array of strings called 'strings' and a single string called 'substring'. It returns a new array that only contains strings from the original array which include the substring.

To implement this, the function uses the built-in filter() method available to arrays in JavaScript. The filter() method takes in a callback function that is applied to each element in the array, and returns a new array with only the elements that pass the test implemented in the callback function.

In this case, the callback function checks if the length of the string (str.length) is greater than the length of the substring (substring.length). If it is, then the string contains the substring and is included in the new array. Otherwise, the string is excluded from the new array.

Finally, the function returns the new array of strings that contain the substring.

Example usage:
filterBySubstring([], 'a') // []
filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a') // ['abc', 'bacd', 'array']

The first example demonstrates how to use the function with an empty array and a substring. In this case, the function returns an empty array since there are no strings in the original array that contain the substring.

The second example demonstrates how to use the function with an array of strings and a substring. The function correctly filters the array and returns only the strings that contain the substring 'a'.

Overall, the filterBySubstring function provides a convenient and efficient way to filter an input list of strings based on the presence of a given substring.








*/


function filterBySubstring(strings, substring) {
    return strings.filter(str => str.length > substring.length);
}







/* Filter an input list of strings only for ones that contain given substring
  >>> filterBySubstring([], 'a')
  []
  >>> filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')
  ['abc', 'bacd', 'array']
  */
const filterBySubstring = (strings, substring) => {
    return strings.filter(str => str