  var sum = 0;
  var i = 0;
  while (i < lst.length) {
    if (lst[i] % 2 == 1) {
      sum += lst[i];
    }
    i += 2;
  }
  return sum;
}



