  var sum = 0;
  for (var i = 0; i < lst.length; i++) {
    sum += Math.pow(Math.ceil(lst[i]), 2);
  }
  return sum;
}