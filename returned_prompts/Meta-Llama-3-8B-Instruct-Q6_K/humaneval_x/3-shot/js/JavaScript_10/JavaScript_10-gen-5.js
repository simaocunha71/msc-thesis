  let revStr = string.split("").reverse().join("");
  let len = string.length;
  for (let i = 0; i < len; i++) {
    if (string.slice(0, len - i) === revStr.slice(i)) {
      return string + revStr.slice(i);
    }
  }
  return string + revStr;
}