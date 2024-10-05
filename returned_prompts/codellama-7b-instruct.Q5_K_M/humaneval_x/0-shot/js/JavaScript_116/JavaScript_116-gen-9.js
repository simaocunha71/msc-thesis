const sortArray = (arr) => {
  return arr.sort((a, b) => {
    const countOfOnesA = (a.toString(2).match(/1/g) || []).length;
    const countOfOnesB = (b.toString(2).match(/1/g) || []).length;
    if (countOfOnesA === countOfOnesB) {
      return a - b;
    }
    return countOfOnesA - countOfOnesB;
  });
}
