  let num = parseFloat(value);
  if (num < 0) {
    return Math.floor(num - 0.5) + 1;
  } else {
    return Math.floor(num + 0.5);
  }
}



