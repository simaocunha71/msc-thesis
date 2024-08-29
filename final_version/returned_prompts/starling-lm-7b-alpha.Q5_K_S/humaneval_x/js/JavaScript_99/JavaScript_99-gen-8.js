  let parts = value.split('.');
  let integer = parseInt(parts[0]);
  let decimal = parts[1];

  if (decimal == '') {
    return integer;
  }

  if (decimal.length == 1) {
    return integer + parseInt(decimal);
  }

  return Math.round(parseInt(parts[0]) + parseFloat(parts[1]));
}



