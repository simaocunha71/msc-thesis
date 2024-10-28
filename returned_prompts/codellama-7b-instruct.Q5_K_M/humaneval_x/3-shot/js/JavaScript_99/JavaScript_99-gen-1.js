  let num = parseFloat(value);
  if (num % 1 === 0.5) {
    return parseInt(num) % 2 === 0 ? parseInt(num) : parseInt(num) + 1;
  }
  else {
    return Math.round(num);
  }
}



