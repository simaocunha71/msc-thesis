  let even_count = 0;
  for (let num of lst1) {
    if (num % 2 == 0) {
      even_count++;
    }
  }
  for (let num of lst2) {
    if (num % 2 == 0) {
      even_count++;
    }
  }
  return even_count == lst1.length;
}