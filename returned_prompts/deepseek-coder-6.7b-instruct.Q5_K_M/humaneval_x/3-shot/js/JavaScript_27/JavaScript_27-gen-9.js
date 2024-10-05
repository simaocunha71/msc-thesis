  return string.split('').map(char => 
    char === char.toLowerCase() ? char.toUpperCase() : char.toLowerCase()
  ).join('');
}



