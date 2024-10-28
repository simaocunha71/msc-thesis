  let count = 0;
  for (let i = 2; a != 1; i++) {
    while (a % i == 0) {
      count++;
      a /= i;
    }
  }
  return count == 3;
}



