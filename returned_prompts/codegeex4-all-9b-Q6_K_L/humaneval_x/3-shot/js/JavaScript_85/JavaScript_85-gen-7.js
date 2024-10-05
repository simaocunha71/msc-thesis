  var sum = 0;
  for (var i = 1; i < lst.length; i += 2) {
    if (lst[i] < 0) {
      sum += lst[i];
    }
  }
  return sum;
}