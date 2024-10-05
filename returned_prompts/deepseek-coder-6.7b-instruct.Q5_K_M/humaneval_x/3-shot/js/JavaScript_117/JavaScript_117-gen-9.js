  const consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';
  return s.split(' ').filter(word => {
    let count = 0;
    for (let i = 0; i < word.length; i++) {
      if (consonants.includes(word[i])) count++;
    }
    return count === n;
  });
}



