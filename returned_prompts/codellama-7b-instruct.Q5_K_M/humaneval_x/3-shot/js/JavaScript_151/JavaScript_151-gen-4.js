  var sum = 0.0;

  for (var i = 0; i < lst.length; i++) {
    if (Number.isInteger(lst[i]) && lst[i] >= 0) {
      sum += Math.pow(lst[i], 2);
    }
  }

  return sum;
}



