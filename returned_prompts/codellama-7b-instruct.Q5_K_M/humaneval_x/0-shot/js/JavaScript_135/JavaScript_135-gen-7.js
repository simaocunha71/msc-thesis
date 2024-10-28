const canArrange = (arr) => {
  let currentMax = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > currentMax) {
      currentMax = arr[i];
    }
  }
  let currentMaxIndex = -1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === currentMax) {
      currentMaxIndex = i;
    }
  }
  return currentMaxIndex;
}