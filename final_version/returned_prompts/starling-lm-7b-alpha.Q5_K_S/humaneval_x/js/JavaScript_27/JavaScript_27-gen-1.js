  return string.split('').map(c => {
    if (c === c.toLowerCase()) {
      return c.toUpperCase();
    } else {
      return c.toLowerCase();
    }
  }).join('');
}



