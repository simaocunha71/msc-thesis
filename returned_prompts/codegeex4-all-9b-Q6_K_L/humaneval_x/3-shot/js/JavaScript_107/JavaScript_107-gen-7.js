  var even_count = 0;
  var odd_count = 0;
  for (let i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      even_count += 1;
    } else {
      odd_count += 1;
    }
  }
  return [even_count, odd_count];
}