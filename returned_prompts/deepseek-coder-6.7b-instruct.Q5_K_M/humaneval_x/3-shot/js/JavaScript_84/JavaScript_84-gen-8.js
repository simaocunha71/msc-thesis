  var binary_N = (N >>> 0).toString(2);
  var sum = 0;
  for  (var i = 0; i < binary_N.length; i++) {
    sum += parseInt(binary_N[i]);
  }
  return sum.toString(2);
}



