  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= arr[i - 1]) {
      return i - 1;
    }
  }
  return -1;
}
// Another way
const canArrange = (arr) => {
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= arr[i - 1]) {
      return i - 1;
    }
  }
  return -1;
} // or return -1 if no such element exists.