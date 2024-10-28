  let words = s.split(' ');
  let result = [];
  let consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';

  for(let word of words) {
    let count = 0;
    for(let char of word) {
      if(consonants.includes(char)) {
        count++;
      }
    }
    if(count === n) {
      result.push(word);
    }
  }

  return result;
}



