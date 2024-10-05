  var result = [];
  var remainder = x % base;
  var quotient = Math.floor(x / base);

  if (quotient == 0) {
    result.push(remainder);
  } else {
    result.push(changeBase(quotient, base));
  }

  return result.join('');
}



