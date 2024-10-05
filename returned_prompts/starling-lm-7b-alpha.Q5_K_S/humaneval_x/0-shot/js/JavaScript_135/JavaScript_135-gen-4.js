  let max = arr[0];
  let index = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
      index = i;
    }
  }

  return index;
};

canArrange([1, 2, 4, 3, 5]) // 3
canArrange([1, 2, 3]) // -1



// Another solution:

const canArrange = (arr) => {
  let max = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max && arr[i] > arr[i - 1]) {
      max = arr[i];
    }
  }
  return max === arr[arr.length - 1] ? arr.length - 1 : -1;
};

canArrange([1, 2, 4, 3, 5]) // 3
canArrange([1, 2, 3]) // -1



// Another solution:

const canArrange = (arr) => {
  let max = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max && arr[i] > arr[i - 1]) {
      max = arr[i];
    }
  }
  return max === arr[arr.length - 1] ? arr.length - 1 : -1;
};

canArrange([1, 2, 4, 3, 5]) // 3
canArrange([1, 2, 3]) // -1



// Another solution:

const canArrange = (arr) => {
  let max = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max && arr[i] > arr[i - 1]) {
      max = arr[i];
    }
  }
  return max === arr[