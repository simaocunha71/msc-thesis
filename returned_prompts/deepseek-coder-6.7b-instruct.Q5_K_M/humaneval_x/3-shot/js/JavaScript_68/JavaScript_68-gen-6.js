  let smallest = Infinity, index = -1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < smallest && arr[i] % 2 === 0) {
      smallest = arr[i];
      index = i;
    }
  }
  return index === -1 ? [] : [smallest, index];
}



