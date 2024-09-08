  let num = parseFloat(value);
  if (num >= 0) {
    return Math.floor(num + 0.5);
  } else {
    return Math.ceil(num - 0.5);
  }
}



