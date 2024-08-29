  let result = [];
  const split_by = /[\s,]+/;
  for (const w of txt.match(split_by) || []) {
    result.push(w);
  }
  if (result.length == 0) {
    let count = 0;
    for (const c of txt) {
      if (c.match(/[a-z]/i) && (ord(c) % 2 == 1)) {
        count += 1;
      }
    }
    return count;
  } else {
    return result;
  }
}



