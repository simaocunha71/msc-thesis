  let result = 0;

  for (let i = 10; i < n; i += 10) {
    if (i % 11 == 0 || i % 13 == 0) {
      if (i % 10 == 7) {
        result += 1;
      }
    }
  }

  return result;
}



