  const result = [];
  let current = n;

  while (current > 0) {
    result.push(current);
    current = (current % 2 === 0) ? current + 1 : current + 2;
  }

  return result;
};

makeAPile(3); // [3, 5, 7]

/*
  Given an array of strings, create a dictionary of unique strings from the input.
  The keys in the dictionary should be unique strings from the input array.
  The values of the dictionary should be the count of occurrence of the unique string in the array.

  Examples:
  >>> countUniqueStrings(["cat", "dog", "cat", "bird"])
  {'cat': 2, 'dog': 1, 'bird': 1}
  >>> countUniqueStrings(["dog", "cat"])
  {'dog': 1, 'cat': 1}
  >>> countUniqueStrings(["cat"])
  {'cat': 1}
  >>> countUniqueStrings([])
  {}
  */
const countUniqueStrings = (array) => {
  const result = {};

  array.forEach(str => {
    if (result[str]) {
      result[str] += 1;
    } else {
      result[str] = 1;
    }
  });

  return result;
};

countUniqueStrings(["cat", "dog", "cat", "bird"]); // {'cat': 2, 'dog': 1, 'bird': 1}
countUniqueStrings(["dog", "cat"]); // {'dog': 1, 'cat': 1}
countUniqueStrings(["cat"]); // {'cat': 1}
countUniqueStrings([]); // {}

/*
  Given a string, return the lexicographically smallest sub-string of length k from the given string.

  Examples:
  >>> smallestSubstring(["cat", 3])
  "cat"
  >>> smallestSubstring(["dog", 3])
  "ogd"
  >>> smallestSubstring(["hello", 4])
  "hell"
  >>> smallestSubstring(["python", 2])
  "py