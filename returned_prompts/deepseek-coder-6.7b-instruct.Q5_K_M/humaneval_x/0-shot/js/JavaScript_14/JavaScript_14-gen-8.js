  let prefixes = [];
  for (let i = 0; i < string.length; i++) {
    prefixes.push(string.slice(0, i + 1));
  }
  return prefixes;
};

console.log(allPrefixes('abc')); // ['a', 'ab', 'abc']


// alternative solution using Array.from and String.prototype.slice
const allPrefixes2 = (string) => {
  return Array.from({length: string.length}, (_, i) => string.slice(0, i + 1));
}

console.log(allPrefixes2('abc')); // ['a', 'ab', 'abc']




