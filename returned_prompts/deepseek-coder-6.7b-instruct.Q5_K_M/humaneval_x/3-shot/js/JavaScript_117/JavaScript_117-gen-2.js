  const consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';
  return s.split(' ').filter(word => {
    let count = 0;
    for (let char of word) if (consonants.includes(char)) count++;
    return count === n;
  });
}



