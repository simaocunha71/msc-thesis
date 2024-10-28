  let totalApples = 0, totalOranges = 0;
  let words = s.split(' ');
  for (let i = 0; i < words.length; i++) {
    if (words[i].includes('apples')) {
      totalApples = parseInt(words[i].replace('apples', ''));
    }
    if (words[i].includes('oranges')) {
      totalOranges = parseInt(words[i].replace('oranges', ''));
    }
  }
  return n - totalApples - totalOranges;
}