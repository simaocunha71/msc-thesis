  const sorted = [...arr].sort((a, b) => a - b);
  const names = [];
  const numbers = [];
  const reverseArr = sorted.reverse();

  for (let i = 0; i < reverseArr.length; i++) {
    if (reverseArr[i] >= 1 && reverseArr[i] <= 9) {
      numbers.push(reverseArr[i]);
    } else {
      names.push(reverseArr[i]);
    }
  }
  const sortedArr = numbers.sort((a, b) => a - b);
  const finalArr = [];

  for (let i = 0; i < sortedArr.length; i++) {
    finalArr.push(names[sortedArr[i] - 1]);
  }
  return finalArr;
};

// console.log(byLength([2, 1, 1, 4, 5, 8, 2, 3]));
// console.log(byLength([]));
// console.log(byLength([1, -1, 55]));

// console.log(byLength([1, -1, 55]));

// console.log(byLength([1, -1, 55]));
