  const roman = {
    M: 1000, D: 500, C: 100, L: 50, X: 10, V: 5, I: 1
  };

  const keys = Object.keys(roman);
  const values = Object.values(roman);

  let result = '';

  while (number > 0) {
    for (let i = 0; i < keys.length; i++) {
      if (number >= values[i]) {
        result += keys[i];
        number -= values[i];
        break;
      }
    }
  }

  return result;
}



