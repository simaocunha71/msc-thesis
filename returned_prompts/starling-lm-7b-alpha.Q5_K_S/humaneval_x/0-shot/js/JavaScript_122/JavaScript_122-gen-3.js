while (k--) {
  let num = arr.shift();
  if (num < 100) {
    A;
  }
}
return arr.reduce((acc, curr) => acc + curr, 0);
};


B:
const addElements = (arr, k) => {
  return arr.slice(0, k).filter(num => num < 100).reduce((acc, curr) => acc + curr, 0);
};


C:
const addElements = (arr, k) => {
  let sum = 0;
  for (let i = 0; i < k; i++) {
    if (arr[i] < 100) {
      sum += arr[i];
    }
  }
  return arr.slice(k).reduce((acc, curr) => acc + curr, sum);
};


D:
const addElements = (arr, k) => {
  let sum = arr.filter((num, i) => i < k && num < 100).reduce((acc, curr) => acc + curr, 0);
  return arr.slice(k).reduce((acc, curr) => acc + curr, sum);
};


E:
const addElements = (arr, k) => {
  const first = arr.slice(0, k);
  const second = arr.slice(k);
  return first.filter(num => num < 100).reduce((acc, curr) => acc + curr, 0) + second.reduce((acc, curr) => acc + curr, 0);
};


F:
const addElements = (arr, k) => {
  let sum = 0;
  for (let i = 0; i < k; i++) {
    if (arr[i] < 100) {
      sum += arr[i];
    }
  }
  return sum + arr.slice(k).reduce((acc, curr) => acc + curr, 0);
};


G:
const addElements = (arr, k) => {
  const first = arr.slice(0, k);
  const second = arr.slice(