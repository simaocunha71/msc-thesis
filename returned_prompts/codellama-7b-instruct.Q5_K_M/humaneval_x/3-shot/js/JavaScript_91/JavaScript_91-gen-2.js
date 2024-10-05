  let count = 0;
  for (let sentence of S.split(/[.?!]/)) {
    if (sentence.startsWith('I')) {
      count += 1;
    }
  }
  return count;
}



