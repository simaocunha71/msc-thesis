  var words = s.split(' ');
  for (var i = 0; i < words.length; i++) {
    words[i] = words[i].split('').sort().join('');
  }
  return words.join(' ');
}