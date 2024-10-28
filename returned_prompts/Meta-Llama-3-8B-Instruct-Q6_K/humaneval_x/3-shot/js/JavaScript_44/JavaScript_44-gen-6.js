  var digits = "0123456789";
  var result = "";

  while (x > 0) {
    result = digits[x % base] + result;
    x = Math.floor(x / base);
  }

  return result;
}