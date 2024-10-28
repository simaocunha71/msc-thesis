  for (let i = 1; i < arr.length; i++) {
    if (arr[i - 1] <= arr[i]) {
      continue;
    } else {
      return i - 1;
    }
  }

  return -1;
}



