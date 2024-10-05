const canArrange = (arr) => {
  let index = -1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < arr[i - 1]) {
      index = i;
    }
  }
  return index;
};

