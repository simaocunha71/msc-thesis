  const sum = s.split('')
    .filter(char => char.toUpperCase() === char)
    .reduce((acc, char) => acc + char.charCodeAt(0), 0);

  return sum;

