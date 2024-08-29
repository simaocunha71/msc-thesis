  let max = 0;
  for (let i = 0; i < lst.length; i++) {
    if (prime(lst[i])) {
      if (max < lst[i]) {
        max = lst[i];
      }
    }
  }
  let result = 0;
  while (max > 0) {
    result += max % 10;
    max = Math.floor(max / 10);
  }
  return result;
}



