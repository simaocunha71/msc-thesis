/* Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
  >>> intersperse([], 4)
  []
  >>> intersperse([1, 2, 3], 4)
  [1, 4, 2, 4, 3]
  */
const intersperse = (numbers, delimeter) => {
    const len = numbers.length;
    let result = [];

    if(isNaN(delimeter)) throw new TypeError(`delimeter is not a number.`);

    for (let i = 0; i < len - 1; i++) {
        result[i] = numbers[i];
    }

    // If the last element doesn't equal `delimeter` we need to add it.
    if(numbers[len - 1] !== delimeter) {
      result[result.length - 1] = delimeter;
    }

    return result;
};
