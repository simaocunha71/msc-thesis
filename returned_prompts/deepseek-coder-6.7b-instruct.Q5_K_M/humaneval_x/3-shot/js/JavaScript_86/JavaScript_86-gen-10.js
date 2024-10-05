  return s.split(' ').map((word) => {
    return word.split('').sort((a, b) => {
      return a.charCodeAt(0) - b.charCodeAt(0);
    }).join('');
  }).join(' ');
}



