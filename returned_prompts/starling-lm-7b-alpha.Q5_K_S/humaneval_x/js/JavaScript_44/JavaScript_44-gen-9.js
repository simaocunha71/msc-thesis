  let result = "";
  while (x > 0) {
    result += String(x % base);
    x = Math.floor(x / base);
  }

  return result.split("").reverse().join("");
}



