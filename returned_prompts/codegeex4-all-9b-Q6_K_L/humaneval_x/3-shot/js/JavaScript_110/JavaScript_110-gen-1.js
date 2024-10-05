  let even_count = 0;
  for (const num of lst1) {
    if (num % 2 == 0) {
      even_count += 1;
    }
  }
  let odd_count = lst2.length - even_count;
  if (even_count == lst1.length) {
    return 'YES';
  } else if (odd_count == lst1.length) {
    return 'NO';
  } else {
    return 'YES';
  }
}



