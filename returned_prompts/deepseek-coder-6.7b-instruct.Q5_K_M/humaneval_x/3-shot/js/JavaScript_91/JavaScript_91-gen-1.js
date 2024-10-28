  let sentences = S.split(/[.?!]/);
  let count = 0;
  for(let i = 0; i < sentences.length; i++) {
      if(sentences[i].trim().startsWith('I')) {
          count++;
      }
  }
  return count;
}



