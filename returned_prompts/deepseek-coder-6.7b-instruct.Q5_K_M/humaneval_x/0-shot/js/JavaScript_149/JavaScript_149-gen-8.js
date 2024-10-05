  // Filter out the strings with odd lengths
  let evenLengthStrings = lst.filter(str => str.length % 2 === 0);

  // Sort the strings by length and alphabetically
  evenLengthStrings.sort((a, b) => a.length - b.length || a.localeCompare(b));

  return evenLengthStrings;
}

// Test the function with some examples
console.log(sortedListSum(["aa", "a", "aaa"]))  // should print ["aa"]
console.log(sortedListSum(["ab", "a", "aaa", "cd"]))  // should print ["ab", "cd"]


