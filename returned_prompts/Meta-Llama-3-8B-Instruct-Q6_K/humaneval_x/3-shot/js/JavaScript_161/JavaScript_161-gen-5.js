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
// OR
const solve = (s) => {
  let result = "";
  for (const c of s) {
    if (c.match(/[a-zA-Z]/)) {
      result += c === c.toUpperCase() ? c.toLowerCase() : c.toUpperCase();
    } else {
      result += c;
    }
  }
  if (!result.match(/[a-zA-Z]/)) {
    return result.split("").reverse().join("");
  }
  return result;
}