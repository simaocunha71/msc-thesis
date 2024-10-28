  return string.split('').map(c => {
    if (c.match(/[a-z]/)) {
      return c.toUpperCase();
    } else {
      return c.toLowerCase();
    }
  }).join('');
}



