  const vowels = ['a', 'e', 'i', 'o', 'u'];
  return s.split(' ').filter(word => {
    let consonants = 0;
    for(let i = 0; i < word.length; i++) {
      if(!vowels.includes(word[i].toLowerCase())) {
        consonants++;
      }
    }
    return consonants === n;
  });
}


