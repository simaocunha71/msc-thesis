  let sum = 0;
  for (let i = 0; i < k; i++) {
    if (String(arr[i]).length <= 2) {
      sum += arr[i];
    } else {
      break;
    }
  }
  return sum;
}  // or
const addElements = (arr, k) => {
  return arr.slice(0, k).filter(x => String(x).length <= 2).reduce((a, b) => a + b, 0);
}  // or
const addElements = (arr, k) => {
  let sum = 0;
  for (let i = 0; i < k && String(arr[i]).length <= 2; i++) {
    sum += arr[i];
  }
  return sum;
}  // or
const addElements = (arr, k) => {
  let sum = 0;
  for (let i = 0; i < k; i++) {
    if (String(arr[i]).length > 2) {
      break;
    }
    sum += arr[i];
  }
  return sum;
}  // or
const addElements = (arr, k) => {
  return arr.slice(0, Math.min(k, arr.length)).filter(x => String(x).length <= 2).reduce((a, b) => a + b, 0);
}  // or
const addElements = (arr, k) => {
  return [...arr.slice(0, k)].reduce((a, b) => String(b).length <= 2 ? a + b : a, 0);
}  // or
const addElements = (arr, k) => {
  let sum = 0;
  for (let i = 0; i < k; i++) {
    if (String(arr[i]).length <= 2) {
      sum += arr[i];
    } else {
      break;
    }
  }
  return sum;
}  // or
const addElements = (arr, k) => {
  return arr.slice(0, k).reduce((a, b) => a + (String(b).length <= 2 ? b : 0), 0);
}  // or
const addElements = (arr, k) => {
  return arr.slice(0, k).filter(x => String(x).length <= 2).reduce((a, b) => a + b,