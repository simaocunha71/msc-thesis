/* Filter an input list of strings only for ones that start with a given prefix.
  >>> filterByPrefix([], 'a')
  []
  >>> filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')
  ['abc', 'array']
  */
const filterByPrefix = (strings, prefix) => {
  return strings.filter((str) => str.startsWith(prefix));
};
/* Filter the input list of strings that end with the given suffix.

  >>> filterBySuffix([], '')
  []
  >>> filterBySuffix(['array'], 'de')
  ['array']
  */
const filterBySuffix = (strings, suffix) => {
  return strings.filter((str) => str.endsWith(suffix));
};
/* Filter an input list of strings only for ones that contain a given substring.

  >>> filterBySubstring(['a', 'b'], 'd')
  ['a']
  */
const filterBySubstring = (strings, substring) => {
  return strings.filter((str) => str.indexOf(substring));
};
/* Filter the input list of strings that are a given length away from containing the given substring.

  >>> filterSliceBySubstring([], 'x', [1])
  []
  >>> filterSliceBySubstring(['a'], 'x', [3, 4])
  ['a']
  */
const filterSliceBySubstring = (strings, substring, slice) => {
  return strings.filter((str) => str.slice(0, -1) === str.slice(-1));
};
/* Return a new list of the input set of strings, but only containing unique elements.
*/
const uniqStr = (strings) => strings.uniq();
/* Return all possible combinations or cartesian product of two input lists of strings.
   In case one of those contains an empty string, nothing will be returned.
*/
const cartesianProductOfTwoStringsSets = ([], []) => [];
const cartesianProductOfTwoStringsSets = (input1, input2) => {
  // If the first list is empty or null and the second one is not, return an empty array
  if