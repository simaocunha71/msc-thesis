  let changes = 0;

  for (let i = 0, j = arr.length - 1; i < j; i++, j--) {
    if (arr[i] != arr[j]) {
      changes += 1;
    }
  }

  return changes;
}



