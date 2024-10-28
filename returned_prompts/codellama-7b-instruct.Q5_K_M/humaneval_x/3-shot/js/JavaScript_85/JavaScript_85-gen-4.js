  var sum = 0;
  var is_even = false;
  for (var i = 0; i < lst.length; i++) {
    if (is_even) {
      sum += lst[i];
    }
    is_even = !is_even;
  }
  return sum;
}



