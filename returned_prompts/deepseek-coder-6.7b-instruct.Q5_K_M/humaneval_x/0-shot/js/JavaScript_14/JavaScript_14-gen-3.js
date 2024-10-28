  let prefixes = [];
  for (let i = 0; i < string.length; i++) {
    prefixes.push(string.slice(0, i + 1));
  }
  return prefixes;
}

console.log(allPrefixes('abc')); // ['a', 'ab', 'abc']

// This solution works by creating an empty array `prefixes`. It then loops through each character in the string, adding the prefix of the string up to that character to the `prefixes` array. The function then returns the `prefixes` array.


