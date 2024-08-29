  let result = "";
  for (const c of s) {
    if (c.match(/[a-zA-Z]/)) {
      result += c.match(/[a-z]/g) ? c.toUpperCase() : c.toLowerCase();
    } else {
      result += c;
    }
  }
  return result;
}



