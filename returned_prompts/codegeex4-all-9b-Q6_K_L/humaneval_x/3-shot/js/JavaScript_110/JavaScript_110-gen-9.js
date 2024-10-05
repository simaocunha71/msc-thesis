  var even_count = 0;

  for (const num of lst1) {
    if (num % 2 == 0) {
      even_count += 1;
    }
  }

  for (const num of lst2) {
    if (num % 2 == 1) {
      even_count += 1;
    }
  }

  if (even_count == lst1.length) {
    return "YES";
  } else {
    return "NO";
  }
}