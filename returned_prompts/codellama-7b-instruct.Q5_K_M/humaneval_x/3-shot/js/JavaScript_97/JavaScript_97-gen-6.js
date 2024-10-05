  var product = 0;

  for (var i = 0; i < a.toString().length; i++) {
    product += parseInt(a.toString().charAt(i)) * parseInt(b.toString().charAt(i));
  }

  return product;
}



