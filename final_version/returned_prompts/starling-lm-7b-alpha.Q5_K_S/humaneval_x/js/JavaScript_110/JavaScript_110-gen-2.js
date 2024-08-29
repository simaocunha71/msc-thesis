  let odd_count = 0;
  for (const n of lst1) {
    if (n % 2 != 0) {
      odd_count += 1;
    }
  }

  if (odd_count == 0) {
    return "YES";
  }

  for (const n of lst2) {
    if (n % 2 != 0) {
      odd_count -= 1;
      if (odd_count == 0) {
        return "YES";
      }
    }
  }

  return "NO";
}



