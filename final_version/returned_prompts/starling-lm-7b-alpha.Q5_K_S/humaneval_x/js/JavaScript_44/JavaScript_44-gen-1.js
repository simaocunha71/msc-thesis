  const digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
  let result = "";
  while (x) {
    result += digits[x % base];
    x = Math.floor(x / base);
  }
  return result.split("").reverse().join("");
}



