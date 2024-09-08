  const vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'];
  const consonants = 'BCDEFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz';

  let words = s.split(' ');
  let result = [];

  for (let w of words) {
    let count = 0;
    for (let c of w) {
      if (consonants.indexOf(c) >= 0) {
        count += 1;
      }
    }
    if (count === n) {
      result.push(w);
    }
  }

  return result;
}



