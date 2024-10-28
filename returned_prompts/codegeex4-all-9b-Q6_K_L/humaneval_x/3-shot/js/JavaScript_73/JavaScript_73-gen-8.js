  let changes = 0;
  for (let i = 0; i < arr.length / 2; i++) {
    if (arr[i] != arr[arr.length - i - 1]) {
      changes++;
    }
  }
  return changes;
}



