  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
  )).join("");
}

const encode = (s) => {
  var result = "";
  for (const ch of s) {
    if (ch >= "a" && ch <= "z") {
      result += encodeShift(ch);
    } else {
      result += ch;
    }
  }
  return result;
}

const decode = (s) => {
  var result = "";
  for (const ch of s) {
    if (ch >= "a" && ch <= "z") {
      result += decodeShift(ch);
    } else {
      result += ch;
    }
  }
  return result;
}



