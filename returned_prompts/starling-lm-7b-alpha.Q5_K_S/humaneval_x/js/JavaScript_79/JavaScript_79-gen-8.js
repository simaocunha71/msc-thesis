  let result = "db";
  while (decimal > 0) {
    result += String(decimal % 2);
    decimal = Math.floor(decimal / 2);
  }
  result += "db";
  return result;
}



