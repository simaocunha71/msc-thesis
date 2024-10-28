const reverseDelete = (s, c) => {
  const result = s.split('')
    .filter(char => !c.includes(char))
    .join('')
    .split('')
    .reverse()
    .join('');

  return [result, result.split('').every((char, i) => char === result.split('')[i])];
}
