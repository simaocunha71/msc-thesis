  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= arr[i - 1]) {
      return i - 1;
    }
  }
  return -1;
}
// or
const canArrange = (arr) => {
  for (let i = arr.length - 2; i >= 0; i--) {
    if (arr[i + 1] <= arr[i]) {
      return i;
    }
  }
  return -1;
}