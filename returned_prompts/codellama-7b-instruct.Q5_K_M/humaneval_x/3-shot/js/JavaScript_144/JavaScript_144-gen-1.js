  var x_numerator = parseInt(x.split('/')[0]);
  var x_denominator = parseInt(x.split('/')[1]);
  var n_numerator = parseInt(n.split('/')[0]);
  var n_denominator = parseInt(n.split('/')[1]);

  if (x_numerator * n_denominator === n_numerator * x_denominator) {
    return true;
  } else {
    return false;
  }
}



