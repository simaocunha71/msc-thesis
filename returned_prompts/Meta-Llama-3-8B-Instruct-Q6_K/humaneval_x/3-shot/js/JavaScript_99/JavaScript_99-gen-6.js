  const num = parseFloat(value);
  if (num >= 0) {
    if (num % 1 >= 0.5) {
      return Math.ceil(num);
    } else {
      return Math.floor(num);
    }
  } else {
    if (Math.abs(num % 1) >= 0.5) {
      return Math.ceil(num);
    } else {
      return Math.floor(num);
    }
  }
}