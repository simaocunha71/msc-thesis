  return strings.filter(string => string.startsWith(prefix));
}
console.log(filterByPrefix([], 'a')); // []
console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')); // ['abc', 'array']
*/

// Solution:
const filterByPrefix = (strings, prefix) => {
  return strings.filter(string => string.startsWith(prefix));
}
console.log(filterByPrefix([], 'a')); // []
console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')); // ['abc', 'array']

// Alternative Solution:
const filterByPrefix = (strings, prefix) => {
  return strings.filter(string => string.indexOf(prefix) === 0);
}
console.log(filterByPrefix([], 'a')); // []
console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')); // ['abc', 'array']

// Alternative Solution:
const filterByPrefix = (strings, prefix) => {
  return strings.filter(string => ~string.indexOf(prefix));
}
console.log(filterByPrefix([], 'a')); // []
console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')); // ['abc', 'array']
*/

// Solution:
const filterByPrefix = (strings, prefix) => {
  return strings.filter(string => string.startsWith(prefix));
}
console.log(filterByPrefix([], 'a')); // []
console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')); // ['abc', 'array']

// Alternative Solution:
const filterByPrefix = (strings, prefix) => {
  return strings.filter(string => string.indexOf(prefix) === 0);
}
console.log(filterByPrefix([], 'a')); // []
console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')); // ['abc', 'array']

// Alternative Solution:
const filter