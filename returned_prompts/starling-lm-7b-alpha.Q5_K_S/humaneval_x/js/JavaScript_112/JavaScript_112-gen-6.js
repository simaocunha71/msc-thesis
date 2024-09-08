  let newS = s;
  for (const char of c) {
    while (newS.includes(char)) {
      newS = newS.replace(char, '');
    }
  }

  const reversedS = newS.split('').reverse().join('');
  return [newS, reversedS === newS];
}



