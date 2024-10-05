  var words = s.split(' ');
  return words.map((word) => {
    return word.split('').sort().join('');
  }).join(' ');
}



