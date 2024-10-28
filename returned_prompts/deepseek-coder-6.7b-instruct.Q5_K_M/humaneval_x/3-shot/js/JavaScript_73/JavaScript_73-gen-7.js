  let changes = 0;

  for (let i = 0; i < Math.floor(arr.length / 2); i++) {
    if (arr[i] !== arr[arr.length - 1 - i]) {
      changes++;
    }
  }

  return changes;
}



