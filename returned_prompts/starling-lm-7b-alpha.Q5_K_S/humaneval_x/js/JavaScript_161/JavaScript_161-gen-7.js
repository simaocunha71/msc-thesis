  let result = "";
  let isLetter = false;
  for (const c of s) {
    if (c.match(/[a-z]/i)) {
      isLetter = true;
      result += c.match(/[a-z]/i).toUpperCase();
    } else {
      result += c;
    }
  }
  if (!isLetter) {
    result = result.split("").reverse().join("");
  }
  return result;
}



