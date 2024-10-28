  return string.split('').map(c => c == c.toLowerCase() ? c.toUpperCase() : c.toLowerCase()).join('');
}