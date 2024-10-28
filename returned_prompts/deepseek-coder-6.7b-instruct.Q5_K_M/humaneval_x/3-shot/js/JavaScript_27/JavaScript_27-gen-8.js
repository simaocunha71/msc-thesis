  return string.split('').map(char => {
    return char === char.toLowerCase()
      ? char.toUpperCase()
      : char.toLowerCase();
  }).join('');
}



