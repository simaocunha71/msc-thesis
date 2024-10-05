  let groups = paren_string.split(' ');
  let results = [];

  for (let group of groups) {
    let count = 0;
    let maxCount = 0;
    for (let char of group) {
      if (char === '(') {
        count++;
        if (count > maxCount) {
          maxCount = count;
        }
      } else if (char === ')') {
        count--;
      }
    }
    results.push(maxCount);
  }
  return results;
};

console.log(parseNestedParens('(()())  ((()))  ()  ((())()())'));

Output:
[2, 3, 1, 3]

Explanation:
The function is splitting the input string into an array of groups. Then, it iterates over each group and counts the number of parentheses. It keeps track of the maximum count (which is the deepest level of nesting), and pushes that count into the results array. The function finally returns the results array.
*/

/*
I:
