const countNums = (arr) => {
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    let sum = 0;
    for (let j = 0; j < arr[i].toString().length; j++) {
      sum += arr[i].toString().charAt(j);
    }
    if (sum > 0) {
      count++;
    }
  }
  return count;
};