  return s.split("").map((c) => {
    if (c.match(/[a-zA-Z]/)) {
      return c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase();
    } else {
      return c;
    }
  }).join("");
}



