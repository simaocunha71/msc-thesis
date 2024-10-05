  let parenArray = paren_string.split(' ');
  let maxNestedArray = [];

  parenArray.forEach((parenGroup) => {
    let count = 0;
    let maxCount = 0;
    for (let i = 0; i < parenGroup.length; i++) {
      if (parenGroup[i] === "(") {
        count++;
      } else if (parenGroup[i] === ")") {
        count--;
      }
      if (count > maxCount) {
        maxCount = count;
      }
    }
    maxNestedArray.push(maxCount);
  });

  return maxNestedArray;
};

console.log(parseNestedParens('(()())  ((()))  ()  ((())()())'));
// Output: [2, 3, 1, 3]

*/

const parseNestedParens = (paren_string) => {
  let parenArray = paren_string.split(' ');
  let maxNestedArray = [];

  parenArray.forEach((parenGroup) => {
    let count = 0;
    let maxCount = 0;
    for (let i = 0; i < parenGroup.length; i++) {
      if (parenGroup[i] === "(") {
        count++;
      } else if (parenGroup[i] === ")") {
        count--;
      }
      if (count > maxCount) {
        maxCount = count;
      }
    }
    maxNestedArray.push(maxCount);
  });

  return maxNestedArray;
};

console.log(parseNestedParens('(()())  ((()))  ()  ((())()())'));
// Output: [2, 3, 1, 3]





































































