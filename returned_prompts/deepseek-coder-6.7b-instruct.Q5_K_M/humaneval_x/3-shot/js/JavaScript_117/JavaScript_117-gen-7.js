  const consonants = 'bcdfghjklmnpqrstvwxyz';
  return s.split(' ').filter(word => {
    let count = 0;
    for (let char of word.toLowerCase()) {
      if (consonants.includes(char)) count++;
    }
    return count === n;
  });
}



