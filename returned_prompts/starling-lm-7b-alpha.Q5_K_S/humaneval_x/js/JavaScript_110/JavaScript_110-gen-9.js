  let odd_count = 0;
  for (const num of lst1) {
    if (num % 2 != 0) odd_count += 1;
  }
  if (odd_count == 0) return "YES";
  for (const num of lst2) {
    if (num % 2 != 0) {
      lst1.splice(odd_count, 1, num);
      odd_count += 1;
    }
  }
  if (odd_count == lst1.length) return "NO";
  else return "YES";
}



