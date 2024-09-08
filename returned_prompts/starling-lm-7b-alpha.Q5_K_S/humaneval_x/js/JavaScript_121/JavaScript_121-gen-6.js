  let total = 0;
  let counter = 0;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] % 2 == 0 && counter % 2 == 0) {
      total += lst[i];
    }
    counter++;
  }
  return total;
}



