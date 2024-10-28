  if (arr.length == 0) {
    return null;
  }

  var result = 0;
  var sign_prod = 1;

  for (const num of arr) {
    result += Math.abs(num);
    sign_prod *= Math.sign(num);
  }

  return result * sign_prod;
}