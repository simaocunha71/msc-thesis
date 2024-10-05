  let sentences = S.split(/[.?!]/);
  let count = 0;
  for (const sentence of sentences) {
    let words = sentence.split(' ');
    if (words[0] == 'I') {
      count += 1;
    }
  }
  return count;
}

