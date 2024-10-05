  let words = s.split(' ');
  let count = 0;
  for (let i = 0; i < words.length; i++) {
    if (words[i].includes('apples')) {
      count += parseInt(words[i].split(' ')[0]);
    } else if (words[i].includes('oranges')) {
      count += parseInt(words[i].split(' ')[0]);
    }
  }
  return n - count;
}