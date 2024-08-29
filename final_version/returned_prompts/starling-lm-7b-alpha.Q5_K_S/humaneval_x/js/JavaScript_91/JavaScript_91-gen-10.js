  let words = S.split(/[!?.:] +/);
  let count = 0;
  for (let i = 0; i < words.length; i++) {
    if (words[i] === 'I') {
      count += 1;
    }
  }
  return count;
}



