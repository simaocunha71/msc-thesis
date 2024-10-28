  const lowerCase = 'abcdefghijklmnopqrstuvwxyz';
  const upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const result = [];

  s.split('').forEach(char => {
    if(lowerCase.includes(char)) {
      char = char.toUpperCase();
    } else {
      char = char.toLowerCase();
    }
    result.push(char);
  });

  return result.join('');
}

