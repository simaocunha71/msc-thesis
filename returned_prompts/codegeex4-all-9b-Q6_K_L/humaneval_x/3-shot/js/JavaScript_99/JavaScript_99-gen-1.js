  var number = parseFloat(value);
  var integer = Math.round(number);
  if (number - integer === 0.5) {
    integer = Math.sign(number) * Math.ceil(Math.abs(number));
  }
  return integer;
}

