  let count = 0;
  let i = 0, j = arr.length - 1;

  while (i < j) {
    if (arr[i] !== arr[j]) {
      count++;
    }
    i++;
    j--;
  }

  return count;
}



