  var result = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i] >= 'a' && s[i] <= 'z') {
      result += s[i].toUpperCase();
    } else if (s[i] >= 'A' && s[i] <= 'Z') {
      result += s[i].toLowerCase();
    } else {
      result += s[i];
    }
  }
  if (result.match(/[a-zA-Z]/g) == null) {
    result = result.split("").reverse().join("");
  }
  return result;
}

