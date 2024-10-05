  let count = 0;
  let i = 0;
  let j = arr.length - 1;

  while (i < j) {
    if (arr[i] != arr[j]) {
      count += 1;
    }
    i++;
    j--;
  }

  return count;
}