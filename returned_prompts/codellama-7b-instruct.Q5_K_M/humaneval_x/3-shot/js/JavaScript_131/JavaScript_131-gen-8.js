  var product = 1;
  var string = n.toString();

  for (var i = 0; i < string.length; i++) {
    if (string[i] % 2 != 0) {
      product *= parseInt(string[i]);
    }
  }

  return product;
}



