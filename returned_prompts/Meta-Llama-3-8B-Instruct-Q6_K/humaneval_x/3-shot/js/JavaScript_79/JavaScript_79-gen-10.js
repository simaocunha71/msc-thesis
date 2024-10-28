  let binary = (decimal >>> 0).toString(2);
  return "db" + binary + "db";
}  // This function uses bitwise right shift operator (>>) to convert decimal to binary. The (>>> 0) is used to remove the negative sign if the decimal is negative. Then, it converts it to a binary string using toString(2). Finally, it adds the extra characters 'db' at the beginning and the end.