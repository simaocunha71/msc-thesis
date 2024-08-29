  let counter = 0;
  for (let i = 0; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      if (i.toString().includes('7')) {
        counter += 1;
      }
    }
  }
  return counter;
}



