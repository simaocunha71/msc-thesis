  var str = String(x);
  var length = str.length;
  var result = "";

  if (shift > length) {
    result = str.split("").reverse().join("");
  } else {
    result = str.split("").slice(shift).concat(str.split("").slice(0, shift)).join("");
  }
  return result;
}



