  let counter = 0;

  for (let i = 0; i < n; i++) {
    for (let j = i; j < n; j++) {
      if (i < j) {
        counter++;
      }
    }
  }
  return counter;
}
