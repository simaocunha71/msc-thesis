  return strings.filter(str => str.startsWith(prefix));

};

console.log(filterByPrefix([], 'a')); // []
console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')); // ['abc', 'array']
console.log(filterByPrefix(["Alice", "Bob", "Charlie", "Alpha"], "Al")); // ['Alice', 'Alpha']
console.log(filterByPrefix(["dog", "door", "car", "cat"], "do")); // ['dog', 'door']

*/


/*
