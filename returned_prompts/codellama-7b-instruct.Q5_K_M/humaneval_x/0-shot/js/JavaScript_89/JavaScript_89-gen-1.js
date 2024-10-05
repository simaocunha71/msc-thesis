  const rot = (c) => {
    return String.fromCharCode(c.charCodeAt(0) - 2 * 2);
  };
  return s.split('').map(rot).join('');
}