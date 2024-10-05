  let even = 0;
  let odd = 0;

  for (const num of lst1) {
    if (num % 2 == 0) {
      even += 1;
    } else {
      odd += 1;
    }
  }

  for (const num of lst2) {
    if (num % 2 == 0) {
      even += 1;
    } else {
      odd += 1;
    }
  }

  return even >= odd;
}