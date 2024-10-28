  return string.split('').map(c => c.toLowerCase() === c ? c.toUpperCase() : c.toLowerCase()).join('');
}