  const digits = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    let num = arr[i];
    if (num >= 1 && num <= 9) {
      result.push(digits[num]);
    }
  }
  return result;
}
const sortAndReverse = (arr) => {
  arr.sort((a, b) => a - b);
  return arr.reverse();
}
const getNames = (arr) => {
  return byLength(sortAndReverse(arr));
}



