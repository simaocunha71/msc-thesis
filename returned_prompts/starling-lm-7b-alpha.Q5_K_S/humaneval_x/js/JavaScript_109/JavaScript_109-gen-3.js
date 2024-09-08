  let max_index = 0;
  let max = arr[0];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
      max_index = i;
    }
  }

  for (let i = 0; i < max_index; i++) {
    let temp = arr[i];
    arr[i] = arr[i + 1];
    arr[i + 1] = temp;
  }

  return arr.every((val, idx) => {
    return val <= arr[idx + 1];
  })
}



