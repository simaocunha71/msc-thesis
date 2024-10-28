  let sentences = S.split(/[.?!]/);
  return sentences.reduce((count, sentence) => {
    return count + (sentence.trim().startsWith('I') ? 1 : 0);
  }, 0);
}



