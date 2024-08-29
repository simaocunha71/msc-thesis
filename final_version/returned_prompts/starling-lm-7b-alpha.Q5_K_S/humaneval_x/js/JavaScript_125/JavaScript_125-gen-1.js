  const words = txt.split(/[\s,]+/);
  if (words.length === 0) {
    let count = 0;
    for (const c of txt) {
      if (c === c.toLowerCase() && (c - 'a') % 2 === 1) {
        count += 1;
      }
    }
    return count;
  } else {
    return words;
  }
}



