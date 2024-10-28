  let arr = [...l];
  for (let i = 0; i < l.length; i += 3) {
    arr[i] = l[i];
  }
  arr.sort((a, b) => a - b);
  for (let i = 2; i < l.length; i += 3) {
    arr[i] = l[i];
  }
  return arr;
}



