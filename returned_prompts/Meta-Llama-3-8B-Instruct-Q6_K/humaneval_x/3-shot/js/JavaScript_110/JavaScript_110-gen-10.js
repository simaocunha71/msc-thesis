  let count_odd = 0;

  for (let num of lst1) {
    if (num % 2 != 0) {
      count_odd += 1;
    }
  }

  for (let num of lst2) {
    if (num % 2 != 0) {
      count_odd -= 1;
    }
  }

  return count_odd === 0 ? "YES" : "NO";
}