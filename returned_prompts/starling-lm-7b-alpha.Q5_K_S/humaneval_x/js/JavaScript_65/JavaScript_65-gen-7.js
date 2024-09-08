  let digits = String(x).split("");
  let n = digits.length;
  if (shift > n) {
    shift = (shift % n) + n;
  }
  digits = digits.slice(shift).concat(digits.slice(0, shift));
  return parseInt(digits.join(""));
}



