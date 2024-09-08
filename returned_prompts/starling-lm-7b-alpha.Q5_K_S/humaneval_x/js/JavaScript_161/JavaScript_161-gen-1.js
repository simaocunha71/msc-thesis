  return s.split('').map(c => {
    if (c.match(/[a-z]/)) {
      return c.toUpperCase();
    } else if (c.match(/[A-Z]/)) {
      return c.toLowerCase();
    } else {
      return c;
    }
  }).join('');
}



