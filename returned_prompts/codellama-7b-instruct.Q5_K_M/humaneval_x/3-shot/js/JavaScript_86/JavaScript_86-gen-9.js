  return s.split(' ').map((word) => {
    return word.split('').sort().join('');
  }).join(' ');
}



