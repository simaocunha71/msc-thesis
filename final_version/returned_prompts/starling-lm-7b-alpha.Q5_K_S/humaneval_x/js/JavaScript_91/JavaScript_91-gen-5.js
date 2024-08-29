  let words = S.split(" ");
  let numBoredoms = 0;
  for (let i = 0; i < words.length; i++) {
    if (words[i] === 'I') {
      let j = i + 1;
      while (j < words.length && words[j].match(/[.?!]/)) {
        j++;
      }
      if (j < words.length && (words[j] === '.' || words[j] === '?' || words[j] === '!')) {
        numBoredoms += 1;
      }
    }
  }
  return numBoredoms;
}



