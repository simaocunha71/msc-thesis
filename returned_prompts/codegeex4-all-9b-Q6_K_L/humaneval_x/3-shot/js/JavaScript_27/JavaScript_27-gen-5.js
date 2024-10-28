  return string.split('').map(char => char.toUpperCase() === char ? char.toLowerCase() : char.toUpperCase()).join('');
}



