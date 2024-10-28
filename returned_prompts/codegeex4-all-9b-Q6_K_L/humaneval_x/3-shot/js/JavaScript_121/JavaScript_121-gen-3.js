  var sum = 0;
  for (var i = 0; i < lst.length; i++) {
    if (i % 2 == 1 && lst[i] % 2 == 1) {
      sum += lst[i];
    }
  }
  return sum;
}