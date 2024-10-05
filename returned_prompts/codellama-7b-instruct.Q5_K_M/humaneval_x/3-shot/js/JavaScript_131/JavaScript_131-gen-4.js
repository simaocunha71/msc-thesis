  var result = 0;

  for (var i = 0; i < n.toString().length; i++) {
    if (n % 2 != 0) {
      result += parseInt(n.toString()[i]);
    }
  }

  return result;
}



