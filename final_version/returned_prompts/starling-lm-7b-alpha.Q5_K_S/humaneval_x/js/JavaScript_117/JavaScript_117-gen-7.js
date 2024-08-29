  let result = [];
  let isConsonant = (c) => {
    return "bcdfghjklmnpqrstvwxyz".includes(c.toLowerCase());
  }
  for (const word of s.split(" ")) {
    let count = 0;
    for (const c of word) {
      if (isConsonant(c)) {
        count += 1;
      }
    }
    if (count === n) {
      result.push(word);
    }
  }
  return result;
}



