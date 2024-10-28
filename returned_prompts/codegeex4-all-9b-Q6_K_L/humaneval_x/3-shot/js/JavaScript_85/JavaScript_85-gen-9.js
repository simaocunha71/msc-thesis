  var sum = 0;
  for (var i = 0; i < lst.length; i += 2) {
    if (lst[i] % 2 == 0) {
      sum += lst[i];
    }
  }
  return sum;
}



