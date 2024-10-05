  let seen = new Set();

  for (let c of string) {
    seen.add(c.toLowerCase());
  }

  return seen.size;
}



