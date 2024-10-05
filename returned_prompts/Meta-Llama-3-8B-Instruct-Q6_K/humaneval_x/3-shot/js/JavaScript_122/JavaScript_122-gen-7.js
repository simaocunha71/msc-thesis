  let sum = 0;
  for (let i = 0; i < k; i++) {
    let num = arr[i];
    if (String(num).length <= 2) {
      sum += num;
    }
  }
  return sum;
}
// or
const addElements = (arr, k) => {
  return arr.slice(0, k).reduce((sum, num) => sum + (String(num).length <= 2 ? num : 0), 0);
}