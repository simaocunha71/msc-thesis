  let words = s.split(' ');
  let consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';
  let result = [];

  for(let word of words) {
    let count = 0;
    for(let char of word) {
      if(consonants.includes(char)) count++;
    }
    if(count === n) result.push(word);
  }

  return result;
}


