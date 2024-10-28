  let changes = 0;
  let start = 0;
  let end = arr.length - 1;

  while (start < end) {
    if (arr[start] !== arr[end]) {
      changes++;
    }
    start++;
    end--;
  }

  return changes;
}



