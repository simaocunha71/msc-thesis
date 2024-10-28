  let result = "";
  for (const c of s) {
    if (c.match(/[a-zA-Z]/)) {
      result += c === c.toUpperCase() ? c.toLowerCase() : c.toUpperCase();
    } else {
      result += c;
    }
  }
  return result.split("").reverse().join("");
}