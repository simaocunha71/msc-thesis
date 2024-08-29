  if (s.length < 3) {
    return false;
  }

  const letters = s.split('');
  for (let i = 0; i < letters.length - 2; i++) {
    const letter1 = letters[i];
    const letter2 = letters[i + 1];
    const letter3 = letters[i + 2];
    if (letter1 === letter2 || letter2 === letter3 || letter1 === letter3) {
      return false;
    }
  }
  return true;
}



