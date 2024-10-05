  let num = parseFloat(value);
  if (num - Math.floor(num) < 0.5) {
    return Math.floor(num);
  } else {
    return Math.ceil(num);
  }
}